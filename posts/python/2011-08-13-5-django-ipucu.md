<!--
.. date: 2011-08-13 14:00:00
.. description: Django'da veritabanı, admin paneli, gzip ve önbellek gibi konularda, işinizi kolaylaştıracak 5 ipucuyu bu yazıda bulabilirsiniz.
.. slug: 5-django-ipucu
.. title: 5 Django İpucu
-->


Başlangıç seviyesindeki anlatımlarda çok sık karşılaşamayacağınız,
ancak, Django ile uygulama geliştirirken işinize yarayacak 5 ipucunu
sizlerle paylaşmak istedim. <!-- TEASER_END -->

Veritabanına Başlangıç Verisi Yüklemek
--------------------------------------

Geliştirme aşamasında sık sık veritabanını baştan başlatıyorsanız, veya
uygulamanızın çalışması için, kurulumdan sonra bazı verilerin
veritabanına yazılması gerekiyorsa, bu ipucu sizin için. Uygulamanızın
içinde açacağınız "fixtures" dizininin içerisinde, initial\_data.[xml,
json veya yaml] isimli belgede, syncdb komutuyla birlikte veritabanına
yazılacak verileri belirleyebilirsiniz. initial\_data.json örneği
aşağıda.

	:::json
	[
	  {
		"model": "blog.Setting",
		"pk": 1,
		"fields": {
		  "anahtar": "blog_baslik",
		  "deger": "Blog Title Goes Here!"
		}
	  },
	  {
		"model": "blog.Setting",
		"pk": 2,
		"fields": {
		  "anahtar": "blog_slogan",
		  "deger": "Slogan Goes Here!"
		}
	  }
	]

Admin panelinde, sadece okunabilen alanlar
------------------------------------------

Eğer modelinizdeki bazı alanların admin panelinde görünmesini istiyor,
ancak, o alanların düzenlenebilir olmasını istemiyorsanız, bunu
readonly\_fields ile belirtebilirsiniz.

	:::python
	class PostAdmin(admin.ModelAdmin):
		readonly_fields = ("slug","last_mod","pub_date")
	admin.site.register(Post,PostAdmin)

Admin panelinde göstermeden alan doldurmak
------------------------------------------

Modelinize ait bazı alanları, admin panelinde göstermeden, programatik
olarak doldurabilirsiniz. Admin paneli, modelleri kaydetmek için,
ModelAdmin sınıfının, save\_model sınıfını kullanıyor. Bu metodun üstüne
yazabilirsiniz.

	:::python
	class PostAdmin(admin.ModelAdmin):
		# excludes içindeki alanlar admin panelinde görünmezler.
		excludes = ("author",)
		
		def save_model(self,request,obj,form,change):
			# change False ise, ilk kez oluşturuluyordur.
			if not change:
				obj.author = request.user
			obj.save()

Gzip sıkıştırması
-----------------

Görünümlerinize ekleyeceğiniz bir dekoratör ile görünümün tarayıcıya
gönderilmeden önce gzip formatında sıkıştırılmasını sağlayabilirsiniz.

	:::python
	from django.views.decorators.gzip import gzip_page
	from django.shortcuts import render_to_response
	@gzip_page
	def homepage(request):
		return render_to_response("blog/index.html")
		
Sayfalarınızı Önbelleğe Alın
----------------------------

Django, birçok farklı önbellek yöntemini desktekliyor, bunlardan
kullanması en kolay olanı muhtemelen bilgisayarın belleğinde önbellek
oluşturmak. Aşağıdaki ayarı settings modülüne ekleyerek, django'nun
bilgisayar belleğinde bir önbellek oluşturmasını sağlayabilirsiniz.

	:::python
	CACHES = {
		'default' : {
			'BACKEND' : 'django.core.cache.backends.locmem.LocMemCache',
		}

	}

Önbellek backend'ini (tr'de tam bir karşılığı yok galiba, sunucu
uygulama diye çevirmişler) ve belirtip ayarlarını yaptıktan sonra, tüm
sitede önbelleklemeyi aktifleştirmek için gerekli middleware (ara
yazılım?) sınıflarını ve birkaç diğer ayarı da ayarlamanız gerekiyor.

	:::python
	CACHE_MIDDLEWARE_ALIAS = "falan" # Önbellek takma adı
	CACHE_MIDDLEWARE_SECONDS = "900" # önbellek ne kadar süre aktif, saniye cinsinden
	CACHE_MIDDLEWARE_KEY_PREFIX = "" # bu sitede kullanılmak üzere bir önek, eğer tek bir site varsa boş kalabilir.
	MIDDLEWARE_CLASSES = (
		'django.middleware.cache.UpdateCacheMiddleware',
		'django.middleware.common.CommonMiddleware',
		'django.middleware.cache.FetchFromCacheMiddleware',
	)


`UpdateCacheMiddleware` sınıfı her zaman ilk, `FetchFromCacheMiddleware` her
zaman son sırada olmalı, bunun nedeni biraz gereksiz detay olur,
[Django belgeri](https://docs.djangoproject.com/en/dev/topics/cache/?from=olddocs#order-of-middleware-classes "django cache framework") bu konuya değinmiş.

Tüm sitede değil de sadece bazı sayfalarda önbellekleme isteyenler de
[cache decorator] kullanarak önbellekleme işlemini yapabilir. Dekoratöre
verilen argüman, bu önbelleğin ne kadar süre boyunca aktif kalacağını
ayarlıyor.

	:::python
	from django.views.decorators.cache import cache_page

	@cache_page(60 * 15)
	def my_view(request):
		...
Son olarak şunu belirtmek istiyorum ki, buradaki ipuçlarının Django'ya
yeni başlayanlara yönelik olmasını hedefledim. Bu nedenle, örnekleri en
basit şeklinde vermeye çalıştım. Bu sebeple, bu yöntemler son kullanım
için uygun olmayabilir.

  [cache decorator]: https://docs.djangoproject.com/en/dev/topics/cache/?from=olddocs#the-per-view-cache
    "django per view cache decorator"