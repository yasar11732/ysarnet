<!--
.. date: 2011/08/05 23:14:00
.. description: Django ile basit bir blog uygulaması nasıl hazırlanır? Django ile blog geliştirme yazı serisinin ilk yazısında, django kurulumu ve yeni projeye başlama konuları anlatılacak.
.. slug: kurulum-ve-ilk-ayarlar
.. title: Django ile Blog Geliştirme - Kurulum ve İlk ayarlar
-->

Django, bir çırpıda uygulama geliştirmenizi, temiz ve sonuç odaklı kod yazmanızı destekleyen bir
web çatısı (framework)'dür. Django iki temel sorunla başa çıkmaya çalışır: kısıtlı zaman ve deneyimli
web geliştiricilerinin sıkı kalite standartları. Django yüksek performanslı, zarif web uygulamarını
kısa zamanda geliştirebilme imkanı sunar. 

Django'nun temel özellikleri arasında, zengin veritabanı erişim API'si, otomatik admin sayfası, şık url
tasarımı, şablon sistemi, önbellek sistemi ve çoklu dil desteği sayılabilir.

[Django siteleri](http://www.djangosites.org/) arasında, Disqus, Instagram, Mozilla, OpenStack, Pinterest
gibi büyük siteler yer alır. <!-- TEASER_END -->

Python ile web geliştirmenin benim için vazgeçilmezlerinden biri olan
django çatısı ile, baştan başlayarak nasıl bir blog geliştirileceğine
dair bir yazı dizisine başlıyorum. Örnek kodlarıyla birlikte geliştirilecek
bu uygulamaya ait yazıların 01. bölümünde yeni bir django projesine nasıl
başlanacağına ve ilk ayarlara değineceğim. <!-- TEASER_END -->

Bu yazı dizisinde bahsedilen blog uygulamasının son haline [github
deposu](https://github.com/yasar11732/django-blog)ndan ulaşabilirsiniz.

Django çatısı ile python web uygulaması geliştirmeye başlamadan önce ilk
iş bir Python yorumlayıcısı edinmek olacaktır. Eğer bir gnu/linux veya
unix tabanlı bir bir işletim sistemi kullanıyorsanız, muhtemelen Python
programlama dili sisteminizde zaten kuruludur. Emin olmak için,
gnu/linux komut satırına `which Python` komutunu
verebilirsiniz. Eğer Python sisteminizde yüklü değilse, komutun
bulunamadığına dair bir hata alırsınız. Böyle bir hata almanız halinde,
sisteminize ait paket yöneticisi aracılığıyla, veya kaynak koddan
derleyerek Python programlama dilini kurabilirsiniz. Bunların
detaylarına değinmeyeceğim.

<del>Ancak şunu belirtmek isterim ki **Django Python'un 3.0 ve üzeri
sürümleri desteklemiyor.**</del><ins cite="https://docs.djangoproject.com/en/dev/releases/1.5/">Django artık Python 3 destekliyor.</ins> Python kullanmak için, 2.5,2.6 veya 2.7
sürümlerini tavsiye edebilirim.

Windows'da Python kurmak için ise [Python'un resmi sitesi](http://Python.org/)nden Windows
kurulum dosyalarını indirip, kurmanız gerekiyor. <del>**2.x bir sürüme
ihtiyacınız olduğunu tekrar belirtmek istiyorum.**</del> Python'u kurduktan
sonra, Python ana dizinini (genellikle `c:\Python27`) ve Python ana
dizini içindeki `Scripts` dizinini windows sistem yoluna eklemek iyi bir
fikir olabilir. Böylece, Python'un kendisi ve yüklü Python paketlerinin
çalıştırılabilir dosyaları komut satırından erişilebilir hale gelir.
Windows'da Python kullanmanın bir diğer yöntemi için [Cygwin aracıyla
ilgili açıklamalar](/yazilim-dunyasi/windowsda-gnu-linux-tadi-cygwin.html)'a bakabilirsiniz.

Çalışan bir Python yorumlayıcısı elde ettikten sonra, ihtiyacınız olan
şey -tahmin edersiniz ki- django çatısı. Gnu/Linux sistemlerin
birçoğunda Django web geliştirme çatısı resmi paket depolarında veya
kullanıcı depolarında bulunabilir. Eğer depolarda bulamazsanız veya
Windows kullanıyorsanız, birkaç seçeneğiniz var.

İlk seçeneğiniz, django'nun kaynak kodlarını indirip,
`python setup.py install` komutunu kaynak kodlarını açmış
olduğunuz dizinden çalıştırarak kurulum yapmak.Eğer windows kullanıcısı
iseniz, python sistem yolunuzda olmayabilir. O yüzden ya python'u sistem
yolunuza ekleyin, ya da python yorumlayıcısının tam yolunu kullanını.

Gnu/Linux sistemlerde ise bunu yapmak için yönetici haklarına ihtiyaç
duyabilirsiniz. Diğer bir seçeneğiniz ise, eğer setuptools python paketi
sisteminizde yüklüyse,`easy_install django` komutuyla
yükleme yapmak. Bu komut django web çatısını sizin için indirip
kuracaktır. Diğer bir seçenek ise pip aracılığıyla yükleme yapmak. Eğer
pip python paketi sisteminizde yüklüyse, `pip install django` komutu aracılığıyla
da yükleme yapabilirsiniz. Django'nun kurulumunu yaptıktan sonra, python kabuğuna
girip, şu komutu vererek, django'nun dosylarının içe aktarılabildiğinden emin olun: `import django`

Eğer bu komutu verdikten sonra hiçbir hata almazsanız, django ile web
geliştirme yapmaya hazırsınız demektir.

Django'nun kurulumunu yaptıktan sonra, eğer daha önceden başlanmış bir
projeniz yoksa,

	:::terminal
	django-admin.py startproject proje_adi

komutuyla yeni bir django projesine başlayabilirsiniz. Bu komut size
`proje_adi` isimli bir dizin içinde, 4 adet dosya oluşturacak.

 - `__init__.py` Boş bir dosyadır. Bu dosyayla neredeyse hiç bir işiniz olmayacak. Bu
   dizinin bir python paketi olduğu belirtmek için oradadır.
 - `manage.py` `django-admin.py` ile neredeyse aynı işi yapar, ancak projenizi
   python yoluna eklemek ve `DJANGO_SETTINGS_MODULE` çevre değişkenini ayarlamak
   gibi birkaç ek fonksiyonu vardır. Bu yüzden projenizin yönetimini bu modül
   aracılığıyla yapacaksınız. Ne yaptığınızdan çok emin değilseniz, bu dosyayı olduğu
   gibi bırakın.
 - `urls.py` Sitemizde hangi url'in nasıl sunulacağına ilişkin bilgi içerir. Daha detaylı
   bilgiye ilerleyen zamanlarda değineceğiz.
 - `settings.py` Projenin bütün ayarları bu modülün içerisindedir. `manage.py` ile aynı
   dizin içinde olması ve adının `settings.py` olması şarttır. Aksi halde başınız bir
   hayli ağrıyacaktır.
   
Ayarların detaylarına birazdan değineceğiz. Böylece içi boş
bir django projesine başlamış olduk. Eğer gözlerinizle şahit olmak
isterseniz, proje dizininizin içindeyken,

	:::terminal
	python manage.py runserver

komutunu vererek geliştirme sunucusunu başlatabilirsiniz. Bu sunucuyu
geliştirme süreci boyunca kullanacaksınız, ama günlük kullanım web
sunucusu olarak tavsiye edilmiyor. Eğer sunucunuz başarıyla çalıştıysa
(localhost)[http://localhost:8000] adresine giderek django'nun "It Worked" (Çalıştı) sayfasını
görebilirsiniz. Ama henüz birşey yapmış değiliz.

Bu yazının son kısmında biraz ayarlara bakacağız. Django projenizin
ayarları settings.py içerisinde bulunur. Bu modülü istediğiniz zaman
uygulamalarınıza "import" ile dahil ederek kullanabilirsiniz. Şimdi her
ayara tek tek bakmaktansa birkaç tanesinin üzerinde duracağım.

	:::python
	DEBUG = True

Bu ayar django projenizde bir hata olduğu zaman ayrıntılı hata ayıklama
mesajlarını görmenizi sağlıyor. Geliştirme sunucuzdayken çok kullanışlı
bir özellik olsa da, günlük kullanım sunucunuza geçtiğinizde kapatmanız
gerekir. Günlük kullanım sunucunuzda açık bırakmak güvenlik açığına
neden olur.

	:::python
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': '/home/yasar/database.db',                      # Or path to database file if using sqlite3.
			'USER': '',                      # Not used with sqlite3.
			'PASSWORD': '',                  # Not used with sqlite3.
			'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
		}
	}

Burada veritabanı ayarlarını yapıyoruz. Blog uygulaması örneğimizde
kullanımı kolay olması açısından sqlite3 veritabanı kullanacağız. Bu
yüzden ENGINE'i django.db.backends.sqlite3 olarak ayarladık. Diğer
seçeneklerimiz sqlite3 yerine 'postgresql\_psycopg2', 'postgresql',
'mysql' veya 'oracle' olabilirdi. Bunların hangisinin ne anlama geldiği
yeteri kadar açık sanırım. NAME anahtarı kullandığımız veritabanının
adı, eğer sqlite3 kullanıyorsak, bu veritabanımızın dosya yolu. **Tam
yol kullanmayı unutmayın.** USER ve PASSWORD, veritabanımızın kullanıcı
adı ve şifresi, sqlite için boş bırakabiliriz. HOST ve PORT ise
sırasıyla veritabanın hangi makinede bulunduğunu ve portunu belirtiyor.
Eğer veritabanı localhost'daysa ve öntanımlı port üzerindeyse, boş
bırakabiliriz. Ayrıca sqlite için bu değerlerin bir anlamı yok.

	:::python
	TIME_ZONE = 'Europe/Istanbul'

zaman dilimimizi ayarlıyoruz. Windows sistemlerde, sisteminizde ayarlı
saat dilimiyle aynı olmalı. Türkiye'deki windows kullanıcıları bunun
için bu değeri 'Europe/Istanbul' olarak ayarlamaları gerekiyor. Unix
sistemlerde ise None girmek django'nun otomatik olarak sistem saatinizi
kullanmasına neden olur. Buraya girilebilecek değerlerin büyük bir
çoğunluğunu [saat dilimiyle alakalı wikipedia makalesinde](http://en.wikipedia.org/wiki/List_of_tz_zones_by_name) bulabilirsiniz.

	:::python
	LANGUAGE_CODE = 'tr'

Bu projenin dilini ayarlıyor. Türkçe için 'tr' girebilirsiniz.

	:::python
	STATIC_ROOT = '/home/yasar/static_files'

css, js ve resim dosyaları gibi içeriği sabit dosyaların toplanacağı
yer. Buraya kendiniz birşey eklemeyin. Detaylarına daha sonra
değineceğiz. Bu dizini proje dosyanızın dışarısında tutmakta fayda var.

	:::python
	STATIC_URL = '/static/''

Bu statik dosyaları hangi link üzerinden sunulacağını ayarlıyor. Olduğu
gibi bırakılabilir.

	:::python
	SECRET_KEY = 'asdfasdşfj qğwfasdfj lşahwe fhaşslkdnfj pqwdnf ş'

Bunu kimseye göstermeyin. Yeteri kadar uzun, eşsiz ve rastgele bir şey
olmalıdır. Size özel bir gizli anahtardır. Şifreleme işlemleri için
kullanılır. Ayrıca, hazırda çalışan bir sitenin SECRET\_KEY'ini
değiştirmek, eski verilere ulaşamamanıza neden olabilir. Projenizi ilk
başlattığınızda size özel bir adet oluşturulur. Olduğu gibi
bırakabilirsiniz.

	:::python
	INSTALLED_APPS = (
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.sites',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		# Uncomment the next line to enable the admin:
		# 'django.contrib.admin',
		# Uncomment the next line to enable admin documentation:
		# 'django.contrib.admindocs',
	)

Bu projede yüklü olan uygulamaların bir listesi. Bunlar yeni bir projeye
başladığınızda otomatik olarak eklenenler. Eğer bunlardan birkaçına
ihtiyacınız olmadığından eminseniz, buradan kaldırabilirsiniz. Ancak
bunlara dokunmamayı tavsiye ederim. En azından şimdilik. Bu yazıda
inceleyeceğimiz ayarlar bu kadar. Yazı dizisinin ilerleyen bölümlerinde
yeri geldikçe ayarlar dosyasına tekrar döneceğiz.

Bu yazıda django ile yeni bir projeye başlamaya ve projenin bazı temel
ayarlarına değinmeye çalıştım. Bir sonraki yazıda [Django modelleri](uygulama-modeller.html) anlatılacak.