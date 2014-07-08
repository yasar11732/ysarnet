<!--
.. date: 2011-08-09 00:35:00
.. description: Django uygulamanızın url yapısını, 301 yönlendirmesi kullanarak değiştirebilirsiniz. Böylece, arama motoru görünürlülüğünüzü artırabilirsiniz.
.. slug: django-301-redirect
.. title: Django'da Url Taşıma
-->

Bu yazıda, eski ziyaretçileri ve arama motorlarını küstürmeden,
django'da nasıl url taşıyacağımıza değineceğiz. <!-- TEASER_END -->

Örneğin, bir bloğunuz var (evet, örnek pek yaratıcı değil...) ve
makale/14 (id'si 14 olan makalenin url'i) gibi urlleri topluca, yazi/14
gibi url'lere taşımak istiyorsunuz. Bunu Django'nun generic view'leri
ile kolaylıkla yapabiliriz. Örneğin: <!-- TEASER_END -->

	:::python
	from django.conf.urls.defaults import patterns
	urlpatterns = patterns('',
	  (r'^makale/(?P<id>\d+)/$','blog.views.makale'),
	)

Şimdi de urlleri taşıdığımız haline bakalım:

	:::python
	from django.conf.urls.defaults import patterns
	from django.views.generic.simple import redirect_to
	urlpatterns = patterns('',
		(r'^makale/(?P<id>\d+)/$',redirect_to,{'url': 'yazi/%(id)s/'}),
		(r'^yazi/(?P<id>\d+)/$','blog.views.makale')

Bu çok basit bir örnekti. Eski bağlantımıza gelen kullanıcıları, yeni
bağlantımıza yönlendirdik. Burada %(id)s kısmı, django'nun bizim için
yaptığı sözlük biçiminde dizgi formatlaması (eng: dictionary-style
string formatting). Böylece bize gelen url'deki id değerini, aynı
şekilde yönlendirdiğimiz url içerisine koyuyoruz.

Peki ama, ya sitemizin /makale/\<id\> olan url'ini makale/\<slug\> gibi
bir url'e yönlerdirmek istiyorsak? Bunu yapabilmek için bir view yazıp,
yönlendirmeyi orada yapmalıyız. Bunu herhangi bir modül içerisinde
yapabiliriz. Ben uygulamanın kendi views modülü içerinde yapacağım.

	:::python
	from django.http import HttpResponsePermanentRedirect
	from django.shortcuts import get_object_or_404
	from blog.models import makale #makale modelinin orada olduğunu varsayıyorum.

	def makeMeSEO(request,makale_id):
		mkl = get_object_or_404(makale,pk=makale_id)
		return HttpResponsePermanentRedirect("/makale/%s/" % mkl.slug)

	"""
	Diğer fonksiyonlar burada devam ediyor.
	"""

Burası da urls.py

	:::python
	from django.conf.urls.defaults import patterns
	from django.views.generic.simple import redirect_to

	urlpatterns = patterns('',
		(r'^makale/(?P<id>\d+)/$','blog.views.makeMESEO'),
		(r'^makale/(?P<slug>[^/]+)/$),'blog.views.makale')

Böylelikle, id'ye dayalı eski url sistemimizi, slug alanına dayalı yeni
bir url sistemine dönüştürdük. Ancak bu dönüşümün şöyle eksik bir yanı
var ki, slug alanı sadece rakamlardan oluşan bir makale varsa,
yaptığımız yönlendirme bu makaleye giden linkleri id'si o rakam olan
url'e yönlendirecek. Bu durumun üstesinden gelmek için iki farklı yöntem
kullanabiliriz. Bu yöntemlerden ilki, yönlendirme sonucunda ulaşılan
url'i yönlendirmeden önceki bir url'le karışmayacak şekilde ayarlamak:

	:::python
	from django.conf.urls.defaults import patterns
	from django.views.generic.simple import redirect_to

	urlpatterns = patterns('',
		(r'^makale/(?P<id>\d+)/$','blog.views.makeMESEO'),
		(r'^slug_alanina_gore_makale/(?P<slug>[^/]+)/$),'blog.views.makale')

Böylece, url yapılandırmamız hangi url'i yönlendirmeye çalışacağına daha
doğru bir şekilde karar verebilir. Bir diğer yöntem de, yönlendirmeyi
yapan fonksiyonda url'in yönlendirilmesi gerekip gerekmediğinin
kontrolünü yapmak. Bunun yapılışı tamamen geliştirilen proje ve
uygulamaya bağlı bir durum olduğu için, burada bir örnek yapmayıp, bunu
uygulama geliştiricilerinin hayal gücüne bırakmak istiyorum.

Son bir not olarak, url taşırken dairesel yönlendirme yapmamaya dikkat
edin. Yaptığınız yönledirmelerin hiçbir şekilde yönledirmeden önceki
haline dönmemesi gerek. Bunun için şöyle basit birşey yapabilirsiniz.

	:::python
	def makeMeSEO(request,makale_id):
		mkl = get_object_or_404(makale,pk=makale_id)
		redirect_link = "/makale/%s/" % mkl.slug
		if redirect_link != request.path:
			return HttpResponsePermanentRedirect("/makale/%s/" % mkl.slug)
		else:
			raise Http404

Burada biraz basite kaçıp, yönlendirilmiş ve yönlendirilmemiş urller
aynı olduğu zaman 404 bulunamadı hatası döndürdüm. Bunun yerine daha
yaratıcı şeyler bulmayı da okuyucuya bırakıyorum.