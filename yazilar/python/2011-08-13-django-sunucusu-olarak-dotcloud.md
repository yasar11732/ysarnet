<!--
.. date: 2011-08-13 00:59:00
.. description: Dotcloud, cloud computing sunucularında, django uygulamamı barındırdım. Bu yazıda deneyimlerimden bahsedeceğim.
.. slug: dotcloud
.. title: Django sunucusu olarak dotcloud
-->

Son zamanlarda bilişim çevrelerinde sık sık duyabileceğiniz "cloud
computing" teriminin henüz oturmuş bir sözlük anlamı yok. En sık
kullanılan anlamında "cloud computing" bir bilgisayarın kaynaklarının
çoğunlukla sanallaştırma yazılımlarıyla birlikte, birden fazla kişi
tarafından bölüşülmesi demek. Bu hizmeti sağlayan "dotcloud" firmasının,
django uygulamalarını destekleyen bir altyapısı var ve belirli
sınırlamalar çerçevesinde bu hizmeti ücretsiz alabiliyorsunuz. <!-- TEASER_END -->

Dotcloud'u kullanarak, sağladığı hizmetlerden bir veya birkaçı'nı
seçerek, Dotcloud sunucularında bir sanal makina oluşturabiliyoruz.
Sağladığı hizmetlerin çerçevesi mysql, postgresql gibi sık kullanılan
veritabanı sistemlerini, Python gibi programlama dillerini içine alıyor.
Bu yazıyı yazdığım tarihte, 13 adet servis kullanılabiliyordu. Bu
servisler ile codeigniter, django, phpbb, wordpress,mediawiki gibi
yazılımların çalıştırabilmesi mümkün görünüyor. [Dotcloud galerisinde][]
de Dotcloud ile sunulan birkaç örnek sitenin linklerine ve bu sitelerin
hangi hizmetlere birlikte sunulduğu bilgisine ulaşabilirsiniz.

Dotcloud'un ücretlendirme politikası, sanal makine başına kullandığınız
servis sayısı, kendinize özgü bir domain adı isteyip istemediğiniz gibi
birkaç değişkene bağlı olarak değişiyor. Örneğin, bu blog'un sunumunu
Dotcloud ile ücretsiz olarak yapıyorum. Saniyede 1000'den fazla istemin
yapıldığı çok büyük bir kullanıcı kitlesine sahip, ya da ona benzer bir
siteniz yoksa, Dotcloud'un ücretsiz sağladığı hizmetin bir django
projesi sunmak için yeterli olacağını düşünüyorum.

Dotcloud'u kullanabilmek için yapmanız gereken ilk iş, tahmin
edebileceğiniz gibi, [Dotcloud web sayfasını][] ziyaret edip, üye kaydı
yapmak. Üye kaydınızı yaptıktan ve siteye giriş yaptıktan sonra,
[ayarlar sayfası][]ndan api anahtarınızı bulabilirsiniz. Bu anahtara
dotcloud cli'yi ilk çalıştırdığınızda ihtiyacınız olacak.

Dotcloud cli'yi kurmak için, Python'un pip paketine ihtiyacınız var,
çoğu gnu/linux sistemlerde bunu şu komutla kurabilirsiniz:

	:::terminal
	sudo easy_install pip

"pip" paketi hazır olduktan sonra ise, şu komutla dotcloud cli'yi
yükleyebilirsiniz:

	:::terminal
	sudo pip install dotcloud

Daha sonra, terminalden `dotcloud` komutu vererek, dotcloud'u
çalıştırabilirsiniz. İlk çalıştırdığınızda sizden api anahtarınızı
isteyecek. Api anahtarınızı da girdikten sonra, dotcloud programı
kullanıma hazır hale gelecek.

Bu aşamada, dotcloud'da yeni bir uygulama oluşturmanız gerekiyor. Bunu
şu şekilde yapıyoruz:

	:::terminal
	dotcloud create benim_blog
Uygulamayı oluşturduktan sonra, bir yml dosyasıyla, bu uygulamanın hangi
servisleri kullanacağı gibi birkaç özelliğini ayarlamak gerekiyor. Bu
dosyanın ismi *dotcloud.yml* olmalı ve, **kodlarınızın kök dizininde**
bulunmalı. Eğer bu yazıyı adım adım takip ediyorsanız, dotcloud
dosyalarınızı içinde bulunduracak bir klasör açıp, bunun içerisinde boş
bir `dotcloud.yml` dosyası oluşturun. Daha sonra içeriğini aşağıdaki
örneğe benzeterek doldurun.

	:::yaml
	www:
	  type : python
	db:
	  type : postgresql

​1. ve 4. satırlarda, yeni bir servis ile ilgili kısıma başlıyoruz.
Buralardaki "www" ve "db" sözleri, sizin bu servislere taktığınız
isimler. "type" sözcüğü ile belirtilen "python" ve "postgresql" ile
yukarıda belirttiğim 13 adet servisden birer tanesi. Bu yapılandırmada,
python servisi django için, postgresql servisi ise veritabanı olarak
kullanılacaklar.

Dotcloud'la *python* servisini kullanırken, "requirements.txt" isimli
bir dosya içerisinde, bu uygulamanın ihtiyaç duyduğu Python paketlerini
listelemek gerekiyor. Bu dosyayı yine kök dizininde bulundurmalısınız,
ve içeriği de şu şekilde olabilir.

	django
	docutils

Dotcloud *python* servisi aslında python-wsgi işlevi sağladığından
dotcloud kök dizininde wsgi.py isimli bir dosya oluşturup, içinde wsgi
işlevini sağlayacak *application* isminde bir fonksiyon
oluşturmalısınız. Dotcloud belgelerinde bu dosyanın içeriğinin şu
şekilde olması tavsiye ediliyor:

	:::python
	import os
	import sys
	os.environ['DJANGO_SETTINGS_MODULE'] = 'portal.settings'
	import django.core.handlers.wsgi

	djangoapplication = django.core.handlers.wsgi.WSGIHandler()
	def application(environ, start_response):
		if 'SCRIPT_NAME' in environ:
			del environ['SCRIPT_NAME']
		return djangoapplication(environ, start_response)


Burada 3. satırı kendinize göre değiştirmeyi unutmayın. Benim uygulamam
dotcloud için açtığım dizin içerisindeki portal isminde bir dizinde
olduğundan, 3. satırda, `DJANGO_SETTINGS_MODULE` çevre değişkenini bu
şekilde belirttim.

Eğer django admin sitesi statik dosyalarını projeniz içerisinde
barındırmıyorsanız, yine kök dizininde bulunduracağınız "postinstall"
isimli çalıştırılabilir bir dosya sayesinde, django'nun kendi içerisinde
gelen admin paneli statik dosyalarını gerekli dizin içerisine sembolik
bağla yerleştirebilirsiniz. Ayrıca, dotcloud'da tüm statik
dosyalarınızın, dotcloud için açtığınız dizinin içindeki "static"
dizininin içerisinde olması gerekiyor. "postinstall" dosyası içeriği de
örneğin şu şekilde olabilir.

	:::python
	#!/usr/bin/env python

	import os
	os.environ['DJANGO_SETTINGS_MODULE'] = 'portal.settings'
	import django.contrib.admin
	admindir = os.path.dirname(django.contrib.admin.__file__)
	mediadir = os.path.join(admindir,'media')
	staticlink = os.path.join('static','admin_media')
	if os.path.islink(staticlink):
		os.unlink(staticlink)
	os.symlink(mediadir, staticlink)

	migrations_link = "/home/dotcloud/current/portal/blog/migrations"
	migrations_source = "/home/dotcloud/blog/migrations"
	if os.path.islink(migrations_link):
		os.unlink(migrations_link)
	os.symlink(migrations_source,migrations_link)


Burada 4. ve 8. satırları yine kendinize göre düzenlemeniz gerekiyor.
11. satırdan sonrası ile konumuz ile alakasız, ancak, orada yapılanları
anlayanlar için, fazladan bir örnek oluşturması amacı ile orada
bıraktım. Ayrıca, dotcloud'a göndermeden önce, bu dosyayı
çalıştırılabilir yapmayı da unutmayın.

Tüm bunları yaptıktan sonra, veritabanı ayarlarını da yapmanız
gerekiyor. Ben buradaki örneğe postgresql ile devam edeceğim. Ancak, şu
ana kadar aslında dotcloud servislerini başlatmadığımız için, veritabanı
ayarlarını yapamıyoruz. Onun için, öncelikle dotcloud içinh
hazırladığımız dosyaları sisteme göndermemiz gerekiyor. Bunun için,
dotcloud kök dizinindeyken, şu komutu kullanıyoruz:

	:::terminal
	dotcloud push benim_blog

Buradaki "benim\_blog" kodları hangi dotcloud uygulamasına
göndereceğinizi belirtiyor. İlk kez kodlarınızı gönderdiğinizde, sizin
için oluşturulan sanal makineye kodlarınız gönderildikten sonra bu
makine içerisinde, python ve postgresql kurulacak, requirements.txt
içerisinde belirttiğiniz python paketleri indirilip kurulacak ve
python-uwsgi işlevi kullanıma hazır hale gelecek.

Artık aşağıdaki komutları vererek, postgresql ile yeni bir veritabanı
oluşturabilirsiniz. Burada yazıyı fazla uzatmamak için, veritabanında
yeni bir kullanıcı oluşturmadık.

	:::terminal
	dotcloud run benim_blog.db -- createdb -O root portal

Burada, size ayrılan dotcloud makinesinde komut çalıştırmak için
"dotcloud run" komutunu kullandık. "benim\_blog.db" benim blog
uygulamasındaki, db servisini ifade ediyor. Bunu bu şekilde kullanmak
zorundayız, benim\_blog.db ile benim\_blog.www aynı makinadaki farklı
kullanıcılar, ve veritabanına ancak benim\_blog.db ulaşabiliyor.

Veritabanı da kullanıma hazır olduktan sonra, settings modülü içerisinde
gerekli değişiklikleri yapmanız gerekiyor. Veritabanının HOST, PASSWORD
ve PORT bilgilerini, şu komutla öğrenebilirsiniz.

	:::terminal
	dotcloud info benim_blog.db
Tüm ayarları doğru bir şekilde tamamladıktan sonra, değişikliklerin
uygulanması için, kodlarınızı bir kez daha yukarıda yaptığımız gibi
dotcloud'a göndermelisiniz.

Son olarak, django'nun veritabanında gerekli tabloları oluşturması için
şu komutu verebilirsiniz:

	:::terminal
	dotcloud run benim_blog.www -- python current/portal/manage.py syncdb

Dotcloud makinesinde, en son gönderdiğiniz kodlar,
/home/dotcloud/current içerisinde tutuluyor. Bu durumda, manage
modülünün tam yolu da benim için current/portal/manage.py oluyor. Herşey
yolunda gittiyse, artk django uygulamanız kullanıma hazır durumda
olmalı.

Dotcloud çok geniş bir konu olduğu için, burada anlattıklarım biraz
üstünkörü kalıyor olabilir, ama başlangıç için yeterli olacaktır. Bu
noktadan sonra ise yolunuzu bulmak size kalmış. Ancak takıldığınız bir
konu olursa, aşağıdaki yorumlardan bana iletebilirsiniz.

  [Dotcloud galerisinde]: https://www.dotcloud.com/gallery/
  [Dotcloud web sayfasını]: http://docs.dotcloud.com/
  [ayarlar sayfası]: https://www.dotcloud.com/accounts/settings