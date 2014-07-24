<!--
.. date: 2011-09-04 21:59:00
.. title: Django'da Sınıf Temelli Genel Görünümler
.. slug: djangoda-sinif-temelli-genel-gorunumler
.. description: Django'da view'ler bir fonksiyon olabileceği gibi, bir sınıf da olabilir. Sınıf olan view'lerin nasıl kullanıldığı ve bunları faydaları hakkında bir yazı.
-->

Django'da geliştirirken, ister istemez genel görünümlere dokunuyoruz.
Son günlerde, [django gezegeninde][] ve mail gruplarında, sınıf temelli
görünümlerden bahsedildiğini gördüm, ancak, bunların nasıl kullanılacağı
hakkındaki bilgim yok denecek kadar azdı. Bu yüzden, Django belgelerine
biraz göz attım, ve etkin kullanıldığında, sınıf temelli görünümlerin,
çok verimli olabileceği kanısına vardım. Şimdilik yüzeysel olarak,
örnekler ve kısa açıklamalar yazmak istedim, kendimi bu konuda
geliştirirsem, ileride daha derin olarak inceleyebilirim bunları. <!-- TEASER_END -->

### Şablonlar

    :::python
    # uygulamam/views.py
    from django.views.generic import TemplateView
    
    class Hakkimda(TemplateView):
        template_name = "hakkimda.html"

Django'nun genel görünümlerinden TemplateView, bir şablonu olduğu gibi
tarayıca göndermeye yarıyor. Burada, Hakkimda isimli sınıf temelli bir
görünümü, TemplateView'den türetip, template\_name değişkeninin, yani
şablon adını belirleyen değişkenin, üstüne yazdık. Böylece, tarayıcıya
hakkimda.html şablonunu gönderen bir görünümü hızlıca yazdık. Şüphesiz
ki bu, baştan bir görünüm yazmaktan daha hızlıdır. Bu sınıfı, bir url
ile eşleştirmek için, urls.py içerisinde gerekli ayarları yapmamız
gerek.

    :::python
    # urls.py
    from django.conf.urls.defaults import *
    from uygulamam.views import Hakkimda
    
    urlpatterns = patterns('',
        (r'^hakkimda/', Hakkimda.as_view()),
    )

Hakkimda, bir sınıftır, url ile eşleştirdiğimiz ise, bu sınıfın as\_view
metodunun döndürdüğü görünüm fonksiyonu. Anlaşılan, sınıf temelli
görünümlerin kendileri aslında görünüm değiller. Gerekli görünüm
fonksiyonlarını, sınıfın as\_view metodundan alıyoruz. Ayrıca, buradaki
gibi, sadece tek bir özelliğin üstüne yazılması gereken durumlarda, bunu
yeni bir sınıf türetmeden, hemen urls.py içerisinden de yapabiliriz.

    :::python
    # urls.py
    from django.conf.urls.defaults import *
    from django.views.generic import TemplateView
    
    urlpatterns = patterns('',
        (r'^hakkimda/', TemplateView.as_view(template_name="hakkimda.html")),
    )

### Objelerin Genel Görünümleri

Bu kısımda yapacağım örneklerde, aşağıdaki iki modeli kullanacağım.

    :::python
    class Tag(models.Model):
        text = models.CharField(max_length=15, unique=True)
        slug = models.SlugField(blank=True)
        created = models.DateTimeField(default=datetime.now)
    
    class Post(models.Model):
        title = models.CharField(max_length=100)
        slug = models.SlugField(unique=True)
        abstract = models.TextField(max_length=500)
        post = models.TextField()
        pub_date = models.DateTimeField("Date Published", default=datetime.now)
        last_mod = models.DateTimeField(auto_now=True)
        tags = models.ManyToManyField(Tag,blank=True)
        yayinlandi = models.BooleanField(default=False)

Tüm Tag'ların listesini almak için:

    :::python
    from django.conf.urls.defaults import *
    from django.views.generic import ListView
    from blog.models import Tag
    
    urlpatterns = patterns('',
        (r'^tags/$', ListView.as_view(
            model=Tag,
        )),
    )

Şimdi de bir şablon oluşturmamız gerekiyor. Url yapılandırmasında
template\_name ile bir şablon adı belirtmediğimiz için, django
tag\_list.html isimli bir şablon arayacak. tag kısmı, model adının küçük
harfe dönüştürülmesiyle elde edilirken, \_list.html kısmı, hep eklenen
bir sonek. Bu tag\_list.html, TEMPLATE\_LOADERS ile settings.py'de
belirttiğiniz, şablon bulucular tarafından aranıp bulunmaya çalışılacak.
Eğer bu listede "django.template.loaders.app\_directories.Loader" varsa,
uygulama dizini içerisinde, templates isimli bir klasörde bu şablon
bulunabilir. Ya da, "django.template.loaders.filesystem.Loader" varsa, o
zaman TEMPLATE\_DIRS ile belirttiğiniz dosya yollarından herhangi
birisinde durabilir. Bu kısmı daha fazla uzatmadan, kısaca bu şablonunun
nasıl olacağına değineyim.

    :::html
    ... Şablonun yukarıları burada ...
    {% for tag in object_list %}
         {{ tag.text }}
    {% endfor %}
    ... Şablonun devamı burada...

Bu şablondaki object\_list içeriği (ing: Context Variable) ListView
objesi tarafından gönderildi. Bu değişkenin adını, daha önce
TemplateView'da şablon adının üstüne yazdığımız gibi
değiştirebilirsiniz. Bunun için, context\_object\_name değişkenine,
şablondan ulaşmak istediğiniz değişken adını verebilirsiniz.

#### Şablona Ek İçerik Gönderme

    :::python
    from django.views.generic import DetailView
    from blog.models import Tag, Post
    
    class PostDetailView(DetailView):
    
        context_object_name = "post"
        model = Post
    
        def get_context_data(self, **kwargs):
            # Şablon içeriğini ebeveyn metottan alacağız.
            context = super(PostDetailView, self).get_context_data(**kwargs)
            # Bütün tagları da şablon'a gönderelim!
            context['taglar'] = Tag.objects.all()
            return context

Şablona gönderilecek içerik, get\_context\_data metodundan döndürülüyor.
Bu metodun üzerine yazarak, şablona istediğimiz içeriği
gönderebiliyoruz.

#### Objelerin Alt Kümesi

Çoğu zaman ListView ile çalışırken, bir modeldeki bütün objelerle değil,
bu objelerin bir alt kümesiyle çalışmak isteyeceksiniz. Üstünde çalışmak
istediğiniz objeleri, statik olarak queryset değişkeniyle veya dinamik
olarak get\_queryset metodunun üzerine yazarak belirleyebilirsiniz.

    :::python
    from django.views.generic import ListView
    from blog.models import Post
    
    class PostListView(ListView):
    
        context_object_name = "publisher"
        queryset = Post.objects.filter(yayinlandi=True).order_by("-pub_date")

Dinamik olarak QuerySet'i ayarlamak için, Url bilgisinden gelen
değişkenleri kullanacağız. Bunlara, self.args, self.kwargs ve
self.request üzerinden ulaşabiliyoruz.

    :::python
    from blog.views import TagListView
    
    urlpatterns = patterns('',
        (r'^tag/(?P\w+)/$', TagListView.as_view()),
    )

    :::python
    from django.views.generic import ListView
    from blog.models import Tag
    from django.shortcuts import get_object_or_404
    
    class TagListView(ListView):
        def get_queryset(self):
            # self.tag diyerek, bunu sınıf örneğine ait bir değişken yapabiliriz.
            self.tag = get_object_or_404(Tag,slug=self.kwargs["slug"])
            return self.tag.post_set.filter(yayinlandi = True)
        def get_context_data(self,**kwargs):
            # queryset alınırken, self.tag oluşturuldu, şimdi istersek onu da şablon'a gönderebiliriz.
            context = super(TagListView,self).get_context_data(**kwargs)
            context["tag"] = self.tag
            return context
        

Basit olarak, bu kadar bilgi konuya giriş yapmak için yeterli olacaktır
diye düşünüyorum. Bunlara ek olarak, mixin'ler var. Bunlar, biraz daha
gelişmiş bir konu olduğu için, biraz daha detaylı öğrenip, onlara başlı
başına bir yazı yazmak istiyorum.

İyi Geliştirmeler.

  [django gezegeninde]: http://planetdjango.org/ "Django Gezegeni"