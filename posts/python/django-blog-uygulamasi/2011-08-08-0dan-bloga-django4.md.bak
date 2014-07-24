<!--
.. date: 2011-08-08 18:07:00
.. description: Django'da url yapıları nasıl düzenlenir? Django uygulamarınızın herbiri kendi url şemasını belirler. Site çapındaki url ayarları bunları bir araya getirir.
.. slug: url-mapping-ve-views
.. title: Django ile Blog Geliştirme - Url ve Görünüm
-->

[Django Yönetici Paneli](yonetici-paneli.html) yazısında blog uygulamamızı
django yönetici paneline eklemiştik. Bu yazıda ise, blog uygulamamızın url
yapılandırmasını yapacak ve tarayıcıya bazı statik ve dinamik yazılar
göndereceğiz. Django'nun şablon sistemine ise bir sonraki dersimizde değineceğiz. <!-- TEASER_END -->

Bu yazı dizisinde bahsedilen blog uygulamasının son haline [github
deposu][]ndan ulaşabilirsiniz.

Django'nun url yapılandırması, herhangi bir python modülü içerisinde
yapılabilir. Bununla birlikte, url yapılandırması yaptığımız modülün
içerisine diğer uygulamaların da url yapılandırmasını dahil edebiliriz.
Django projeleri geliştirirken tavsiye edilen yöntem, her uygulamanın
kendi url yapılandırmasını yapması, ve bu yapılandırmaların kök
dizindeki urls modülüne dahil edilmesidir. Böylece django
uygulamalarının ayrıştırılması sağlanmış olur. Bu ayrıştırma sayesinde
bir projede geliştirdiğimiz uygulamayı, istersek kolaylıkla dağıtabilir,
istersek diğer projelerimize dahil edebiliriz.

Yeni başladığımız projemizin kök dizininde bulunan urls modülünün
sıradan bir python modülünden bir farkı yoktur. Sadece, urlpatterns
isminde bir *patterns* objesi tanımlaması gerekir. Bunun için öncelikle,
django.conf.urls.defaults içerisinde bulunan patterns'ı bu modüle dahil
etmemiz gerekir. Yeni oluşturulan projemizde bu işlem django tarafından
yapılmıştır. Bununla birlikte örnek bir urlpatterns objesi de
tanımlanmıştır. Geçen dersimizde django'nun içerisinde gelen admin
uygulamasında tanımlanan url'leri, buraya dahil etmiştik. Şimdi de blog
projemize ait url yapılandırmasını buraya ekleyelim.

	:::python
	from django.conf.urls.defaults import patterns, include, url
	from django.contrib import admin
	admin.autodiscover()
	 
	urlpatterns = patterns('',
		url(r'^admin/', include(admin.site.urls)),
		url(r'^blog/',include('blog.urls'))
	)

Buradaki `r'\^blog/'` bir düzenli ifadedir. Eğer düzenli ifadeleri
bilmiyorsanız, Django ile url yapılandırması yapmadan önce düzenli
ifadeler hakkında en azından temel bilgiye sahip olmanız gerekir.
Burada, düzenli ifadeler üzerinde fazla durmayacağım, çünkü buraya
sığamayacak kadar uzun bir konu. Örneğimizdeki ilk "\^" (şapka işareti)
düzenli ifadelerde satır başına işaret eder. Burada, satır başında
(sitemizin adından sonra) blog/ olan url'ler için, blog.urls içinde
tanımlanan url yapılandırmasını kullanmasını istedik.

Uygulamamızın url yapılandırmasını, kök url yapılandırmasına eklemiş
olmamıza rağmen, uygulamamız henüz bir url tanımlaması yapmıyor.
Uygulamanızın ana dizini içerisindeyken (projenin değil dikkat edin.
blog dizini içinde) urls.py adında boş bir dosya oluşturun ve içine
şunları girin:

	:::python
	from django.conf.urls.defaults import patterns
	urlpatterns = patterns('blog.views',
	  (r'^$', 'anasayfaView'),
		(r'^makaleler/(?P<slug>[^/]+)/$','makaleView'),
	)

Burada iki adet url tanımlaması yaptık. İlk url'imiz `^$`. Şapka
işaretinin satır başı anlamına geldiğini söylemiştik. Dolar işareti ise
satır sonu anlamına gelir. Bunları bu şekilde yanyana kullanmak, boş biz
dizgeyi ifade eder. Bu url yapılandırmasında, django url olarak boş bir
dizge görürse, bizim için blog.views içerisindeki anasayfa fonksiyonunu
çağıracak. Oraya daha sonra geleceğiz. İkinci url tanımlamamız biraz
daha karışık. Burada satır başını `makaleler/` ile takip etmesini
söylüyoruz. Bundan sonra yazdığımız parentez içerisindeki alan bir
değişken tanımlıyor. Django bu değişkeni bizim için çağıracağımız
fonksiyona argüman olarak gönderecek. ?P kısmı, değişken tanımladığımızı
söylerken, `<...>` içerisindeki şey ise değişkenimizin adı. Değişkenin
adından sonra yazdığımız `[^/]+` yine bir düzenli ifade. Bu düzenli ifade
"/" haricinde bir veya birden fazla karakter anlamına geliyor. Url
tanımlamamızın geri kalanı ise, düzenli ifadenin devamı. Burada
tanımladığımız url'i şöyle özetleyebiliriz. `makaleler/` den sonra `/`
haricinde bir veya birden fazla karakter devam etsin sonra bir `/`
gelsin ve url tamamlansın. Burada iki `/` arasında kalan yazı dizgesi de
fonksiyona argüman olarak verilecek.

Bu url tanımlamalarını yaptıktan sonra, views içerisinde anasayfa ve
makale adındaki fonksiyonları tanımlamamız gerekiyor. Bu fonksiyonların
ilk argümanı her zaman django'nun request objesi olacak. request
objesinin detaylarına şu anda değinmeyeceğim, o kendi başına bir
makaleyi hak eden bir konu. Şimdilik ilk argümanın request objesi
olduğunu bilmemiz yeterli. Diğer argümanlar ise, url tanımlarken
belirttiğimiz argümanlar. Ayrıca burada tanımladığımız fonksiyonların
HttpResponse objesi döndürmek, başka bir url'e yönledirme yapmak veya
404 bulunamadı hatası vermek gibi, birkaç şeyden birini yapması
gerekiyor. Örneğin tarayıca bir yanıt gönderelim. Bunun için
fonksiyonumuzdan Django'nun HttpResponse objesini döndüreceğiz.

	:::python
	# -*- coding:utf-8 -*-
	from django.http import HttpResponse

	def anasayfaView(request):
		return HttpResponse("<h1>Burası anasayfa :)</h1>")

Şu anda eğer bir şeyi atlamadıysak, http://localhost:8000/blog adresine
gittiğinizde, kocaman bir "Burası anasayfa :)" yazısı görmeniz
gerekiyor.

Şimdi biraz daha gelişmiş bir örnek yapalım. makale fonksiyonu
içerisinde, bizden istenen makaleyi bulup, tarayıcıya gönderelim.

	:::python
	from django.http import HttpResponse
	from blog.models import makale

	def makaleView(request, slug):
		mkl = makale.objects.filter(slug=slug)[0]
		return HttpResponse(mkl.makale)

Artık, `http://localhost:8000/makale/cok-onemli-makale` adresine
gittiğinizde size, slug alanı cok-onemli-makale olan makaleyi bulup
getirecektir. Peki ama ya böyle bir makale yoksa?

	:::python
	from django.http import HttpResponse, Http404
	from blog.models import makale
	def makaleView(request, slug):
		mkl_query = makale.objects.filter(slug=slug)
		if len(mkl_query) > 0:
			mkl = mkl_query[0]
			return HttpResponse(mkl.makale)
		else:
			raise Http404

Artık makale bulunamadığında tarayıcıya bir 404 bulunamadı mesajı
göndereceğiz. Şu anda debug mod açık olduğu için bunu göremiyoruz, ancak
settings içerisindeki debug değişkenini False yaparsak 404 mesajını
görebiliriz. Ancak bunun için daha erken, şimdilik öyle kalsın.

Objenin gerçekten var olup olmadığını kontrol etmek ve buna göre bir 404
hatası göndermek doğru bir yöntem olsa da, her seferinde bunu yapmak
vakit kaybı, ve biz bunu istemiyoruz. Django bunun için bize bir kısayol
sağlıyor. Örneğimize tekrar bakalım:

:::python
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from blog.models import makale
def makaleView(request, slug):
    mkl = get_object_or_404(makale, slug=slug)
    return HttpResponse(mkl.makale)
Bu yazımızda, url tanımlamaya ve tarayıcıya basit statik veya dinamik
içerikler göndermeye çalıştık. Ancak, view fonksiyonlarının içerisinden
tarayıcıya doğrudan veri göndermek çok doğru bir geliştici davranışı
sayılmaz. [Django Şablonları](template.html) yazısında django şablon moturunu
kullanarak html oluşturma konusuna değineceğiz.

  [github deposu]: https://github.com/yasar11732/django-blog