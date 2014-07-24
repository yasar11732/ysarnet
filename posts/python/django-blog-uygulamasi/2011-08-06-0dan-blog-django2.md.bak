<!--
.. date: 2011/08/06 22:09:00
.. description: Django uygulaması nasıl oluşturulur? Django uygulamasında veri yapıları nasıl belirlenir? Örnekleriyle django modelleri ve veritabanı işlemleri...
.. slug: uygulama-modeller
.. title: Django ile Blog Geliştirme - Modeller
-->

[Django'ya başlangıç bölümü](kurulum-ve-ilk-ayarlar.html) kurulumdan ve
ayarlardan bahsetmişti. Yazı dizisinin ikinci bölümünde projemizin içinde blog
uygulamasına başlayacağız ve uygulamamızın modellerini yazacağız. <!-- TEASER_END -->

Bu yazı dizisinde bahsedilen blog uygulamasının son haline [github
deposu][]ndan ulaşabilirsiniz.

Django'da yeni bir uygulamaya başlamak için, komut satırından başlamış
olduğumuz projenin ana dizininin içindeyken <!-- TEASER_END -->

	:::terminal
	python manage.py startapp blog

komutunu vererek, projemizin içinde blog isminde yeni bir uygulamaya
başlayabiliriz. Her django projesi bir veya birden fazla uygulamadan
oluşur. Aynı zamanda bir proje'de geliştirdiğiniz uygulamayı kolaylıkla
başka projelerinizde de kullanabilirsiniz. Aynı şekilde başkalarının
geliştirdiği uygulamaları da kendi projenize çok rahatlıkla dahil
edebilirsiniz. Bu özellik, django'nun en önemli özelliklerinden biridir.
Bir kez yaptığınız bir işi, tekrar yapmanızı engeller.

Yeni başladığımız uygulama, blog isimli bir klasörün içerisinde bulunan
4 adet py uzantılı dosyadan oluşuyor.

 - `__init__.py`: boş bir dosyadır. Bu dosyayla neredeyse hiç bir
işiniz olmayacak. Bu dizinin bir python paketi olduğu belirtmek için oradadır.
 - `model.py`: sıradan bir python modülüdür. Bu modülün içerisinde veri
yapılarımızı, yani modellerimizi, tanımlayacağız. Bu dosyanın detaylarına daha
sonra değineceğiz.
 - `views.py`: içerisinde verilerimizi nasıl sunacağımıza karar verecek
olan sınıfları tanımlayacağız. Yazı dizisinin ilerleyen bölümlerinde
zaman zaman bu dosyayla ilgili detaylara değineceğiz.
 - `tests.py`: modülün içerisinde birim testi yapmak için gerekli sınıflar
bulunur. 

Yeni ugulamamızı artık tanıdığımıza göre, modellerimizi yazmaya
başlayabiliriz. Ben bu uygulamada yalnızca iki model kullanacağım, bir
tanesi makele için, bir tanesi de etiket için. Yorumlar için yazı
dizisinin ilerleyen bölümlerinde disqus kullanmaya değineceğiz.

Uygulamamızın models modülünün içerisinde sadece django'nun models
modülünü dahil edildiğini görüyoruz. Buraya kendi modelimizi eklemek
için, django'nun models modülünde bulunan Model sınıfından kalıtım alan
(inheritance) yeni bir sınıf tanımlamamız gerekiyor.

	:::python
	class makale(models.Model):
	  pass

Böylece yeni bir model üretmiş olduk. Bu model veritabanınızda bir
tabloya karşılık geliyor. Bu modelin karşılık geldiği tabloda sütun
oluşturmak için, modelimize bir alan girmemiz gerekiyor. Örneğin
makelemizin bir başlığa ihtiyacı var. Makale modelimize bir başlık
ekleyelim:

	:::python
	class makale(models.Model):
	  baslik = models.CharField(max_length=60)

Böylece, makale modelimize bir `baslik` alanı eklemiş olduk. Başlık
alanımız bir karakter dizisi olacak. models.CharField bir karakter
dizisine karşılık geliyor. Bu karakter dizisinin uzunluğu 60 karakterle
sınırlı olacak. Django alanlarına max\_length gibi birçok argüman
verebiliriz. Yeri geldikçe bunlardan bahsedeceğim. Şimdi de diğer
alanlarımızı ekleyelim.

	:::python
	slug = models.SlugField(unique=True)

Burada bir slug alanı ekliyoruz. Slug alanı sadece harfler, rakamlar,
tireler ve alttirelerden oluşan bir karakter dizisidir. Örneğin, şu anda
adres çubuğunun son kısmına baktığınızda gördüğünüz şey veritabanında
bir slug alanında tutuluyor. *unique=True* argümanı bu slug alanının
özgün olmasını sağlıyor. Bu alanı makaleye ait linki tutmak için
kullanacağımızdan, bu alanın özgün olması gerekiyor.

	:::python
	giris = models.TextField(max_length=500)

Burada ise bir yazı alanı tanımlıyoruz. Bu alanı her makalenin ilk
paragrafını tutması için kullanacağız. Bu alanı makalenin özetine
ihtiyaç duyan birkaç farklı yerde kullanacağız. Örneğin bu blogun
anasayfasına bakarsanız göreceğiniz makalelere ait özetleri bu alanda
tutuyorum.

	:::python
	makale = models.TextField()

Burada da makalenin kalanı olacak. Maksimum değeri kullanmıyorum.
Makalelerimizi istediğimiz kadar uzun yazabiliriz.

	:::python
	yayin_tarihi = models.DateTimeField("Yayınlanma Tarihi")

Bu alanda makalemizin yayınlanma tarihini tutacağız. Argüman olarak
verdiğimiz karakter dizgesi, bu alanın görünen adı olacak. Bu adın ne
işe yarayacağına daha sonra değineceğiz. Böylece makalemize ait alanları
tanımlamış olduk.

Ancak modelimize birkaç tane de metod eklememiz gerekiyor. Modellerinize
ihtiyaç duyduğunuz kadar metod ekleyebilirsiniz. `__unicode__()`
metodunu tanımlayalım.

	:::python
	def __unicode__(self):
		return self.slug

Bu metodun döndürdüğü değer makalemizin görünen adı olacak. Bu ad
ileride işe yarayacak. O yüzden şimdiden tanımlamakta fayda var. Bu
fonksiyondan birşey döndürdüğünüzden emin olun. makale modelimize
ileride tekrar dönüp birkaç tane metod ekleyeceğiz. Ama şimdilik bu
kadar yeterli. makale modelimizi bitirdiğimizde şu şekilde görünüyor
olmalı:

	:::python
	# -*- coding: utf-8 -*-
	from django.db import models
	class makale(models.Model):
		baslik = models.CharField(max_length=60)
		slug = models.SlugField(unique=True)
		giris = models.TextField(max_length=500)
		makale = models.TextField()
		yayin_tarihi = models.DateTimeField("Yayınlanma Tarihi")
		
		def __unicode__(self):
			return self.slug

Şimdi de etiket modelimizi yazalım. `makale` modeline nazaran kolay bir
model olacak. Sadece tek bir alanı var, yazi:

	:::python
	class etiket(models.Model):
		yazi = models.CharField(max_length=15, unique=True)
		
		def __unicode__(self):
			return self.yazi

Yalnız bu modele küçük bir ekleme yapmak istiyorum. Bu modelin yazi
alanındaki değeri url olarak kullanacağım için, url olmaya uygun
olduğundan emin olmam gerekiyor. Bunun için validator (doğrulayıcı)
kullanacağım. Validator'lerin detaylarına şu anda girmek istemiyorum.
Bizim ihtiyacımın olan validator'u kullanmak için önce yeni bir import
(dahil etmek) yapmamız gerekiyor.

	:::python
	from django.core.validators import validate_slug

Bu ifade bizim için django içerisinde hazır gelen validator
fonksiyonlarından validate\_slug'ı modülümüze dahil edecek. Şimdi
modelimizi şu şekilde değiştireceğiz.

	:::python
	class etiket(models.Model):
		yazi = models.CharField(max_length=15, unique=True, validators=[validate_slug])
		
		def __unicode__(self):
			return self.yazi

Böylece yazi alanına yeni bir doğrulayıcı eklemiş olduk. Django artık bu
alana yeni bir kayıt eklemeden önce, bu kaydın url çubuğuna uygun olup
olmadığına karar verecek. Eğer uygun değilse, canımızı sıkacak :)

Bu aşamada etiketlerle makaleler arasında bir ilişki kurmamız gerekiyor.
"etiket" modelimizi birden fazla makale modeline ekleyebiliriz. Aynı
zamanda, bir makale modeline ait, birden fazla etiket olabilir. Bu tip
ilişkilere çokdan-çoğa ilişki diyoruz (en azından ben öyle diyorum).
Django bu tip ilişkileri kullanmak için ManyToManyField kullanıyoruz.
Şimdi makele modelimizi şu hale getirelim:

	:::python
	class makale(models.Model):
		baslik = models.CharField(max_length=60)
		slug = models.SlugField(unique=True)
		giris = models.TextField(max_length=500)
		makale = models.TextField()
		yayin_tarihi = models.DateTimeField("Yayınlanma Tarihi")
		etiketler = models.ManyToManyField(etiket)
		
		def __unicode__(self):
			return self.slug
Böylece makalemizi çoktan-çoğa olacak bir şekilde etiketlerle
ilişkilendirdik. ManyToManyField'ı ilişkinin hangi tarafına koyduğunuzun
pek bir önemi yok. Ama genellikle, kapsayıcı olan tarafa eklemek tercih
edilir. Örneğin burada, etiketleri makale'ye eklediğimiz için, bu alanı
makalelere ekledik. Artık modellerimiz kullanıma hazır.

Modellerimizi hazırladığımıza göre, artık uygulamamızı projemize dahil
edebiliriz. Projemizin ana dizinindeki settings modülünde
INSTALLED\_APPS şeklinde bir liste göreceksiniz. Bu listeye
hazırladığımız uygulamayı ekleyelim:

	:::python
	INSTALLED_APPS = (
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.sites',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'projem.blog',
	)

Burada "projem" projenizin adı, blog ise uygulamınızın adı. İsimleri
kendize göre düzeltmeniz gerekiyor.

Artık veritabanımızda gerekli tabloları oluşturabiliriz. Daha doğrusu,
django bizim için gerekli tabloları oluşturacak. Projemizin ana
dizininden şu komutu verelim:

	:::terminal
	python manage.py syncdb
Bu komut veritabanımızda gerekli tabloları oluşturacak. Eğer yüklü
uygulamalarınızın içerisinde admin varsa, sizden bir superuser
oluşturmanızı isteyecek. Bu superuser, yönetici paneline ulaşmanızı
sağlayacak. Yönetici paneline ilerleyen derslerde değineceğim.

Bu yazıda yeni bir django uygulamasına başladık ve bu projenin veri yapılarını belirledik. Çeşitli veri yapısı özelliklerine değindik.
Bir sonraki yazıda [Django Yönetici Paneli](yonetici-paneli.html) anlatılacak.


  [github deposu]: https://github.com/yasar11732/django-blog