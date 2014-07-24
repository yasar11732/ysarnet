<!-- 
.. description: Python'a yeni başlayanlar için en merak edilen konulardan biri olan Python'un kullanım alanlarını, Python'un ne işe yaradığını anlattım.
.. date: 2013/10/08 14:44:59
.. title: Python Kullanım Alanları
.. slug: kullanim-alanlari
-->

Bu yazı Python'a yeni başlamış veya başlamayı düşünen kişilere yönelik olacak. Eğer Python'a başlamayı düşünüyorsanız
ancak sizin için doğru bir dil olduğun emin değilseniz, bu yazı sizin için. 

Python çok çeşitli alanlarda kullanılan oldukça güçlü, dinamik bir programlama dilidir. Python'u farklı kılan
özelliklerden biraz bahsetmek gerekirse:

 * Net ve kolay okunabilen yazımı
 * Çalışma esnasında objelerin özelliklerini inceleyebilme imkanı
 * Kolay anlaşılır nesne tabanlı programlama özellikleri
 * Güçlü ifade yeteneği
 * Modüler yapısı
 * Exception tabanlı hata yönetimi
 * Çok yüksek seviye dinamik veri yapıları
 * **Çok geniş** kütüphaneleri
 * C veya C++ ile ek modüller yazmanın kolaylığı
 * [Diğer programlara kodlama arayüzü olarak dahil edilebiliyor olması](http://docs.python.org/2/extending/embedding.html) <!-- TEASER_END -->
 
Bu özelliklerinin yanında, öğrenmesinin bir hayli kolay olmasını da ekleyebiliriz. Bu sebeple bazı
üniversitelerde programlamaya giriş dersinde kullanıldığını duymuştum. Ancak şu anda bunu teyit edemiyorum.

Python öğrenmenin kolaylığını göstermek için, Python ve C++'da birer *Hello World* örneğine bakalım. Önce
C++:

    :::++
	#include <iostream>
	using namespace std;
	 
	int main()
	{
		  cout << "Merhaba Dünya";
		  return 0;
	}
	
5 satır kod kullanarak ekrana *Merhaba Dünya* yazdık. Şimdi Python örneğine bakalım:

	:::python
	print("Merhaba Dünya")
	
Çok daha basit değil mi? Artık Python öğrenmeye niyetlendiyseniz, Python ne işe yarar sorusunun cevaplarını aramaya
başlayabiliriz.

## Rest API'si oluşturma

Bu yazının konusu [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) olmadığından, bunun bir çeşit mimari olduğunu söylemekle yetineceğim. Günümüzde genellikle
web servisleri oluşturmak için kullan bir standard haline gelmiş durumda.  Örneğin, [twitter APIsi](https://dev.twitter.com/docs/api) bir RESTful API. 

Python bir rest API'si oluşturmak için çok sık kullanılan bir dil. [Flask](http://flask.pocoo.org/),
[eve](http://python-eve.org/) veya [Django](http://django-rest-framework.org/) gibi frameworkler sayesinde
çok kısa bir zamanda web servisinizi kullanıma hazır hale getirebilirsiniz.

## Machine Learning

Machine Learning, bir veri üzerinden çeşitli algoritmalar yardımıyla birşeyler öğrenme uğraşına verilen genel bir ad. Bunun içine,
sınıflandırma (spam tanıma, resim tanıma), regresyon (hisse fiyatları), bölümleme (müşteri grupları oluşturma),
gibi çeşitli alanlar giriyor. Machine Learning neredeyse her sektörde uygulama alanı bulabilecek bir disiplin.
Machine Learning alanına merak salan kişiler, [Hilary Mason](http://www.hilarymason.com/) ve
[Andrew Ng](http://cs.stanford.edu/people/ang/) kişilerinin takipçisi olabilirler.

Python için yazılmış [scikit-learn](http://scikit-learn.org/stable/) adında çok kapsamlı ve güçlü
bir machine learning kütüphanesi var. Machine Learning ile alakalı aklınıza (ya da benim aklıma)
gelebilecek her türlü algoritma tanımlanmış. Web sitelerinde [machine learning örnekleri](http://scikit-learn.org/stable/auto_examples/index.html)
de bulunmakta.

Bunun yanında bir de [PyBrain](http://pybrain.org/) var. Son kontrol ettiğimde (muhtemelen 1-2 sene önce)
PyBrain daha çok Neural Network algoritmalarına odaklı bir kütüphane idi. Unsupervised Learning alanında
gerekli olabilecek çeşitli algoritmalar tanımlanmış durumda.

## Web Uygulamaları

Web uygulaması (web sitesi de olabilir) geliştirme konusunda Python çokça tercih edilen bir dil. Python ile web geliştiriciliği
yapmış herkes [Django](https://www.djangoproject.com/)'yu duymuş, hatta kullanmıştır.

Django framework'ü içinde ihtiyaç duyabileceğiniz neredeyse herşey dahil edilmiş. Ancak, web uygulamalarınızı geliştirmek için Django'ya bağlı
kalmak zorunda değilsiniz. [Basit cgi programları](https://wiki.python.org/moin/CgiScripts) yazmaktan,
tüm bir [server yazmaya](https://wiki.python.org/moin/WebServers) kadar çok çeşitli şekillerde
Python'u kullanabilirsiniz. Python ile REST APIsi yazabileceğinizi zaten daha önce belirtmiştim.

## Örümcek türü yazılımlar

Python, web'i taramak ve veri toplamak için de çok uygun bir dil. Bu konuyu biraz araştırınca, karşıma
[Scrapy](http://scrapy.org/) çıkıyor. Dökümanlarından anladığım kadarıyla, Scrapy her şeyi içinde, birçok özelliği
hazır bir web tarama ve veri ayıklama kütüphanesi.

Her zaman olduğu gibi, örümcek türü yazılımlar yazmak için belirli bir kütüphaneye bağlı kalmak zorunda
değilsiniz. Örneğin, ben daha önce bu tarz şeyler yapmak istediğimde (basit ihtiyaçlarım doğrultusunda)
[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) ve [requests](http://docs.python-requests.org/en/latest/)
kütüphanelerini kullarak işimi halletmiştim.

Ayrıca, bu örümcek türü yazımlarınızı, biraz önce bahsettiğim Machine Learning kütüphaneleriyle yan yana
koyup, çok farklı uygulamalar geliştirebilirsiniz. Örneğin, google dediğiniz şey de altı üstü bir örümcek ve
bir Machine Learning uygulaması (ayrıca, devasa bir index) den oluşuyor.

## Bilimsel

Python bilimsel alanda da Matlab'a kafa tutabilecek (belki geçebilecek?) zengin fonksiyonlar sunuyor.

Python'u bilimsel alanda kullanmak istediğinizde, çeşitli seçenekleriniz mevcut. Hepsi içinde dağıtımlar
indirip kurabilirsiniz. [SciPy indirme sayfası](http://www.scipy.org/install.html) size temel bilimsel
programların içinde bulunduğu çeşitli Python dağıtımlarının bir listesini sunuyor. Buna ek olarak, ihtiyaç
duyduğunuz kütüphaneleri ayrı ayrı yükleme imkanınız da mevcut.

SciPy setinin içinde gelen [IPython](http://ipython.org/), Matlab tarzında interaktif bir şekilde Python ile çalışmanıza olanak
sağlıyor. [Matplotlib](http://matplotlib.org/) ise, verilerinizi görselleştirme imkanı sağlıyor. SciPy setinin içinde, türev, integral,
optimizasyon, lineer cebir, istatistik gibi alanlarda ihtiyaç duyabileceğiniz veri tipleri ve işlevsellik sağlanıyor.

Ben de ara sıra matplotlib kullanıyorum. [Arch Linux Paket Grafiği](/yazilim-dunyasi/arch-linux-paket-grafigi.html) ve [Arch Linux Paket Grafiği 2](http://ysar.net/yazilim-dunyasi/arch-linux-paket-grafigi-2.html)
yazılarımda, matplotlib kullanımına örnek kod bulabilirsiniz.

## Veri Analizi

Veri analizi konusu aslında az çok Machine Learning ve Bilimsel başlıkları altında anlatılanlarla
çakışan bir alan, ancak ayrıca belirtmek istedim. [Pandas](http://pandas.pydata.org/) kütüphanesi,
yüksek performanslı kullanımı kolay veri yapıları ve veri analizi özellikleri sunuyor. Böylece,
[R](http://www.r-project.org/) veya [stata](http://www.stata.com/) gibi istatistik programlarına
ihtiyaç kalmadan, veri analizi ve modelleme yapabilirsiniz. IPython, [statsmodels](http://statsmodels.sf.net/),
ve scikit-learn gibi araçlar ve kütüphanelerle bir arada kullanıldığında, performans ve üretkenlik açısında
hayli güçlü bir veri analizi ortamı elde edebilirsiniz.

Ben daha önce Pandas'ı eğlencelik bir projemde kullanmıştım. Şu anda kodlar eski laptop'umda olduğu için örnek
gösteremiyorum. Ancak, şöyle anlatayım; önce her tıkladığımda bir dosyaya tıklama zamanımı kaydeden bir programcık
yazıp, bunu bilgisayar açıldığında otomatik olarak çalışması için ayarladım. Daha sonra elde ettiğim verileri Pandas'da
her dakikada kaç kere tıklandığını gösterecek şekilde grupladım. Sonra bunlardan, bir dakika içinde tıklama sayımın olasılık
dağılımı fonksiyonunu çıkarmıştım. Ortalama değeri 5 olan bir [poisson dağılımı](http://tr.wikipedia.org/wiki/Poisson_da%C4%9F%C4%B1l%C4%B1m%C4%B1) gibi duruyordu.

## Ağ ve Soket programcılığı

Bu da biraz Web uygulamalarıyla çakışan bir konu, ancak biraz daha geniş bir alan. [Twisted](http://twistedmatrix.com/trac/)
bu yazıda illa ki bahsedilmesi gereken bir kütüphane. Bununla, Web sunucularına ek olarak, internet üzerinden
yapılabilecek çok çeşitli uygulamalar geliştirilebilir. Artık mail sunucusu, mail alıcısı, internet üzerinden
oynanan oyunlar, ne yazacaksanız elinizin altında Twisted gibi bir kütüphane var.

Açıkçası ben bu kütüphaneyi hiç kullanmadım, çünkü bu tarz uygulamalar geliştirmeye ihtiyaç duymadım. Ancak,
sırf bunun üzerine yazılmış [kitap](http://www.amazon.com/gp/product/1449326110/)
bulunduğu ve çeşitli yerlerde çok adı geçtiği için, yeterince kapsamlı ve güçlü bir kütüphane olduğunu düşünüyorum.
Eğer aranızda Twisted deneyimi olan varsa, paylaşırsa çok hoş olur.

## Sistem Yönetimi

Bu başlık daha çok linux ile alakalı. Linux sistemlerinde, geleneksel olarak sistem yönetim kodları daha çok kabuk programları
aracılığıyla yazılırdı. Ancak şu anda, çoğu (her?) linux sisteminde Python kurulu olarak geliyor. Ve Python,
kabuk programlarıyla yapabileceğinizden fazlasını sunduğu için, sistem yönetim programcıkları yazmak için
gayet uygun bir dil. [os](http://docs.python.org/2/library/os.html) modülüne bakarsanız, ihtiyaç duyabileceğiniz
herşeyin Python'a dahil olarak geldiğini görebilirsiniz.

Hatırlar mısınız, bir zamanlar [Pardus](https://www.pardus.org.tr/){: rel="nofollow"} vardı. Aslında halen
var ama, eski tadı kalmadı. Neyse, pardus'da bir çok sistem aracı Python ile yazılmıştı. Hatta bu biraz genç
ve meraklı arkadaşlar üzerinde kafa karışıklığı yaratmış, Python ile işletim sistemi yazıldığı yanılgısı
oluşturmuştu. Bu konuya biraz sonra geleceğiz.

## Diğer

Python'un kullanım alanı çok geniş olduğu için, hepsini tek tek buradan saymam mümkün değil. Benim
görüşüme göre, en önemli gördüğüm alanlardan bahsettim. Bu saydıklarımın dışında, veritabanı erişimi, oyun geliştirme ve
masaüstü programları geliştirme için de Python kullanılıyor. Ancak, son zamanlardaki görüşüme göre, Python
oyun geliştirme ve masaüstü uygulaması (arayüz uygulamarını kastediyorum) geliştirmek için uygun bir değil,
ama bu konunun yeri olmadığı için daha sonraya bırakıyorum.

Ayrıca, Python'un günlük kullanım için de çok uygun bir dil olduğunu söyleyebilirim.  Belki benim günlük
iş anlayışım sizinkinden biraz farklı olabilir, ancak, şunu belirteyim ki, hızlıca birşey yazıp, çalıştırıp,
sonuç almak istediğiniz durumlarda Python sizin diliniz.

## Python ile Ne Yapamazsınız

Python her ne kadar kullanım alanı çok geniş bir dil olsa bile, Python ile yapamayacağınız şeyler de. Bunun
en önemli nedeni, Python'un makine kodlarına derlenen bir dil değil, yorumlanan bir dil olması.

Makine kodlarına derlenen C gibi diller, çalıştırılmadan önce derlenip makine kodlarına dönüştürülmesi gerekir.
Bu derlenme aşaması, yazdığınız kodların, kullandığınız işlemcinin anlayacağı dile dönüştürülmesi demek. Farklı
işlemcilerin anladığı, farklı kod setleri olabilir. C derleyiciniz bu dönüşümü kendisi hallediyor.

Ancak Python kodları makina koduna derlenmez. Eğer bazı yerlerde, Python kodunun derlenmesine ilişkin şeyler
duyarsanız, unutmayın ki bu derleme makine diline değil, Python'un anlayacağı bir dile derlenmesi anlamına
gelir.

Bu sebeple, Python kodlarını çalıştırmak için, programlarınızın çalışacağı ortamda bir Python yorumlayıcısı
olması şarttır. Muhtemelen bilirsiniz, java'da da durum böyledir. Java kodlarının çalışması için istenen
platformda bir *java virtual machine* kurulu olmalıdır.

Bu sebeple, Python ile bir **işletim sistemi yapamazsınız**. Python ile işletim sistemi yapıldığı algısı,
zannımca tam olarak bir işletim sisteminin ne olduğu konusundaki bilgisizlikten veya bu konudaki yanlış 
algılamadan kaynaklanıyor. Öncelikle şunu belirteyim ki, işletim sistemi kullanıcının gözle görebileceği
birşey değildir. İşletim sistemi Python yorumlayıcısını çalıştıran şeydir. Yani yazdığınız Python kodlarının
Python yorumlayıcısı tarafından yorumlanması için, önce Python yorumlayıcısının bir işletim sistemi
tarafından çalıştırılması gerekir.

İşletim sistemleri, bilgisayar açıldığında ilk çalıştırılan ve makine kodlarından oluşan programlardır.
Bu programlar, kullanıcı seviyesindeki programların bilgisayarın kaynaklarını nasıl kullandığını denetler,
ve böylece bilgisayarın sorunsuz bir şekilde çalışmasını sağlar.

Pardus'da Python ile yazılan şey ise, çeşitli sistem araçlarıdır. Bunlar mesela, paket yönetim sistemi,
konfigürasyon sistemi gibi çeşitli şeyler olabilir. Bu tarz araçlar, bilgisayarın kullanıcı tarafından
kullanılması için gereken ortamı oluştururlar, ancak bunlar işletim sistemi değildir.

Python'un kısıtlayıcı olabileceği durumlardan bir diğeri de, sistem kullanımı yoğun olan programlar. Ancak,
bunun gibi durumlarda, yazılacak kodların optimize edilmesi gereken kısımları, C ile yazılıp eklenti modülü
olarak derleniyor. Böylece, performans sorununu da halledebiliyorsunuz. Ayrıca, [Cython](http://cython.org/) C eklentisi
yazmayı, Python kodu yazmak kadar kolay bir hale getiriyor.

## Sonuç olarak

Python çok çeşitli alanlar ve sektörlerde kullanılabilecek, öğrenmesi ve kullanması kolay, her iş için
bir kütüphanesi bulunan güçlü bir dildir. Eğer siz de aktif bir şekilde Python kullanıyorsanız, hangi
alanda Python kullandığınızı yorumlarla iletebilirsiniz.

*[REST]: Representational State Transfer
*[API]: Application Programming Interface