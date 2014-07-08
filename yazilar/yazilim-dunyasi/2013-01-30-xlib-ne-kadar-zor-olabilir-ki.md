<!--
.. date: 2013-01-30 00:01:27
.. title: Xlib, ne kadar zor olabilir ki?
.. slug: xlib-ne-kadar-zor-olabilir-ki
.. description: Xlib kütüphaneleri'ni mi kullanmak istiyorsun? Manyak mısın? Ben ettim, siz etmeyin, Xlib kütüphanelerine bulaşmayın.
-->

Dün müydü, ondan önceki gün müydü hatırlamıyorum, aklıma bir fikir
geldi. Mouse ile tıkladığım noktaları bir yere kaydedeyim, bir kaç gün
veri topladıktan sonra da scatter plot'unu çizerim, enteresan birşey
olur diye düşündüm.

Mouse ile tıklanan noktaları bulmak kısmını Xlib ile yapmak gerekir diye
düşündüm, gui kütüphaneleri işimi görmüyordu, çünkü programın pencere
oluşturmadan arka planda çalışması, hangi pencere seçili olursa olsun,
mouse tıklanma durumunu görebilmesi lazımdı. Aradan bir miktar araştırma
süresi geçtikten sonra, \#xorg-devel'de şöyle bir muhabbet geçti; <!-- TEASER_END -->

<pre>yasar: Hi. I am trying to learn Xlib. Can I use XSelectInput on root window?
       Because I don't want to create a window, I am only interested in Mouse Events.

jcristau: why do you hate yourself that much?  anyway, yes.
</pre>

Ben bu `why do you hate yourself that much?` (kendinden niye bu kadar
nefret ediyorsun?) lafına o an tam bir anlam veremedim. Neyse, sorduğum
soru basit. XSelectInput fonksiyonu, bir girdi aygıtını dinlemeye
yarıyor. Ben bunu root pencerede, yani bütün pencerelerin içinde
bulunduğu pencerede kullanabilir miyim diye soruyorum. Aldığım cevap
olumlu, root pencerede buton tıklama olayını dinlemeye çalışıyorum, ama
bir sıkıntı var;

<pre>X Error of failed request: BadAccess (attempt to access private resource denied)
Major opcode of failed request: 2 (X_ChangeWindowAttributes)
Serial number of failed request: 7
Current serial number in output stream: 7
</pre>

Hmm, BadAccess diye bir hata aldım. Bunun ne olduğunu anlamak için de
baya bir zaman ve efor harcadım. [Meğersem][], tıklama olayını bir
pencerede, sadece bir client dinleyebiliyormuş, ve root penceredeki
tıklanma olayını da pencere yöneticisi dinliyormuş, ki bu çok mantıklı.
Ben bu aşamada, ümitlerimi biraz yitirmiştim aslında, ancak,
ButtonRelease (butonu salıverme) olayını aynı pencerede birden fazla
client dinleyebildiğini öğrendim. Benim amacım için, tıklanma olayı ile
salınma olayı arasında fazla bir fark yoktu, o yüzden işim çok kolay
oldu. ([Dermişim][]) Bunu denediğim kodlar şu şekilde;

	:::c
	#include <stdio.h>
	#include <stddef.h>
	#include <X11/Xlib.h>
	#include <assert.h>
	#include <unistd.h>
	#include <signal.h>


	int working = 1;

	void signal_callback_handler(int signum) {
		working = 0;
	}

	int main () {
		signal(SIGINT, signal_callback_handler);
		signal(SIGTSTP, signal_callback_handler);
		signal(SIGTERM, signal_callback_handler);

		Display *d = XOpenDisplay(NULL);
		assert(d);

		XSelectInput(d,DefaultRootWindow(d), ButtonReleaseMask);

		while(working) {
			XEvent e;
			XNextEvent(d, &e);
		printf("Something Occured");
			if (e.type == ButtonRelease) {
				printf("%dx%d",e.xbutton.x,e.xbutton.y);
		fflush(stdout);
			}
		}


		return 0;
	}

Evet, yukarıdaki kodda herşey güzel gibi görünüyor. Hata falan da
almıyorum. Ama aksi gibi, bir çıktı da almıyorum. Peki neden mi? Hiçbir
fikrim yok :)

Aslında yukarıdaki olayları anlatırken, kronolojik sıraya dikkat
etmedim. Bu olaylar olurken, aynı zamanda şöyle birşey öğrendim: \`It's
possible to read XI\_RawButtonPress events from the root window if that
helps\`. Diyor ki, XI\_RawButtonPress olayını root pencereden
dinleyebilirsin. Peki, bu XI\_RawButtonPress ne mi? X input extensions
diye bir kütüphane varmış, Bu kütüphane işlenmemiş (raw) olayları
dinleyeme izin veriyormuş. Yanlış anlamadıysam, ki yanlış anlamış olma
ihtimalim var, bu kütüphaneyi biraz karmaşık ihtiyaçları olan, oyunlar,
gibi programlar kullanıyor. Neyse, biraz ileri saralım, ben bu konuda
biraz aşama kaydettim, ve root pencereden işlenmemiş tıklanma olaylarını
dinleyebilmeyi başardım. En son olarak kullandığım kodlar şu şekilde;

	:::c
	#include <stdio.h>
	#include <X11/Xlib.h>
	#include <X11/extensions/XInput2.h>
	#include <signal.h>
	#include <unistd.h>

	FILE *f;

	int working = 1;

	/* This functions recieves XI_RawButtonPress event */
	void handle_raw_event(XIRawEvent *ev) {
	  if(ev->detail == 1) {/* I am only interested in left button clicks */
			fprintf(f,"%u\n",time(NULL));
			fflush(f);
		}
	}

	int main() {
		Display *dpy = XOpenDisplay(NULL);

		/* XInput Extension available? */
		int opcode, event, error;
		if (!XQueryExtension(dpy, "XInputExtension", &opcode, &event, &error)) {
			printf("X Input extension not available.\n");
			return -1;
		}

		/* Which version of XI2? We support 2.0 */
		int major = 2, minor = 1;
		if (XIQueryVersion(dpy, &major, &minor) == BadRequest) {
			printf("XI2 not available. Server supports %d.%d\n", major, minor);
			return -1;
		}

		f = fopen("/home/yasar/.mouselogs/log","a");
		XIEventMask eventmask;

		unsigned char mask[2] = { 0 }; /* the actual mask */

		eventmask.deviceid = XIAllMasterDevices;
		eventmask.mask_len = sizeof(mask); /* always in bytes */
		eventmask.mask = mask;

		/* now set the mask */
		XISetMask(mask, XI_RawButtonPress);

		/* select on the window */
		XISelectEvents(dpy, DefaultRootWindow(dpy), &eventmask, 1);
		while(working) {
			XEvent ev;
			usleep(10000);
			while(XPending(dpy)) {
				XNextEvent(dpy, &ev);
				if (XGetEventData(dpy, &ev.xcookie))
				{
					switch(ev.xcookie.evtype)
					{
						case XI_RawButtonPress:
							handle_raw_event(ev.xcookie.data);
							break;
					}
				}
				XFreeEventData(dpy, &ev.xcookie);
			}
		}
		fflush(f);
		fclose(f);
	}

(Yukarıdaki kodlar çok gelişigüzel bir şekilde yazılıp, göstermek
amaçlı konulmuştur.)

Bu programı, pencere yöneticisinin oto-başlat listesine ekledim.
Malesef, henüz hala XIRawEvent içinden nasıl x ve y koordinatları alınır
bilmiyorum, o yüzden sadece tıklanma zamanlarını kaydediyorum. Belki bu
verilerden de ilginç bir analiz çıkabilir.

Süreç boyunca olanları daha yakından incelemek isteyenler için, [SO
sorusu][] ve 

Tüm bunları yazmaya başlamadan önce, aklımda vermek istediğim bir mesaj
vardı, galiba açık kaynak dünyasında düzgün ve kapsamlı belgelendirmenin
önemi hakkında birşeydi. İyi düşünülmüş, insanları düşünmeye sevk eden
birşey olacaktı, ama o kadar yazacak enerjim kalmadı. Sadece hikayemi
paylaşmış olmakla yetineceğim. Ve, genç programcılara bir tavsiye, Xlib
olayına bulaşmayın.

  [Meğersem]: http://www.eksisozluk.com/show.asp?t=me%C4%9Fersem
  [Dermişim]: http://www.eksisozluk.com/show.asp?t=dermi%C5%9Fim
  [SO sorusu]: http://stackoverflow.com/q/14561267/886669