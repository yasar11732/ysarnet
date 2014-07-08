<!--
.. date: 2013-10-06 10:15:05
.. slug: soru-cevap
.. title: Soru & Cevap
.. description: Zaman içinde Python ve programlama hakkında bana sorulan sorulara verdiğim cevapların bir derlemesi
-->

Siz de bana soru sormak istiyorsanız, sorularınızı yasar11732@gmail.com adresine mail olarak gönderebilirsiniz.

## [Asal Sayılar](#asal) {#asal}

> Hocam, ben Süha Türköz. Asal sayıların bulunmasında hangi
> algoritmayı kullandığınızı öğrenebilir miyim?

En çok tercih ettiğim algoritma [Eratosten kalburu][]. Ayrıca, [Asal sayı algorimaları] yazımı
da okuyabilirsin.

## [__asm yönergesi ve Python decorator](#asm-ve-decorator) {#asm-ve-decorator}

> Hocam merhabalar. Benim python üzerinde merak ettiğim bir kaç
> konu var. Öncelikle c++ dilindeki gibi `__asm` tarzı bir fonksiyon
> kullanabilir miyiz? Mümkünse ingilizce kaynak dahi olabilir. Son olarak
> ise pythonda sınıfların üstlerine @blabla tarzında girdiler var
> isimlerinide bilmiyorum, bunlar ne işe yarar? Teşekkür ederim..

Python derlenebilen bir dil olmadığı ve yorumlanan (interpreted) bir dil
olduğu için, Python kodların içerisinde assembly kullanamazsın. Eğer
assembly kodları kullanmak mecburiyetinde isen, bunları C fonksiyonu
olarak derleyip, [ctypes][] ile çağırabilirsin. İkinci sorun için ise,
[decoratörlerle ilgili yazı][]yı okuyabilirsin.

Kolay Gelsin.

## [Python'da sınıflar](#siniflar) {#siniflar}

> Sınıflar hakkında detaylı bilgi verirmisiniz?

Çok uzun bir konu olduğu ve birçok yerlerde uzunca anlatıldığı için,
link vermekle yetineceğim. Özellikle takıldığın bir yer varsa tekrar
sorabilirsin;

 * [belgeler.org](http://www.belgeler.org/uygulamalar/python-tutorial_siniflar.html)
 * [istihza.com](http://www.istihza.com/py2/nesne.html)

## [Oyun programcılığı için C++](#oyuncpp) {#oyuncpp}

[takipdelisi](http://takipdelisi.tumblr.com/){: rel="nofollow"}:
> Oyun programcılığına dair pek
> bilgisi olmayan biri olarak C++ programlama dilini örenmelimiyim sence?

Tam olarak ne yapmak istediğinle alakalı bence, ama boş vaktin varsa C++
öğren derim. Oyun programlama amaçlı düşünüyorsan, [lazyfoo sdl dersleri] c++ ve sdl
kullanarak oyun programlamayı bir güzel anlatmış. Ancak şunu da
belirteyim ki, sdl ve openGl ve directX için gereken eklentiler
Python’da mevcut. Yani bunları kullanmak için C++ öğrenmene gerek yok.

(Ekleme)

Bu arada, SDL eklentisinden kastım PyGame idi. PyGame ile ilgili bolca
kaynak internette mevcut. <del>Türkçe kaynak için [metehan.us][] adresinde
güzel anlatımlar vardı diye hatırlıyorum.</del>

## [Uzaktan eğitim](#uzaktan) {#uzaktan}

> hocam selam django ve python konusunda uzaktan eğitim almak
> istiyoruz bize nasıl yardımcıolabilirsiniz

Uzaktan eğitim konusunda daha önce bir tecrübem olmadı, bu yüzden pek
bir bilgim yok açıkcası. Google'da arayınca bir iki yer çıkıyor, ama ne
kadar güvenilir olurlar bilemiyorum.
İstersen [istihza forum](http://www.istihza.com/forum/index.php)da sormayı
deneyebilirsin, belki oradaki arkadaşlar biliyorlardır. Bir de [linux
programlama mail listesi](http://liste.linux.org.tr/listeler.php) var, oradan da yardım
almayı deneyebilirsin. Kusura bakma daha fazla yardımcı
olamayacağım.

## [BeautifulSoup ile tag içindeki tanımlamaları alma](#BeaufitulTag) {#BeautifulTag}

[eraygezer](http://eraygezer.tumblr.com/){: rel="nofollow"}:
> Merhabalar. Blogunuzda BeautifulSoup
> kullanımını göstermişsiniz ve çok güzel de bir ders olmuş. Benim sormak
> istediğim `<img src="kaynak"></img>` kodundaki kaynağı nasıl alabileceğim olacaktı.
> Şimdiden teşekkürler. :)

	:::python
	from BeautifulSoup import BeautifulSoup
	basit_html = """
	<html><head><title>Başlık buraya>/title></head>
	<body><p>Paragraf 1<img src="http://www.blogcdn.com/wow.joystiq.com/media/2008/01/maiev.jpg"></p><p class="hebele">Paragraf 2</p></body>
	</html>"""
	soup = BeautifulSoup(basit_html)
	imgs = soup("img") # img taglarının listesini al
	for img in imgs:
		print img["src"]

## [Django modelleri](#django-model) {#django-model}		

> hocam selam , üç modeli öncelikle formlar aracılı ile view ve
> oradan da temp e taşıyorum sıkıntım şu .... örneğin dersler modelimde
> ForeignKey ile bağlantılı hocalar var , öğrenciler modelim de de yine
> ForeignKey ile bağlı hoca ve dersler var , ben öğrenci kaydederken hoca
> seçtiğimde hocaya atanmış olan derslerin gelmesini istiyorum ama dersler
> tablomdaki tüm kayıtlar geliyor. bilmem anlatabildimmi bunu yapmamın
> imkanı varmı yoksa boşunamı kasıyorum

Sorunu bu şekilde anlamak biraz zor. İstersen örnek kodlarla birlikte
www.istihza.com/forum adresine sorabilirsin. Yarın okul başlıyor ama
vakit bulabilirsem ben de cevap vermeye çalışırım.

## [Dosyaları neden kapatıyoruz?](#dosya-neden-kapatmak) {#dosya-neden-kapatmak}

[eraygezer](http://eraygezer.tumblr.com/){: rel="nofollow"}:
> Merhaba hocam, iyi günler. Aslında
> sorumu bir örnekle açıklayacaktım ama soru sorma bölümünde alt satıra
> geçemediğim ve kodları yazınca link uyarısı aldığım için anlatarak
> açıklayacağım. Python'da bir dosyayı açarken open'i kullanıyoruz, daha
> sonra dosyayla işimiz bittiğinde close ile kapatıyoruz. Peki kapatmanın
> önemi nedir? a değişkeninin içeriğini mi sıfırlar, yoksa a'yı hafızadan
> tamamen kaldırır mı? Şimdiden teşekkürler.

Dosyayı kapatmanın amacı, işletim sistemine o dosyayla işinin bittiğini
bildirmek. İşletim sistemleri her işlemin (yazdığın program çalıştığı
anda bir işlemdir, aynı anda iki kopyası çalışırsa iki işlem olur vs.)
kullandığı kaynakların (ram, dosya, port vs.) kaydını tutar. İşletim
sistemi bu kaynakların nasıl kullanıldığını denetler.

Şu an tam olarak sayılarını bilmiyorum, ama işletim sistemlerinde her
işlemin aynı anda açık tutabileceği dosya sayısı için limitleri var.
Eğer açtığın dosyaları kapatmazsan, bu limite takılabilirsin.

İşletim sistemleri, iki farklı işlemin aynı dosyayı aynı anda yazma
modunda açmasına izin vermeyecektir. Dolayısıyla, yazma modunda açtığın
bir dosyayı sen kapatana kadar, diğer programlar o dosyaya yazamaz (ya
da o dosyayı silemez).

Programlama dillerinde kullandığın dosyalar genellikle yazılım
arabelleğine sahiptir. Bunların da çeşitli modları var. Mesela, eğer
kullandığın dosya yeni satıra geçildiğinde arabelleği boşaltan bir
moddaysa, sen dosyaya yeni satır yazana kadar işletim sisteminin senin o
dosyaya birşey yazmak istediğinden haberi yoktur. Python veya
kullandığın diğer dillerin kütüphaneleri yazdığın şeyleri biriktirip
bunları işletim sistemine tek seferde bildirir. Böylece performans
artışı sağlanır. Bir dosyayı kapatmak aynı zamanda ara bellekte kalan
her şeyin işletim sistemine gönderilmesine neden olur. Buna *flush* da
denir. Bunu Python’da dosya objelerinin `flush()` metoduyla da
yapabilirsin. Ancak işletim sistemi gönderdiğin şeyi hemen dosyaya
yazacak diye birşey de yok. Ne zaman uygun görürse o zaman yazar. Eğer
işletim sistemini hemen yazmaya zorlamak istiyorsan, [fsync fonksiyonu] işini görebilir.

Son olarak da, Python kullanırken dosyalarını `close()` ile kapatma.
Python 2.5’den beri olan `with` yapısını kullan. Örneğin;

	:::python
    with open("a","w") as dosya1, open("b","r") as dosya2:
		dosya1.write(dosya2.read())

Eğer dosyayı açtığın yer ile, `close()` metodunu çağırdığın yer arasında
bir hata olursa, `close()` satırına ulaşamayabilir. Bu yüzden dosya açık
kalır. `with` yapısı yer zaman dosyanın kapandığından emin oluyor.

Bu arada, modern işletim sistemleri bir işlem sonlandığında onun açık
kalan dosyalarını otomatik olarak kapatır. Galiba eski işletim
sistemleri bunu yapmayabiliyormuş.

`a` değişkeniyle ilgili pek bir değişiklik olmaz. Sadece artık o dosya
objesi üzerinde daha fazla işlem yapamazsın. Eğer dosya objesini tamamen
hafızan silmek istiyorsan, `a` değişkenine başka bir değer
atayabilirsin. *Garbage collection* denen şey, o dosyaya hiç bir
referans kalmadığı için onu hafızadan silecektir. Ya da `del a` diyerek
de o değişkeni silebilirsin.

**ekleme:**

Bu arada, `open()` fonksiyonuna tekrar bir göz attım. `open()`fonksiyonu
arabellek modunu belirlemene izin veriyor. Bunun için üçüncü argümanı
kullanıyorsun.

<pre>
open("a.txt","w",0) # arabellek kullanma (sadece işlemin kendi arabelleğini etkiler, işletim sisteminin arabelleğini etkilemez)
open("a.txt","w",1) # yeni satır arabellek modu
open("a.txt","w",4096) # boyutu belirtilen değer kadar olan bir arabellek kullan. Her 4096 bayt yazıldığında işletim sistemine yazım için istek gidecek
</pre>

## [GNU Lisansı ve versiyonlama](#lisans-versiyon) {#lisans-versiyon}

[eraygezer](http://eraygezer.tumblr.com/){: rel="nofollow"}

> Merhabalar hocam. Benim sorum sürümler
> ve GNU GPL lisansı olacaktı. İlk önce sürümlerden başlayacağım. Sürüm
> dediğimiz şey, programlarda nasıl belirlenir? İkinci olarak da GNU GPL
> ile ilgili bir şeyler soracağım. Benim gördüğüm kadarıyla GNU GPL v2 ve
> v3 var, bunların arasındaki fark nedir? Başka bir şey ise şu ki bir
> forumda GNU'nun sitesindeki bir ifadeyi programın başına eklersek onu
> lisanslamış olduğumuz söyleniyor, bu ne kadar doğrudur? Şimdiden çok
> teşekkürler.

Sürümleme aslında programı yazanın keyfine kalmış ama genel olarak kabul
edilen standartlar da var. Sürümler genelde major.minor.relase.build
şeklinde olur. Aynı major'a sahip sürümlerin kendi arasında uyumlu
olması beklenir. Örneğin, Python 2.x için yazdığın programlar 2.7, 2.6,
2.5 gibi aynı major'a sahip Python sürümlerinde pek fazla değişime
ihtiyaç bırakmadan çalışabilir. Major numarası çok belirgin
değişiklikler yapılacağında artırılır. Ticari programlarda, aynı major'a
yapılan güncellemeleri ücretsiz olarak alabilmen gerekir. Minor numarsı
ise, eski özellikleri bozmayan yeni bir özellik eklendiğinde ve hata
düzeltmeleri yapıldığında artırılır. Örneğin, 2.5 sürümünde Python'a
eklenen özellikler eklendi. Ancak, Python 2.4 için yazılan kodlar halen
Python 2.5'de çalıştırılabilir. Release ise ufak bir hata düzeltmesi,
minik değişikler yapıldığında artırılır. Minor artırıldığında, release
sıfırlanır. Build numarası ise yazılım her derlendiğinde artırılır ve
hiç sıfırlanmaz. Hata raporu yazarken belirtilmesi iş görür.

GPL versiyonları arasında çok fazla bir fark yok. Birkaç birşey eklendi,
bazı konular netleştirildi vs.

Evet, o ifadeyi ekleyerek programı lisanslamış oluyoruz, ancak bunun
Türkiye'de hukuki bir geçerliliği var mı bilmiyorum.

## [Hangi sürümle başlamalı?](#hangi-surum) {#hangi-surum}

> Bakıyorum da hep tartışılmış ve konuşulmuş. Sizin fikrinizi
> merak ettim. Bu gün itibarıyla sizce Python 2.X mi Python 3.X'mi
> öğrenilmelidir. Tkinker, pyqt, django gibi yapılar hangisini
> destekliyor. Teşekkürler

Kısa cevap: 2.x

Uzun cevap;

[Python 3 Wall of Superpowers][] en çok kullanılan paketlerden Python 3
destekli olanları yeşil ile gösteriyor. Durumlar eskiye nazaran biraz
daha iyi görünüyor. 200 paketten 128 tanesi Python 3'e taşınmış
vaziyette. Saydığın paketlerin hepsi de Python 3'de çalışıyor. Ancak ben
yine de Python 2'nin öğrenilmesini tavsiye ederim.

Python 3 öğrendiğinde, kullanmak istediğin paketin Python 2 versiyonu
olmaması ihtimali var, diğer yandan, sadece Python 3 destekleyip, Python
2 versiyonu olmayan paket hatırlamıyorum.

Eğer yazdığın kodu bir server'da çalıştıracaksan, o server'in sadece
Python 2'yi çalıştırması bir hayli olası. Örneğin, bildiğim kadarıyla
google app engine Python 2.7 versiyonunu kullanıyor.

Bildiğim kadarıyla çoğu linux dağıtımında kurulu gelen Python versiyonu
2. Ekstra birşey yapmadan direk kullanmaya başlayabilirsin. Python 3
kullanmak istediğin zaman ise, hem Python 2 hem de Python 3 kurulu
olacaktır bilgisayarında, çünkü bazı programlar Python 2'yi bağımlılık
olarak yükler diye tahmin ediyorum. Böyle olduğu zaman iki farklı sürüm
yüklü olduğu için, sinek küçüktür ama mide bulandırır tarzında
problemler çıkıyor. Yazdığın kodu yanlış Python ile çalıştırıyorsun vs.

İnternette bir süredir Python 3 için yazılan çizilen şeyler var, ancak
Python 2 için yazılan şeyler yılların birikimi. Bir problemin olduğunda,
bulduğun sonuç büyük ihtimalle Python 2'ye yönelik olacaktır. Ders
anlatımlarının, örneklerin, makalelerin çoğu hala Python 2'ye yönelik.

Vakti geldiğinde, Python 3'e geçmen hiçbir zorluk teşkil etmiyor. Bir
iki yeni özelliğini öğrenirsin, eski kodlarından taşımak istediklerini
2to3 aracıyla Python 3'e taşırsın, bitti gitti zaten.

Python 2 öğrenin derim, sadece unicode'larınıza biraz dikkat edin :)

**Not:** Vakit darlığından dolayı hızlıca yazdım, okuyup düzeltme yapma
şansım olmadı. Eğer dil veya bilgi hataları varsa mazur görün lütfen.

  [Python 3 Wall of Superpowers]: https://python3wos.appspot.com/
  [fsync fonksiyonu]: http://docs.python.org/2/library/os.html#os.fsync
    "os.fsync"
  [lazyfoo sdl dersleri]: http://www.lazyfoo.net/SDL_tutorials
  [metehan.us]: http://www.metehan.us/tag/pygame-2
  [ctypes]: http://docs.python.org/library/ctypes.html
  [decoratörlerle ilgili yazı]: /python/decorator.html
  [Eratosten kalburu]: http://tr.wikipedia.org/wiki/Eratosten_kalburu
  [Asal sayı algorimaları]: /python/asal-yolculuk.html