<!--
.. date: 2012-08-25 20:43:00
.. title: Python threading modülü
.. slug: threading
.. description: Python'da paralel işlem yapmaya yarayan iki modülden biri olan threading modülünün mantığını ve kullanımını örneklerle anlatan bu yazı, yeni başlayanlara yöneliktir.
-->

Python'da paralel işlem yapmak için seçenek çok. Standart Python
kütüphanesindeki threading, multiprocessing, subprocess gibi üst-seviye
modüller bu işleri diğer dillere bakılırsa bir seviye daha
kolaylaştırıyor. Standart modül dışında da, bu amaçlar için yazılmış
[stackless][] gibi modüller de var. Bu yazıda threading modülü
incelenecek. Ne yazık ki, bu modül hakkında Türkçe kaynak bulmak
konusunda sıkıntı var. Bu nedenle, bu yazıda pratik örneklerle, bu
modülün kullanılışı anlatılmaya çalışılacak.

Devam etmeden önce, process ve thread arasındaki farklara değinmekte
fayda var. Threadler aynı işlem içerisinden, birkaç daldan çalışırlar.
Yani, aynı hafızayı ve kaynakları kullanırlar. Bir başka deyişle, birkaç
farklı thread, aynı veri üzerinde çalışabilir. Bu bir yandan daha hafif
olmak ve thread'ler arasında iletişimin kolaylığı gibi üstünlüklere
neden olsa da, diğer yandan kendine ait sorunları da beraberinde
getirir. Bu sorunlara örnek olarak, [deadlock][] ve
[race-condition][] verilebilir. İşin güzel yanı ise, Python'daki GIL
(Global Interpreter Lock) ve queue modülü sayesinde, Python'da
thread'leri kullanmak diğer dillerden daha basittir. <!-- TEASER_END -->

Örnekleri Python 2.7'ye göre vereceğim. Kullandığım bazı özellikler,
eski versiyonlarda olmayabilir veya 3.x versiyonlarında biraz
değiştirilmiş olabilir. Ancak, bu, yazıyı takip etmeyi engellemez. İşin
mantığı ve yönteminde önemli farklılıklar yoktur.

Temel bir örnekle başlayalım;

    :::python
    from time import sleep
    from threading import Thread
    
    def tekrarla(ne, bekleme):
        while True:
            print ne
            sleep(bekleme)
    
    if __name__ == '__main__':
        dum = Thread(target = tekrarla, args = ("dum",1))
        tis = Thread(target = tekrarla, args = ("tis",0.5))
        ah = Thread(target = tekrarla, args = ("ah",3))
        
        dum.start()
        tis.start()
        ah.start()

Bu örneği çalıştırırsanız, şuna benzer bir çıktı alacaksınız;

<pre>
dum
tis
ah

tis
dumtis

tis
dumtis

tis
ah
tisdum
</pre>

Çıktıyı incelersek, "dum","tis" ve "ah" kelimelerinin karışık şekilde
yazıldığını görüyoruz. Kodları incelediğimizde, önce `sleep` fonksiyonu
ve `Thread` sınıfı içe aktarılıyor. Daha sonra, `tekrarla` isimli bir
fonksiyon tanımlanıyor. Bu fonksiyon, kendisine verilen bir kelimeyi,
kendisine verilen zaman aralıklarında sürekli tekrarlayan bir fonksiyon.

Daha sonra 3 adet `Thread` oluşturulduğunu görüyoruz. Bunların hepsi,
kendilerine ait değişkenlere atanmışlar. Bunları oluştururken, bu
thread'in hangi fonksiyonu çalıştıracağını nasıl belirledik, ve bu
fonksiyona nasıl argümanları geçirdik dikkatle inceleyin.

Son 3 satır, bu thread'lerin çalışmaya başladığı yer. Dikkat ediniz,
bunlar oluşturulduğunda çalışmaya başlamıyor. `start()` metodunu
kullandığımızda çalışmaya başlıyorlar. Böylece örneğimiz tamamlanmış
oluyor.

Yukarıda bahsedildiği gibi, thread'ler, kaynakların paylaşılması
gerektiği zaman karmaşık hale gelebilir. Threading modülü, thread'ler
arası zamanlamayı ayarlamak için `Lock()` ve `Event()` sınıfları gibi
temel yöntemlere sahip olsa da, `Queue()` (sıra) kullanmak daha çok
tercih edilen bir yöntem. Queue'lerin kullanılması hem daha kolay, hem
de daha güvenlidir. Bunlarla çalışmak daha temiz ve anlaşılırdır.

Aşağıda ilk önce, thread kullanmadan, birer birer web sayfası okuyan bir
programcık örneği gösterilecek. Bu örnek, thread'lerle daha hızlı
gerçekleştirilebilecek şeyler arasında klasik bir örnektir.

    :::python
    import urllib
    from time import time
    siteler = ("http://www.python.org",
               "http://istihza.com",
               "http://yasararabaci.tumblr.com",
               "http://metehan.us",
               "http://blog.tanshaydar.com",
               "http://fatihmertdogancan.wordpress.com",
               "http://ozgurerdogdu.blogspot.com/")
    
    start = time()
    
    for site in siteler:
        f = urllib.urlopen(site)
        _ = f.read() # okudugum veriyi goz ardi ediyorum, bu ornekte gerek yok.
        f.close()
    print "%f saniye surdu" % (time() - start)

Bu kodu çağırdığınızda, okunan web sitelerini görmeyeceksiniz, çünkü
gerek olmadığı için bir yere kaydetmedik veya ekrana bastırmadık. Ancak,
işin sonunda, toplam ne kadar sürede bunların okunduğunu görebilirsiniz.
Bunu yazdığım bilgisayarda, 8-10 saniye kadar sürdü. Kod bir hayli açık
olduğundan açıklamaya gerek yok.

Şimdi de thread örneğine bakalım;

    :::python
    from threading import Thread
    from Queue import Queue
    from urllib import urlopen
    from time import time
    
    sira = Queue()
    
    siteler = ("http://www.python.org",
               "http://istihza.com",
               "http://yasararabaci.tumblr.com",
               "http://metehan.us",
               "http://blog.tanshaydar.com",
               "http://fatihmertdogancan.wordpress.com",
               "http://ozgurerdogdu.blogspot.com/")
    
    def siteokuyan(que):
        while True:
            site = que.get()
            f = urlopen(site)
            _ = f.read()
            f.close()
            que.task_done()
    
    if __name__ == "__main__":
        basla = time()        
        # 5 thread olustur;
        for i in range(5):
            t = Thread(target = siteokuyan, args = (sira,))
            t.daemon = True
            t.start()
        
        # sitelerimizi siraya ekleyelim;
        for site in siteler:
            sira.put(site)
            
        # siranin bosalmasini bekle
        sira.join()
        print "%s saniye surdu" % (time() - basla)

Bu örnekte açıklanacak yeni şeyler var. İlk göze çarpan değişiklik, bu
örnekte Queue'yi içe aktarmamız. Bu Queue, elimizdeki işleri tutacak ve
iş istendikçe iş verecek. Bu Queue sınıfının sira isminde bir örneğini
oluşturduk.

`siteokuyan` isimli fonksiyon, argüman olarak bir `Queue` objesi alıyor.
`Queue` objesinden yeni bir iş almak için, bu objenin `get()` metodu
kullanılır. Bu metot, sıradaki işi döndürür. Ayrıca, işi bitirdikten
sonra, `task_done()` metodunu kullandığımıza da dikkat edin. Bu metot
elimizdeki işimizi bitirdiğimizi `Queue` objesine belirtiyor.

Daha sonra, bir for döngüsü ile 5 tane thread oluşturduk. Argüman olarak
da yukarıda oluşturmuş olduğumuz sira objesini verdiğimize dikkat edin.
Hepsine aynı Queue objesini verdik, çünkü hepsi aynı iş topluluğundan iş
alacaklar. Burada yeni olan tek şey, bu thread'lerin daemon özelliğini
True'ya ayarlamış olmamız. Eğer bunlar daemon olarak belirtilmezse,
Python bu thread'ler sonlanmadan programınızı kapatmaz. Ancak dikkat
ederseniz, thread olarak kullanacağımız fonksiyonda sonsuz bir while
döngüsü var. Yani, eğer bunları daemon yapmazsak, programımız
kapanmazdı.

Daha sonra, başka bir for döngüsü ile elimizdeki siteleri sira objesine
ekledik. Queue objesine iş eklemek için `put()` metodu kullanılır. Biz
burada siraya yazı (string objesi) ekledik, ancak, aşağı yukarı herşey
bu sıraya eklenebilir. `put()` metodu ile ne verirseniz, `get()` metodu
ile onu alırsınız.

Daha sonra, sira objesinin `join()` metoduyla elimizdeki işlerin
tükenmesini bekledik. Bu metot, `put()` ile eklenen her iş, `get()` ile
alınıp her bu iş için `task_done()` çağırılıncaya kadar programı
bloklar. Böylece, elimizdeki işler bitmeden programın sonlanmasını
önlemiş olacağız. Böylece bu örneğimizi de tamamlamış olduk.

Queue'ler ve thread'ler bu şekilde bir arada çok temiz bir şekilde
çalıştığı için, rahatlıkla birden fazla thread ve Queue ile aynı anda
çalışabiliriz. Yukarıdaki örnekte, sadece tek bir sıradan iş alıp, bu
siteleri okuduk. Aşağıdaki örnekte ise, iki tane sıra olacak. İlk
sıradan site isimleri alınıp, bu siteler okunacak. Daha sonra bu okunmuş
siteler ikinci bir sıraya konulacak. Başka bir thread grubu ise, okunmuş
web sayfalarını sırasıyla işleyip bunların linklerini okuyacaklar.
Linkleri okumak için [BeautifulSoup][] isimli modülü kullanacağım. Bu 3.
şahıs bir modül olduğundan sizde bulunmayabilir. Ayrıca, konumuzla
alakası olmadığından bu modülün detaylarına girmeyeceğim. Ancak, bunu
rahatlıkla internetten bulup kurabilirsiniz.

    :::python
    from threading import Thread
    from Queue import Queue
    from urllib import urlopen
    from time import time
    from BeautifulSoup import BeautifulSoup
    
    siteler = ("http://www.python.org",
               "http://istihza.com",
               "http://yasararabaci.tumblr.com",
               "http://metehan.us",
               "http://blog.tanshaydar.com",
               "http://fatihmertdogancan.wordpress.com",
               "http://ozgurerdogdu.blogspot.com/")
    
    ilk_sira = Queue()
    ikinci_sira = Queue()
    
    def siteokuyan():
        while True:
            site = ilk_sira.get()
            f = urlopen(site)
            icerik = f.read()
            f.close()
            ikinci_sira.put(icerik)
            ilk_sira.task_done()
            
    def linkokuyan():
        while True:
            icerik = ikinci_sira.get()
            soup = BeautifulSoup(icerik)
            for link in soup.findAll(['a']):
                print link
            ikinci_sira.task_done()
            
    if __name__ == "__main__":
        basla = time()
        for i in range(5):
            t = Thread(target = siteokuyan)
            t.daemon = True
            t.start()
        
        for site in siteler:
            ilk_sira.put(site)
            
        for i in range(5):
            t = Thread(target = linkokuyan)
            t.daemon = True
            t.start()
        
        ilk_sira.join()
        ikinci_sira.join()
        
        print "%f saniye" % (time() - basla)

Bu kodu çalıştırdığınızda, verdiğimiz sitelerdeki linklerin alt alta
sıralandığını ve son olarak bu işlemin ne kadar sürdüğünü göreceksiniz.
Burada farklı olarak yaptığımız en önemli şey, `siteokuyan()`
fonksiyonunda okuduğumuz siteleri, ikinci\_sira isimli Queue objesine
eklememiz. Bu sayede, bunları `link_okuyan()` isimli fonksiyon bu
sıradan alıp işleyecek. Diğer bir farklılık da, bu örnekte iki sırayı da
beklememiz. Önce ilk sıradaki bütün linklerin okunmasını bekliyoruz.
Böylece, ikinci sıraya eklenecek bütün sitelerin eklenmiş olduğundan
emin oluyoruz. Daha sonra ikinci sıradaki bütün işlerin tamamlanmasını
bekliyoruz. Böylece bu örneğimiz de tamamlanmış oluyor. Bu örnek biraz
çaba ile ufak bir arama motoru veya data-mining programı haline
getirilebilir.

Bu yazıyı bitirirken şunu da belirtlemekte fayda var ki, threading
modülü her soruna çözüm değil. Bazı durumlar için, ayrı işlem
(multiprocessing) kullanmak daha uygun olabilir. Programcının elindeki
problemi iyi değerlendirip, hangi aracın daha uygun olduğuna karar
verebilmesi gerekir.

  [stackless]: http://www.stackless.com/
    "Thread-based Python programming"
  [deadlock]: http://tr.wikipedia.org/wiki/Deadlock
    "Deadlock in threading"
  [race-condition]: http://en.wikipedia.org/wiki/Race_condition#Computing
    "Race-condution in computing"
  [BeautifulSoup]: http://www.crummy.com/software/BeautifulSoup/