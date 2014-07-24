<!--
.. date: 2011-08-27 12:19:00
.. description: Django veritabanında özet veri elde etmek için annotate ve aggregate fonksiyonları kullanılıyor. Bu fonksiyonlar ile, satırların ortalaması, toplamı gibi tanımlayıcı istatistikler alınabilir.
.. title: Django'da Aggregate ve Annotate
.. slug: djangoda-aggregate-and-annotate
-->


Django veritabanı yönetiminde annotate() ve aggregate()
kullanarak,satırların toplamı, ortalaması gibi, veritabanında birden çok
satırdan veya ilgili diğer tablolardan bilgi toplayarak bulunması
gereken değerleri bulabilirsiniz. annotate() ve aggregate() metodlarının
farkı, aggregate'in tüm tablo için tek bir sonuç döndürmesi, annotate'in
ise veritabanındaki tüm satırlar için ayrı birer değer oluşturmasıdır.
Bu yazıda kısaca Django'da annotate ve aggreate kullanımı ile ilgili
örnekler göstereceğim.

Burada anlatılanlar kısaca django'da annotate ve aggregate nasıl
kullanılır konusuna giriş yapmak içindir, daha fazlasını django
belgelerinde [aggregate][] ile ilgili bölümden bulabilirsiniz. <!-- TEASER_END -->

### Tablo alanlarının ortalaması

    :::python
    ###
    # models.py
    ###
    
    from django.db import models
    
    class Urun(models.Model):
        fiyat = models.PositiveIntegerField()
    
    ###
    # Tüm ürünlere ait ortalama fiyatları almak istediğinizde
    ###
    from uygulama_adi.models import Urun
    from django.db import Avg
    
    a = Urun.objects.aggregate(Avg('fiyat'))
    
    # a = {"fiyat__avg": 23.56} -> bir dict objesi döndürür.
    # Dönen sözlükteki anahtar adını da ayarlayabilirsiniz.
    
    a = Urun.objects.aggregate(ortalama_fiyat=Avg('fiyat'))
    
    # a = {"ortalama_fiyat": 23.56}
    
    ##
    # Birden fazla değer hesaplamak
    ##
    from django.db.models import Max, Min
    a = Urun.objects.aggregate(Ortfiyat=Avg('fiyat'),Minfiyat=Min('fiyat'),maksfiyat=Max('fiyat'))
    
    # a = {"Ortfiyat" : 15.23, "Minfiyat": 3, "Maxfiyat" : 28}

### Django'da annotate kullanımı

Bir istem kümesindeki (QuerySet) tüm değerler için aggregate almak için
annotate kullanılır. Çoğu zaman annotate m2m (çokdan çoğa) ilişkilerde
kullanılır.

    :::python
    ###
    # models.py
    ###
    from django.db import models
    
    class Etiket(models.Model):
        yazi = models.CharField(max_length=60)
    class Makale(models.Model):
        etiketler = models.ManyToManyField(Etiket, blank=True)
    
    ### model.py sonu ###
    
    # Her etiket için kaç makale var
    
    from uygulamam.models import Etiket
    from django.db.models import Count
    
    a = Etiket.objects.annotate(makale_sayisi=Count('makale'))
    
    # a değişkeni Etiket.objects.all() gibi, ancak her elemanın artık makale_sayisi diye bir özelliği var,
    # örneğin: a[0].makale_sayisi ilk sıradaki etikete ait kaç adet makale olduğunu verir.
    # aynı zamanda bir etikete ait diğer tüm özellikler de her bir elemanda mevcuttur.

### Alakalı tablo sütünları

Django'daki çift alt tire gösterimini, annotate ve aggregate için
kullanabilirsiniz.

    :::python
    # gerekli import'lar yapılmış sayın
    
    """
    Bu örnekteki uygulama, aynı site içerisinde birden fazla blog tutuyor.
    Her makale bir blog'a ilişkilendirilmiş
    """
    class Blog(models.Model):
        # bir iki alan tanımı var burda
    
    class Makale(models.Model):
        blog = models.ForeignKey(Blog,related_name="makaleler")
        begeni_yuzdesi = models.DecimalField()
    
    ###
    # Her blog için, en az beğenilen makalelerin ne kadar begeni_yuzdesi aldığı!
    ###
    from django.models import Min
    a = Blog.objects.annotate(en_az_begeni = Min('makaleler__begeni_yuzdesi'))
    
    # a değişkeni tüm blogların bir listesini tutuyor. a'nın her elemanının en_az_begeni diye bir
    # özelliği var ve bu özellik o blog'daki tüm makeler içerisinde en az beğenilen makalenin
    # begeni yüzdesini tutuyor.

### İstem (Query) metotlarını zincirlememek

Django'da aggregate() ve annotate() metodları, Django veritabanı
apisindeki filter, exclude gibi diğer istem metotlarıyla
zicirleyebilirsiniz. Ancak aggregate() her zaman en son metot olmak
zorunda. annotate'in ise zincirlemedeki yerine göre, istem kümesinin
elemanları değişiyor.

    :::python
    Makale.objects.filter(yayinlandi=True).aggregate(ortalama_begeni = Avg("begeni_yuzdesi"))
    # Yayınlanan makalelerin ortalama beğeni yüzdesini döndürür : {"ortalama_begeni": 93.21}
    
    Blog.objects.annotate(makale_sayisi = Count("makaleler")).order_by("-makale_sayisi")
    
    # annotate ile eklediğimiz makale_sayisi özelliğini Blog'ları sıralamak için kullanıyoruz.

  [aggregate]: https://docs.djangoproject.com/en/dev/topics/db/aggregation/