<!--
.. date: 2014/07/21 03:56
.. slug: python-calisma-rehberi
.. title: Python Çalışma Rehberi
.. description: Yeni başlayanlar için, Python'a nasıl çalışmalıyım sorusuna bir cevap
-->
Bir konuyu öğrenmeye başlamanın kendine göre zorlukları vardır. Bunların en başında, çalışma planına karar verilmesi gelir. Özellikle,
internettin kaynak kaynadığı şu zamanlarda, asıl sıkıntı kaynak bulmakdan öte, hangi kaynakların hangi sırada kullanılması gerektiği
sorusudur. Eğer siz de benim gibi, bol bol internetten birşeyler öğrenmeye çalışan bir insansanız, muhtemelen bir öğretmenin eksikliğini
hissetmişsinizdir. Onca materyalin içerisinde size rehberlik edip yol gösterecek kimse yoktur ve belki de boğulduğunuzu hissedersiniz.

Bu yazıda, internetten Python öğrenmeye çalışan, ancak, kendine çalışma planı hazırlamakta zorluk çeken kimselere, kendi deneyimlerimden
ve şu ana kadar öğrenmeye muktedir olduğum bilgilerden yola çıkarara, kısa bir çalışma rehberi hazırlamak istiyorum. Bununla birlikte,
şunun da farkındayım ki, herkesin öğrenme üslubu ve ihtiyaçları farklılık gösterecektir. Bu yazıyı yazarken, bu tarz farklılıkları
da akılda bulundurmaya çalışacağım.

Görebildiğim kadarıyla, Python öğrenmeye başlayanların kafalarına takılan ilk soru, hangi Python sürümünü öğrenmeleri gerektiğidir. Bu soruyla
ilgili en büyük problem, sorunun cevabının zaman içinde çok hızlı bir şekilde değişebilecek olması. Buna daha önce farklı tarih ve muhitlerde
verdiğim cevaplar bile, birbirini tutmuyor. Bu sebeple, bu soruya bir cevap vermek yerine, konuya nasıl yaklaşılması gerektiğini, kendi bakış
açıma göre, yazacağım.

Bence bu değerlendirmeyi yaparken kullanılması gereken ilk mikyas, kullandığınız işletim sistemi ve araçlar olacaktır. Eğer linux kullanıyorsanız,
cidden büyük bir ihtimalle, bilgisayarınızda belli bir Python sürümü yüklü olacaktır. Oradan başlayın derim, çünkü, bilgisayardaki Python sürümünü
değiştirmek, muhtemelen o anda uğraşmak istemeyeceğiniz türlü sıkıntıları da beraberinde getirecektir. Sürümler arasındaki farklılıklar, sıfırdan
Python öğrenirken, o kadar da dikkat çekici olmadığından, bu aşamada sürüm değiştirmek uğraşına girmeye değmeyeceğini düşünüyorum. Bu kriter aynı
şekilde, okulda ders olarak veya dersin bir parçası olarak Python öğrenenler için de geçerli bence. Hocanız hangi sürümü kullanıyorsa, siz de önce
onu öğrenin.

Ancak bilgisayarınızda, hazır bir Python sürümü yoksa, Python öğrenmekteki teşvikiniz önemli bir kriter olabilir. Eğer elinizde belli bir kod
tabanı varsa, ve bu kod tabanı size emanet edildiği için Python öğreniyor iseniz, haliyle o sürümle başlamak işinize gelecektir.

Eğer yukarıdaki şartlar size uymuyorsa, Python 3 ile başlamanızı tavsiye ederim. Önceleri, Python 2'yi tavsiye ediyordum. Ancak, Python 3
artık yeterince olgunlaştı ve görebildiğim kadarıyla, 3'e geçiş süreci ivme kazanmış durumda. Ayrıca, Python 3 ile başlamış olmanız, Python 2
ile ilgili herşeyi geride bırakmak anlamına gelmiyor. Aşağıda sunacağım çalışma planında, iki sürümü birden kullanmaya başlamanızın uygun
olduğu zamandan bahsedeceğim.

Genel Konseptler
----------------
Bu kısım, genel olarak Python kaynaklarında bulamadığım bir kısım. Özellikle benim gibi tümden gelim yöntemiyle çalışmayı sevenler için,
ihtiyaç duyulan bir konu başlığı olduğu düşünüyorum. Bu kısımda, Python dilinin temellerini oluşturan kavramlardan bahsedeceğim.

### Python makine diline derlenmez

Python ile yazmış olduğunuz programlar, Python sanal makinesi tarafından yorumlanır. Eğer bunun ne demek olduğu konusunda pek bir fikriniz
yoksa, şunu bilmeniz yeterli, Python programlarını çalıştırmak için, bir Python yorumlayıcısına ihtiyacınız olacaktır. Her ne kadar çeşitli
Python yorumlayıcıları olsa da, özellikle aksi belirtilmediği takdirde, Python deyince akla, resmi Python yorumlayıcısı gelir.

Bu aynı zamanda, makine seviyesinde işlemler yapmak isteyenler için, Python'un uygun bir dil olmadığı anlamına gelir.

Python'un makine diline derlenmiyor oluşu, şu anda girmeyeceğim teknik detaylar nedeniyle, performansına da etki eder. Bu performans farkı,
çoğu zaman önemsenmeyecek derecede olsa da, önemli olduğu noktalarda, yeri geldiğince bahsedilebilir.

Bu yazının konusu olmadığı için, alternatif Python derleyecilerine girmeyeceğim. Başka bir zaman, ondan da bahsedilebilir.

### Python değişkenleri ve Mutable kavramı

Bu kısım, özellikle programlamaya yeni başlayanlar için fazla teknik gelebilir. Eğer bu konsepti anlamazsanız, üzerinde fazla durmanıza gerek yok,
daha sonra tekrar dönebilirsiniz.

Python'da, özellikle Python'la birlikte gelen kütüphanelerde, iki çeşit veri türü vardır. Bunlar, yerinde değiştirilebilen ve yerinde değiştirilemeyen
olarak ikiye ayrılır. Eğer buna dikkat etmezseniz, çok can sıkıcı hatalarla karşılaşabilirsiniz. Bunları, değişkenlerle birlikte anlatacağım için, biraz
da değişkenlere değineyim.

Python'daki değişkenler, hafızadaki bir objeye işaret eder. C bilenler için baştan belirteyim, C'deki pointerlardan farklıdır. Bunu bir örnekle anlatayım.

	:::python
	a = [1, 2, 3]
	b = a
	a.append(4)
	print("a =", a)
	print("b =", b)
	
Program çıktısı;

<pre>
	a = [1, 2, 3, 4]
	b = [1, 2, 3, 4]
</pre>

`a = [1, 2, 3]`, içinde 3 eleman olan bir liste oluştur ve `a` ismi de bu objeden bahsetsin demek. Şuna dikkat edin, `a` objenin bir ismidir. Bir
objenin, birden fazla ismi olabilir. İstediğiniz ismini kullanarak, obje üzerinde işlem yapabilirsiniz.

`b = a`, `b` ismi, `a` ile aynı objeden bahsetsin demek.

`a.append(4)`, ismi `a` olan listenin sonuna, `4` ekle demek.

Daha sonra, ekrana `a` ve `b` değerlerini bastırdığımızda, aynı listeyi görüyoruz, çünkü a ve b, aynı objenin iki farklı ismi. Şimdi de faklı bir örneğe bakalım;

	:::python
	a = "yasar"
	b = a
	a += " arabaci"
	print(a)
	print(b)
	
Bu programın çıktısına bakarsak, `a` ekrana `yasar arabaci`, b ise `yasar` olarak basılacak. Dikkat ederseniz, bir önceki örneğin tersine, `a` ve `b`
değerleri birbirinden farklı. Bunun nedeni, Python'da karakter dizilerinin `Mutable` olmaması, yani kendi üzerinde değişiklik yapılamaması. Yukarıdaki
örnekte, şu oluyor;

<pre>
a ---> "yasar" (a ismi, hafızadaki bu karakter dizisinden bahsetsin)
b ------^      (b ismi de hafızadaki bu karakter dizisinden bahsetsin)
a -----> "yasar arabaci" (a ismi, hafızadaki bu yeni karakter dizisinden bahsetsin)
</pre>

Yani, Python karakter dizisini yerinde değiştiremediği için, `a += " arabaci"` satırında, hafızada ayrı bir obje oluşturdu, ve a ismi artık bu
yeni isimden bahsediyor. `b` üzerinde ise, herhangi bir değişlik yapılmadığı için, hala biraz önceki `"yasar"` karakter dizisinde bahsediyor.

### Python'da herşey bir objedir

Obje dediğimiz zaman, akla belli nitelikler ve fonksiyonlar kümesi aklınıza gelsin. Python'da herşey bir objedir dediğimizde ise,
Python'da herşeyin belli nitelikleri ve fonksiyonları vardır demek olur. Örneğin, başka bir dilde `a = 5` dediğiniz zaman, hafızanın
bir yerinde, 5 değeri tutuluyor demektir. Bu değerin herhangi bir niteliği veya fonksiyonu yoktur. `a` sadece bir sayı değerini ifade
eder. Python'da ise, `a = 5` dediğimizde, bir sayı objesi oluştururuz. Python'da, int objelerinin `bit_length` isimli bir fonksiyonu var
(teknik olarak buna fonksiyon yerine method demek gerekir, ancak, şu anda kafa karıştırmaya gerek yok.) Örneğin, `a.bit_length()` ile,
bu int objesini, binary olarak ifade etmek için, kaç bit gerekir öğrenebiliriz.

Python'da, normalde obje olmasını beklemeseniz bile, herşey bir objedir, fonksiyonlar, sınıflar, hatta modüller bile bir objedir.

Objeler Python'da birinci sınıf vatandaş olduğu için, her objeyi çalışma anında oluşturabilir, silebilir, fonksiyona argüman
olarak verebilir veya fonksiyondan döndürebilirsiniz. Örneğin, Python'da argüman olarak bir modül alıp sınıf döndüren bir fonksiyon
gayet rahatlıkla yazılabilir. Başka dillere alıştıysanız, bu biraz manyakça gelebilir, ama alışkanlık yapar.

### Yardım Alma

Python'da `help(obje)` fonksiyonunu, herhangi bir obje ile çağırdığınızda, o obje hakkında yardım alabilirsiniz.

Bir diğer yöntem de `pydoc` modülünü kullanmak. `pydoc` modülünü çalıştırma yöntemi, sürümler arası farklılık gösterebilir. Ben,
3.4'de `python -m pydoc -b` ile, 2.7'de ise, `python -m pydoc -p 9090` ile server'ı çalıştırıp, browser'da *http://localhost:9090*
adresine giderek pydoc'a ulaşabiliyorum.

Yalnız, Bunlardan faydalanmak için, biraz İngilizce bilgisine ihtiyaç duyacaksınız.

Konu Çalışma
------------

Eğer yukarıda bahsettiğim noktaları anladıysanız, Python'un çalışma yapısını genel olarak anladınız demektir. Bundan sonra,
konu çalışarak, Python bilginizi geliştirmeye ihtiyaç duyacaksınız. Bunun için, özellikle Türkçe dökümantasyon kullanmak
isteyenler için, [İstihza](http://belgeler.istihza.com) belgelerinden faydalanın derim.

Eğer İstihza belgelerini takip edecekseniz, öncelikle temel bilgiler kısmına göz atın derim. Py2.7 sürümünde, birinci
kısım, Py3.3 sürümünde ise, ilk 12 kısım, temel bilgilerden bahsediyor. Bence bu kısmı satır satır okumaya gerek yok,
alt başlıklara göz gezdirin ve ihtiyaç duyacağınız kısımları okuyun.

Daha sonra, koşullu durumlar, işleçler, döngüler, karakter dizileri ve temel metotları (replace, split, endswith, startswith, join)
listeler, demetler ve bunların metotları, temel dosya işlemleri, bu noktada Py3 için byte'lar ve byte dizileri, sözlükler ve metotları,
fonksiyonlar (Py2 belgelerinde), modüller (Py2 belgelerinde) ve nesne tabanlı programlama (Py2 belgelerinde) kısımlarını iyice öğrenin.

Dikkat ederseniz, bazı kısımları atladım. Bence atladığım kısımları konu başlıklarıyla bilseniz yeterli. Bu kısımları referans materyali
olarak, başınız sıkıştıkça kullanın.

Alan Seçme
----------

Eğer bu rehberi takip ederek çalışmışsanız, şu ana kadar geldiğiniz noktada öğrendikleriniz, Python ile ne yapacak olursanız olun, bilmeniz
gereken kavramlardı. Artık, hangi alanda ilerlemek istediğinize karar vermeniz gerekiyor. [Python kullanım alanları](kullanim-alanlari.html)
yazısında, Python ile çalışılan farklı alanlardan biraz bahsetmiştim. Artık bu noktada, sizin de uzmanlaşmak istediğiniz alana göre, temel
araçları öğrenmeniz gerekiyor. Bu bir arayüz geliştirme kütüphanesi, Web çatısı, bilimsel kütüphaneler vs. olabilir. Gerisi size kalmış.

Artık uzun süreli gelişim sürecine girdiğiniz için, bu sürecin ucu açık. Ne tarafa istiyorsanız, o tarafa gidebilirsiniz.

Paketleme ve Dağıtım
--------------------

Artık alanınızda uzman olduğunuza göre, paylaşmak istediğiniz kodlarınız olacatır. Dolayısıyla, Python paketleri hazırlamayı ve bunları
[Python Paket İndeksi](http://pypi.python.org)'ne yüklemeyi öğrenmeniz gerekecek. Ayrıca, [git](http://git-scm.com/) ve [github](https://github.com/)
ikilisi, her ne kadar Python'a özgü olmasa da, eğer Programcılığa Python ile başladıysanız, şu noktada artık bilmeniz gereken iki araç.

Python Sürümleri
----------------

An itibariyle Python'un en can sıkıcı noktası olsa da, eğer Python programlarınız paylaşmaya başladıysanız, Python sürümleri arasındaki farklılıklara
da artık dikkat etmeniz gerekiyor. Eğer az bir çabayla, hem Py2.7, hem Py3.x sürümlerinde çalışabilecek bir programınız varsa, gerekli düzenlemeleri
yaparak, programınızın daha fazla kişiye ulaşmasını sağlayabilirsiniz.

VirtualEnv
----------

Eğer farklı sürümlerle çalışacaksanız, virtualenv olmazsa olmazlar arasında sayılabilir. Bunu kullanmayı öğrenin. Ya da anaconda kullanın, o da güzel :)

Sonuç
-----

Bir yazının daha sonuna geldim, umarım faydalı olmuştur.