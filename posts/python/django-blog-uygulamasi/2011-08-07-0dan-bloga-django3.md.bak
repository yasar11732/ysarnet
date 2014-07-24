<!--
.. date: 2011/08/07 20:21:00
.. description: Django'da yönetici (admin) sayfaları nasıl oluşuturulur? Uygulamalar yönetici paneline nasıl kaydedilir? Django yönetici panelinde otomatik alan doldurma nasıl yapılır?
.. slug: yonetici-paneli
.. title: Django ile Blog Geliştirme - Yönetici Paneli
-->

[Django Modelleri](uygulama-modeller.html) yazısında django'da veri yapılarının
oluşturulmasından ve bunların veritabanına kaydedilmesinden bahsetmiştik. Bu yazımızda
ise, uygulamamızı django'nun yönetici paneline kaydedeceğiz. <!-- TEASER_END -->

Bu yazı dizisinde bahsedilen blog uygulamasının son haline [github
deposu][]ndan ulaşabilirsiniz.

Django'nun belki de en güzel özelliklerinden biri bizi yönetici paneli
yapmaktan kurtarmasıdır. Django kendi içerisinde bir admin sitesi
uygulamasıyla gelir, ve bu uygulamayı kolaylıkla projemize dahil
edebiliriz. Eğer halen aktifleştirmediyseniz, `settings` modülü
içerisindeki `django.contrib.admin` uygulamasını şimdi
aktifleştirebilirsiniz. `settings` modülü içerisindenki `INSTALLED_APPS`
listesinde zaten varsa, django.contrib.admin'in başındaki `#` işaretini
kaldırın, eğer yoksa bunu listeye kendiniz ekleyin. Django'nun yönetici
sitesinin bağımlılıkları yeni bir django projesinin içerisinde
kendiliğinden sağlanmış olarak gelirler. Ancak, bu bağımlıkları
yanlışlıkla sildiğinizi düşünüyorsanız, şunları kontrol edin:

 - Yüklü uygulamalarınız içerisinde şunlar var mı: `django.contrib.auth`, `django.contrib.contenttypes`, `django.contrib.messages`
 - `MIDDLEWARE_CLASSES` içerisinde `MessageMiddleware` var mı?
 - `TEMPLATE_CONTEXT_PROCESSORS` içerisinde django.contrib.messages.context\_processors.messages var mı?

Eğer bunların hepsi varsa, admin sitesi kullanıma hazır demektir. Eğer
admin sitesini yeni aktifleştirdiyseniz, şu komutu vererek veritabanında
admin sitesi için gerekli olan tabloları oluşturun:

	:::terminal
	python manage.py syncdb

Bu komut eğer daha önce bir yönetici hesabı oluşturmadıysanız, bir
yönetici hesabı oluşturmanızı isteyecek. Gerekli bilgileri girerek
yönetici hesabınızı oluşturun.

Admin sitesi uygulamasını yüklemiş olmamıza rağmen, henüz bu siteye
hangi link üzerinden ulaşılacağını django'ya bildirmedik. URL
tanımlaması yapması konusuna daha sonra değineceğiz. Şimdilik, proje ana
dizininiz içindeki urls modülünde, admin uygulaması için gereken
değişiklikleri yapın, urls modülünüzün şu şekilde görünmesi gerekiyor.

	:::python
	from django.conf.urls.defaults import patterns, include, url
	from django.contrib import admin
	admin.autodiscover()

	urlpatterns = patterns('',
		url(r'^admin/', include(admin.site.urls)),
	)

Artık admin panelimiz kullanıma hazır. Ancak, admin panelinin düzgün
görünmesi için gereken statik dosyalar yerinde olmayabilir. *settings*
modülünde tanımladığınız ADMIN\_MEDIA\_PREFIX'in gösterdiği yere, admin
uygulamasıyla birlikte gelen statik dosyaları kopyalamanız gerekiyor. Bu
dosyalar, djangoyu yüklediğiniz klasör altındaki, contrib/admin/media
içerisinde bulunur. Örneğin, ADMIN\_MEDIA\_PREFIX'iniz /static/admin
ise, contrib/admin/media içersindeki bütün dosyaları, statik
dosyalarınızı tuttuğunuz dizinin içerisinde, admin ismindeki bir klasöre
kopyalamalısınız. Artık admin siteniz kullanıma hazır. Eğer geliştirme
sunucunuz açık değilse, projenizin ana dizini içerisindeyken şu komutu
verin:
	
	:::terminal
	python manage.py runserver

Bu sizin için [http://localhost:8000](http://localhost:8000) adresinde bir sunucu oluşturacak.
Eğer, o adrese giderseniz, size gittiğiniz adresin tanımladığınız
url'ler içerisinde bulunamadığına dair bir hata verecek. Çünkü, anasayfa
için henüz bir görünüm tanımlamadık. Şimdilik,
`http://localhost:8000/admin` linkinden ulaşabileceğimiz, yönetici
paneline ilerleyelim. Sizden yönetici girişi yapmanızı isteyecek. Admin
veritabanını oluşturuken girdiğiniz kullanıcı adı ve şifresiyle giriş
yapabilirsiniz.

Burada, yönetici sistemine kayıt ettiğiniz uygulamaların yönetimini
yapabilirsiniz. Şu anda Auth ve Sites olarak iki uygulama yüklü olmalı
ve bunlar altında kullanıclar, gruplar, ve siteler ile ilgili yönetim
işlemlerini yapacağınız linkler olmalı. Bu ayarların detaylarına
değinmeyeceğim. Ancak, şu anda gördüğünüz gibi, burada blog uygulamamnız
yok. Önce blog uygulamamızı django'nun admin sistemine kaydetmemiz
gerekiyor. Bunun için, blog uygulaması içerisinde admin isminde bir
model oluşturmalıyız. Uygulamanızın ana dizini (projenin değil,
uygulamanın) içerisinde admin.py isimli boş bir dosya oluşturun. Admin
uygulaması, bizim uygulamamızı kaydetmek için bu dosyanın içeriğini
kullanacak. Şimdi modülümüzü yazmaya başlayalım. Öncelikle modülümüzün
içerisine django'nun admin uygulamasını dahil etmemiz gerekiyor.

	:::python
	from django.contrib import admin

Daha sonra admin sitesine kayıt edeceğimiz modelleri modülümüze dahil
etmeliyiz.

	:::python
	from blog.models import makale, etiket

Artık modellerimizi admin sitesine kayıt edebiliriz. Bunun için
modülümüze dahil ettiğimiz admin paketinin içerisindeki sites modülünde
bulunan AdminSite sınıfının register() metodunu kullanacağız. "admin"
paketini modülümüze dahil ederken, bu paketin \_\_init\_\_ modülü, bizim
için sites.AdminSite'ye işaret eden bir kısayol olarak "site"
değişkenini tanımladı. Bu yüzden kayıt işlemini şu şekilde
gerçekleştirebiliriz.

	:::python
	admin.site.register(makale)
	admin.site.register(etiket)

Burada, *makale* ve *etiket* argümanlarının tırnak içinde olmadığına
dikkat edin. Bu metoda argüman olarak models.Model'den kalıtım alan bir
sınıf vermemiz gerekiyor, bir karakter dizgesi değil.

Artık modellerimiz kullanıma hazır, ancak, geliştirme sunucunuzu yeniden
başlatmanız gerekiyor. Geliştirme sunucunuzu yeniden başlattıktan sonra,
admin sitesine giderek, blog uygulamanıza makale girmeye
başlayabilirsiniz.

Bu yazıyı bitirmeden önce, admin modülüne bir ekleme yapacağız. makale
modelimizdeki slug alanını her seferinde doldurmak sıkıntı verici bir
durum olabilir. Bu yüzden, admin sitesinin slug alanlarını otomatik
olarak doldurmasını isteyeceğiz. Önce kodu görelim, sonra açıklamalarını
yapacağım:

	:::python
	from blog.models import makale, etiket
	from django.contrib import admin

	class MakaleAdmin(admin.ModelAdmin):
		prepopulated_fields = {"slug": ("baslik",)}

	admin.site.register(makale,MakaleAdmin)
	admin.site.register(etiket)

Burada admin paketi/uygulaması içerisindeki ModelAdmin sınıfından
kalıtım alan (php'deki extends gibi) makale adında bir sınıf oluşturduk.
Bu tip sınıfları, modellerimizi admin uygulamasına kaydederken ikinci
bir argüman olarak kullanabiliriz. Bu sınıfın içinde tanımladığımız
özellikler (sınıf özellikleri [eng: class attributes]) modellerimize ait
yönetim panelini daha da özelliştirmeye yarıyor. prepopulated\_fields
özelliğini tanımlarsanız, anahtar-değer ikililerinden anahtardaki alanın
değerini değerdeki tuple'ın her birisine girilen verilere göre admin
paneli bir javascript ile doldurur. Burada, slug alanımız baslik alanına
girilen veriye göre kendiliğinden doldurulacak.

Artık django'nun admin sitesi kullanıma hazır. Bloğumuza makale eklemeye
başlayabiliriz. [Django url ve görünüm](url-mapping-ve-views.html) yazısında
url şemamızı tanımalayacak ve `views` modülü içerisinde birkaç görünüm tanımlayacağız.

  [github deposu]: https://github.com/yasar11732/django-blog