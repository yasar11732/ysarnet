<!--
.. date: 2011-08-17 14:49:00
.. description: Django modelleri web programı geliştirmek için değil, bir paket yöneticisi yapmak için kullanılabilir mi?
.. slug: djangoda-paket-yoneticisi
.. title: Django Modelleriyle Paket Yöneticisi
-->


Birçok web uygulama ve python geliştiricisi, Django'nun harika bir web
çatısı olduğunu düşünür. Ancak, Django'yu bir web çatısı olmakla
sınırlandırmak, bence biraz haksızlık olur. Django'nun parçalarının
mümkün olduğu kadar birbirinden bağımsız olmasından dolayı, kolaylıkla
istediğiniz parçasını, kendi uygulamalarınıza dahil edebilirsiniz.
Django'nun kişisel olarak en sevdiğim yanı veritabanı API'si olduğu için,
Django'nun veritabanı geliştirme arayüzünü nasıl kendi projemize dahil
edebileceğimizi göstermek için, küçük bir örnek yapmak istedim. <!-- TEASER_END -->

Örneğimizde, çok basit, sadece iki fonksiyondan oluşan bir paket
yöneticisi yazacağız. Lütfen örnekdeki kodu çalıştırmaya çalışmayın.
Örnek olsun diye yazılmış, bir kez bile denenmemiştir. Bunu açıklığa
kavuşturduğumuza göre, işe koyulalım. İlk iş, uygulamanız için bir dizin
oluşturup, içinde bir Django projesine başlamak.

	:::terminal
	mkdir PaketYoneticisi
	cd PaketYoneticisi
	django-admin.py startproject veritabani
	cd veritabani
	django-admin.py startapp Paket

Gerekli dizin yapılanmasını ayarladıktan sonra, Django projesi
ayarlarından gereksiz kısımları atabilirsiniz. Sadece veritabanı
kullanacağımız için, şu kadar ayar yeterli olacaktır:

	:::python
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': 'paketler.db',                      # Or path to database file if using sqlite3.
			'USER': '',                      # Not used with sqlite3.
			'PASSWORD': '',                  # Not used with sqlite3.
			'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
		}
	}

	INSTALLED_APPS = ( "Paket", )

Artık paket modelini yazabiliriz. Mümkün olduğu kadar kısa tutacağım. Bu
kodlar, Paket uygulamasının, models modülü içerisinde olmalı.

	:::python
	from django.db import models

	# Create your models here.

	class Paket(models.Model):
		isim = models.CharField(max_length=40)
		versiyon = models.CharField(max_length=20)
		dosyalar = models.TextField("Dosya Listesi")
		gerekli = models.ManyToManyField("self",blank=True,symmetrical=False,related_name="bagimlilik")
Artık veritabanında gerekli tabloları oluşturabilirsiniz. Django projesi
ana dizinindeyken, şu komutla veritabanlarını oluşturabiilrsiniz.

	:::terminal
	python manage.py syncdb

Django'yla alakalı kısımlar, kendi projenize dahil edilmek için hazır.
Şimdi, kendi projenizin kök dizinde, yani, bu örnekde oluşturduğumuz
PaketYoneticisi dizini içerisinde, uygulamanızı geliştirmeye
başlayabilirsiniz. Örnek kodlar yorumlarıyla birlikte aşağıda:

	:::python
	# -*- coding:utf-8 -*-

	import os
	import sys
	import imp
	import tarfile
	import shutil

	# Django'yu projeye dahil etmeden önce, DJANGO_SETTINGS_MODULE çevre değişkenini
	# ayarlamak gerek!
	 
	os.environ["DJANGO_SETTINGS_MODULE"] = "veritabani.settings"

	# veritabani klasörünü python yoluna ekleyelim :)

	PROJE_DIZINI = os.path.abspath(os.path.dirname(__file__))
	sys.path.append(os.path.join(PROJE_DIZINI,"veritabani"))

	# artık modellerimizi projemize dahil edebiliriz.
	from Paket.models import Paket

	def yukle(paket_yolu):
		# Basitleştirilmiş bir paket yükleme fonksiyonu
		# Örnek amaçlıdır, çalışmaz! KULLANMAYIN!!
		
		
		try:
			paket = tarfile.open(paket_yolu,'r|gz')
		except:
			sys.exit(1)
			
		# paketi geçici bir klasöre açalım,
		# uzatmamak için rastgele isim üretmedim.
		paket.extractall(u"/tmp/rasgeleuretilmişisim")
		
		# Şimdi paket bilgilerini yüklemeliyiz, bu örnekte
		# paket bilgilerinin bir python modülünde olduğunu varsayıyorum
		# üstünde çalışması daha kolay :)
		
		paket_bilgileri = imp.load_source("paket_bilgisi",u"/tmp/rasgeleuretilmiçisim/ayarlar.py")
		
		# Eğer paket zaten yüklüyse, hata vererek çıkıcaz.
		try:
			Paket.objects.get(isim=paket_bilgileri.isim)
			sys.exit(1)
		except:
			pass
		
		# paket gereksinimleri sağlanmış mı?
		
		for paket in paket_bilgileri.gereksinimler:
			try:
				Paket.objects.get(isim=paket)
			except:
				sys.exit(1)
				
		
		# Eğer paketle yüklemeye çalıştığımız dosyalar sistemde zaten mevcutsa, yine hata vereceğiz!
		
		for dosya in paket_bilgileri.dosyalar:
			if os.path.isfile(dosya):
				sys.exit(1)
				
		# Dosyaları sisteme kopyalayabiliriz.
		
		for dosya in paket_bilgileri.dosyalar:
			shutil.copyfile(u"/tmp/rasgeleuretilmisisim/" + dosya, dosya)
			
		# paketi veritabanına kaydedelim
		
		p = Paket.objects.create(
			isim=paket_bilgileri.isim,
			versiyon = paket_bilgileri.versiyon,
			dosyalar = "\n".join(paket_bilgiler.dosyalar)
		)
		
		for paket in paket_bilgileri.gereksinimler:
			gereksinim = Paket.objects.get(isim=paket)
			p.gereklis.add(gereksinim)
			
		p.save()
		
	def sil(paket_adi):
		"Basit bir paket silme programı, örnketir, KULLANMAYINIZ"
		
		# gerekli paket bilgisini yükleyelim
		
		try:
			silinecek = Paket.objects.get(isim=paket_adi)
		except:
			sys.exit(1)
		
		# Eğer bu pakete ihtiyaç duyan varsa, silme işlemini iptal etmeliyiz.
		
		if silinecek.bagimlilik.all().count() > 0;
			sys.exit(1)
			
		dosyalar = "\n".split(silinecek.dosyalar)
		
		for dosya in dosyalar:
			os.remove(file)
		silinecek.delete()

Böylece, kısaca, Django'nun belli kısımlarını kendi projemiz içerisine
dahil edebileceğimiz gördük. Ben burada gerçekten işe yarayan bir örnek
yapmadım. Bunun yerine böyle bir olasılığın varlığyla ilgili bir örnek
göstermek istedim.

İyi geliştirmeler.