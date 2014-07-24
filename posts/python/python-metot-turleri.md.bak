<!-- 
.. description: Özellikle @classmethod a yönelik, Python'daki metot çeşitleri hakkında bir yazı.
.. date: 2013/11/15 18:17:06
.. title: Python Metot Türleri
.. slug: metot-turleri
-->

Python sınıflarında, temel olarak 3 farklı şekilde metot tanımı yapılabilir.

 * Örnek (Instance) metotları
 * Statik (`@staticmethod`) metotlar
 * Sınıf (`@classmethod`) metotları

 Bunların arasındaki başlıca fark, aldıkları argümanlardır. Örnek metotlarına, ilk argüman olarak, objenin kendisine bir referans gönderilir. Bu argümana,
geleneksel olarak `self` adı verilir. Statik metotlar, kendisini çağıran sınıf veya örnek hakkında herhangi bir bilgiye
sahip değildir. Bunlar, işlevini kaybetmeden, sınıf dışında da aynı şekilde tanımlanabilir. Sınıf metotları ise, otomatik
olarak, kendisini çağıran sınıfa veya örneğin sınıfına bir referans alır. Bu argümana da geleneksel olarak `cls` adı verilir. <!-- TEASER_END -->

## Örnek (Instance) Metotları

Python'da yeni bir sınıf tanımlandığınız, yazdığınız metotlar öntanımlı olarak, örnek (instance) metotlarıdır. Örnek metotları,
ilk argüman olarak, kendisini çağıran örneğe bir referans alır. Böylece, geçerli örneğin niteliklerine erişim ve müdahale
imkanı bulurlar. Aşağıdaki kodları inceleyelim;

	:::python
	class ikisayi(object):

		def __init__(self, a, b):
			self.a = a
			self.b = b

		def toplam(self):
			return self.a + self.b

	
	x = ikisayi(3,5)
	print(x.toplam) # 1
	print(ikisayi.toplam) # 2
	print(x.toplam()) # 3
	print(ikisayi.toplam(x)) # 4
	
Programın çıktısı:

<pre>
#1: &lt;bound method ikisayi.toplam of &lt;__main__.ikisayi object at 0x021F0390&gt;&gt;
#2: &lt;unbound method ikisayi.toplam&gt;
#3: 8
#4: 8
</pre>
	
Yukarıda, görmeye alışık olduğunuz türden bir sınıf tanımımız var. Bu sınıf, iki tane sayı hakkında veri tutmak için kullanılıyor.
Yine, bolca karşınıza çıkacağı gibi `__init__` başlangıç metodu var. `toplam` metodu ise, normal şekilde tanımlanmış, yani bir
örnek (instance) metodu. `toplam` metodumuz, her örnek metodunda olduğu gibi, zorunlu bir ilk argüman alıyor. Bu argümana, çalışma
anında oluşturulmuş bir ikisayı objesi geçirilecek. Böylece, toplam metodu, hangi objenin `a` niteliğiyle `b` niteliğini toplaması gerektiğini bilebilecek.

Program çıktısına dikkat edersek, `x.toplam` metodunun `bound method` olduğunu görüyoruz.Yani, `ikisayi.toplam` metodu belirtilen adresdeki `ikisayi` objesine
bağlanmış. Yani, `x.toplam` metodu çağırıldığında, `ikisayi.toplam` metodu, ilk argüman olarak, o adresdeki objeyi alacak.

Diğer yandan, aynı metoda, sınıf üzerinde eriştiğimizde, bir `unbound method` buluyoruz.Yani, bu method, herhangi bir örneğe bağlanmamış. Dolayısıyla,
otomatik bir ilk argüman almayacak. Eğer `ikisayi.toplam()` şeklinde çağırırsanız, aşağıdaki hatayı alırsınız:

`TypeError: unbound method toplam() must be called with ikisayi instance as first argument`

\#3 ve \#4 numaralı ifadeler aynı çıktıyı veriyor, çünkü, teknik olarak aynı şeyler. Siz, `x.toplam()` çağırdığınızda, Python bunu kendi içinde `ikisayi.toplam(x)` şekline dönüştürüyor. 

## Statik Metotlar

Statik Metotlar, kendisini hangi sınıf veya örneğin çağırdığını bilmez. Sadece kendine
verilen argümanları bilir, örnek veya sınıf metotları gibi, gizli bir ilk argüman almazlar.
Bu yönden bakıldığında, bu fonksiyonun sınıf içinde yazılmasıyla, sınıf dışında yazılması
arasında, hiçbir fark yoktur. Ancak, aynı modül içerisindeki birçok fonksiyonu anlamsal
bütünler içinde toplamak gerektiğinde kullanılabilir. Bunları tanımlamak için, metot tanımından
önce `@staticmethod` [dekoratörü](decorator.html) kullanılır.

## Sınıf Metotları

Diğer yandan, sınıf metotları, ilk argüman olarak, kendisini çağıran sınıfa veya kendisini çağıran örneğin
sınıfına mecburi/otomatik bir referans alır. Bunu o sınıfın bir örneğini oluşturmak istediğiniz durumlarda (bkz: [Factory](http://en.wikipedia.org/wiki/Factory_(software_concept))) kullanabilirsiniz.
Kendisini çağıran sınıfa bir referans aldığı için, alt sınıflarda da istenildiği gibi çalışacaktır. Örneğin, diyelim ki, bir telefon numarasını temsil eden bir sınıfınız var:

	:::python
	class TelNo(object):

		def __init__(self, ulkekodu, alankodu, numara):
			self.ulkekodu = ulkekodu
			self.alankodu = alankodu
			self.numara = numara

Burada, bir telefon numarasının, ülke kodu, alan kodu ve numrasını ayrı değişkenlerde tutan bir sınıf tanımladık. Muhtelemen, elimizdeki
telefon numaraları, bir dosya veya veritabanında "+90 507 7997272" gibi karakter dizileri içerisinde tutuluyordur. Dolayısıyla, böyle karakter dizilerinden
TelNo objesi üreten bir fonksiyona ihtiyacımız olacak.

	:::python
	def str_to_telno(string):
		return TelNo(*string.split(" "))
		
	mytel = str_to_telno("+90 507 7997272")
	
`str_to_telno` fonksiyonu, verilen karakter dizisini boşluklarından bölüp, bunlardan yeni bir TelNo objesi oluşturuyor. Telefon numarası tutabilmek
güzel ama, bu numarayı arayabilmemiz daha da güzel olurdu. Bunun için, TelNo'nun aranabilen bir alt sınıfını oluşturalım. 

	:::python
	class AranabilenTelNo(TelNo):

		def ara(self):
			"bu numaraya VOIP üzerinden bağlantı kur"
			pass # gerçekten bu fonksiyonu kodlamamı beklemiyordunuz umarım :)
			
	def str_to_aranabilentelno(string):
		return AranabilenTelNo(*string.split(" "))

Aynı TelNo'da yaptığımız gibi, bir karakter dizisinden AranabilenTelNo oluşturan bir fonksiyon da tanımladık.

Bu yöntemin şöyle bir sıkıntısı var. Diyelim ki, ileride, mesaj atılabilen telno, mms gönderilebilen tel no vs. gibi bir çok alt sınıf
tanımlayacaksınız. Her seferinde tek tek bu dönüşüm işlemini yapmak hem yorucu olacak, hem de kodlar çorba olacak.

Buna alternatif olarak, `TelNo` objesinde, `from_string` isminde bir `@classmethod` tanımladığımızda, ne olduğuna bakalım;

	:::python
	class TelNo(object):
		def __init__(self, ulkekodu, alankodu, numara):
			self.ulkekodu = ulkekodu
			self.alankodu = alankodu
			self.numara = numara
			
		@classmethod
		def from_string(cls, string):
			return cls(*string.split(" "))
			
	class AranabilenTelNo(TelNo):
		def ara(self):
			pass
			
	mytel = TelNo.from_string("+90 507 7997272")
	print(type(mytel)) # 1
	myaranabilentel = AranabilenTelNo.from_string("+90 507 7997272")
	print(type(myaranabilentel)) # 2
	
Program Çıktısı:

<pre>
#1: &lt;class '__main__.TelNo'&gt;
#2: &lt;class '__main__.AranabilenTelNo'&gt;
</pre>
	
Program çıktısından görebileceğiniz gibi, iki sınıfın `from_string` metotları, doğru sınıfa ait objeler oluşturuyor. Böylece,
hem alt sınıf için tekrar ayrı fonksiyon yazmak zorunda kalmadık, hem de, doğru sınıfa ait bir örnek oluşturabildik.

Dikkat ettiyseniz, `@classmethod` ile tanımladığımız metotları, doğrudan sınıf üzerinden çağırdık. Halbuki, Örnek (Instance) metotlarını, sınıfın bir örneği
üzerinden çağırıyorduk. Özetle, sınıfın kendisi ile ilgili işlem yapılacak durumlarda, `@classmethod` kullanabiliriz.s