<!--
.. date: 2011/08/09 17:30:00
.. description: Bu yazıda Django'daki şablon (template) dili anlatılıyor. Örnekler aracılığıyla, gerekli dosyalar ve ayarlar gösteriliyor.
.. slug: template
.. title: Django ile Blog Geliştirme - Şablonlar
-->

[Django url ve görünüm](url-mapping-ve-views.html) yazısında
url şemamızı tanımalamış ve `views` modülü içerisinde birkaç görünüm tanımlamıştık.
Bu yazımızda, Django'nun şablon sistemini kullanarak,
uygulamalarımızı son kullanıcıya daha zarif bir şekilde sunmanın
yollarından bahsedeceğiz. <!-- TEASER_END -->

Bu yazı dizisinde bahsedilen blog uygulamasının son haline [github
deposu][]ndan ulaşabilirsiniz.

Django'da şablon oluşturma işlemi, içeriğinin belirli kısımları Django
tarafından doldurulacak şekilde bir belge oluşturmaktan ibarettir. Çoğu
zaman bu sistem HTML sayfaları üretmek için kullanılsa da, Django'nun
şablon sistemiyle javascript, css, xml belgeri gibi her türlü belgeyi
betimleyip tarayıcıya gönderebilirsiniz.

Hazırladığımız şablonların Django tarafından bulunabilmesi için,
settings modülü içerisindeki `TEMPLATE_LOADERS` listesinde bulunan şablon
bulucu python sınıfları kullanılır. Yeni başlanan bir proje
yapılandırmasında, iki adet şablon bulucu sınıf aktif olarak gelir.
Bunlardan birtanesi `django.template.loaders.filesystem.Loader`'dir.
Django'nun şablon sisteminin bir parçası olan bu sınıf, şablonlarınızın
yerini belirlemek için, yine settings modülü içerisinde belirttiğiniz
`TEMPLATE_DIRS` listesindeki dosya yollarında şablonlarınızı bulmaya
çalışır. Django'yla birlikte gelen ve öntanımlı olarak ayarların
içerisinde belirtilen diğer bir şablon bulucu ise
`django.template.loaders.app_directories.Loader`'dir. Bu sınıfın görevi
ise, `INSTALLED_APPS` listesinde belirttiğiniz uygulamaların içerisindeki
templates ismindeki dizinlerden aradığınız şablonları bulmaktır.

Django'da geliştirdiğiniz uygulamaların yeniden kullanılabilir olması
adına, uygulamaların kendi şablonlarını kendi içlerinde barındırması
gerekir. Böylece, başka bir proje içine kopyalandıklarında, yeni projede
yeniden şablon geliştirilmek zorunda kalınmaz. Bunu yapmak için,
geliştirdiğimiz proje içerisinde, templates adında bir dizin oluşturup,
içerisinde `blog_anasayfa.html` adında bir dosya oluşturalım. Dosya
uzantısını html olarak seçmemin nedeni, bazı metin düzenleme
programlarının dosya uzantısına göre kod renklendirme ve tamamlama gibi
işlevler sağlaması. Django açısından bir şablonun uzantısının hiçbir
önemi yok. Dosya adının başına `blog_` öneki getirmemin sebebi ise, diğer
uygulamaların şablonlarıyla blog uygulamasının şablonlarının karışmasını
önlemek. Şimdilik oluşturduğunuz dosya içerisinde basit birkaç html kodu
yazabilirsiniz, nasıl çalıştığını gördükten sonra asıl işimize
başlayacağız.

Django'da şablonların yüklenmesi, views modülü içerisinde yapılır.
Aşağıdaki örnekte bir şablonu derleyip (henüz içerisinde derlenecek
birşey olmasa da) tarayıcıya göndereceğiz.

	:::python
	from django.template import Context, loader
	from blog.models import makale
	from django.http import HttpResponse

	def anasayfaView(request):
		sablon = loader.get_template('blog_index.html')
		icerik = Context()
		yanit = sablon.render(icerik)
		return HttpResponse(yanit)



Django'da şablon kullanmak için yapılacak ilk iş, şablonun yüklenip bir
değişkene atanmasıdır. Bunu yukarıdaki örneğin 6. satırında yaptık.
Ancak, django'nun şablonumuzu işleyebilmesi için, ona bir içerik
vermemiz gerekiyor. Verdiğimiz içerik, django'nun içindeki template
modülünde tanımlanan BaseContext sınıfının herhangi bir alt sınıfı
olabilir. Burada, Context sınıfını kullanıyorum. Bu sınıfı oluştururken
herhangi bir argüman kullanmadım, çünkü şu anda şablonumuzun işlenmesi
için herhangi bir içeriğe ihtiyacı yok, basit bir html sayfası. Bunu da
yaptıktan sonra, 8. satırda, bir önceki satırda tanımlamış olduğum
içeriği kullanarak, sablonu derleyip bir değişkene atıyorum. Sonra
olarak da, derlemiş olduğum şablonu, tarayıcıya gönderiyorum.

Django şablonlarını daha dinamik olarak kullanmak için, bu şablonların
içerisinde, şablon etiketleri, filtreler ve değişkenler kullanıp,
şablonumuza bunlarla birlikte derlememiz gerekiyor. Basit bir değişken
örneğiyle başlayalım. Bu örnek şablonumuz:

	:::html
	<html>
	  <head>
		<title>{{ baslik }}</title>
	  </head>
	</html>
Burada şablon içerisinde `baslik` adında bir değişken tanımladık.
Şablondaki bu değişkene bir değer atamak için, bu değeri şablonu
derlemeden önce, şablon içeriğinde belirtmemiz gerekiyor.

	:::python
	from django.template import Context, loader
	from blog.models import makale
	from django.http import HttpResponse

	def anasayfaView(request):
		sablon = loader.get_template('blog_index.html')
		icerik = Context({'baslik': 'Cok guzel blog, cok da guzel iyi blog!'})
		yanit = sablon.render(icerik)
		return HttpResponse(yanit)

Böylece, şablonumuzun içerisinde basit bir değişken kullanmış olduk.
Şimdi de biraz şablon etiketlerine bakalım. Bunun için önce, şablon
içeriğine makalelerimizin bir listesini gönderelim.

	:::python
	from django.template import Context, loader
	from blog.models import makale
	from django.http import HttpResponse

	def anasayfaView(request):
		makaleler = makale.objects.all()
		sablon = loader.get_template('blog_index.html')
		icerik = Context({
								   'baslik': 'Cok guzel blog, cok da guzel iyi blog!',
								   'makaleler' : makaleler
		})
		yanit = sablon.render(icerik)
		return HttpResponse(yanit)

Burada, tüm makalelerimizi şablonumuza içerik olarak gönderdik. Şimdi
anasayfa şablonumuzu makalelerimizi gösterecek şekilde düzenleyelim.

	:::html
	{% for makale in makaleler %}
	<h1> {{ makale.baslik }}</h1>
	<p>{{ makale.makale }}</p>
	{% endfor %}

Burada ilk şablon etiketimizle tanışmış olduk. Bu etiket bize
python'daki for döngüsüne benzer bir döngü oluşturup, döngünün her
tekrarında makale isimli değişkeni, makaleler içerisindeki model
objelerinden bir sonrakine eşitliyor. Django şablonlarının içerisinde,
nesne özelliklerine python'daki gibi nokta gösterimiyle ulaşabiliyoruz.
Son olarak, bir diğer etiket ile, for döngüsünün bittiği yeri
belirtiyoruz.

Django şablonlarında sıklıkla kullanmak isteyeceğiniz bir başka etiket
ise, bize python'daki `if` yapısına benzer bir yapı kurma imkanı
sağlıyor. Bir örnekle görelim:

	:::html
	{% if makaleler %}
	  {% for makale in makaleler %}
	  <h1> {{ makale.baslik }}</h1>
	  <p>{{ makale.makale }}</p>
	  {% endfor %}
	{% else %}
	  <p>Malesef makale yok!</p>
	{% endif %}

Burada, if etiketi sayesinde, makaleler değişkenini bir mantıksal
değerlendirmeye aldık. Eğer buradaki mantıksal değerlendirme doğru
olarak sonuçlanırsa, yani, makaleler değişkeni tanımlanmış, boş değil ve
False değilse, if etiketi kedisiyle eşleşen else veya endif etiketine
kadar olan kısımların işlenmesini sağlıyor. Eğer değerlendirme yanlış
olarak sonuçlanırsa, şablon'un derlenmesi, eşleşen `else` etiketi veya
`endif` etiketinden sonra devam ediyor. `else` etiketinin nasıl
çalıştığını da zaten tahmin etmişsinizdir.

`block` ve `extends` etiketleri ise, bir şablonda, başka bir şablonun
sadece belli kısımlarını değiştirerek kullanma imkanı veriyor. Örneğin,
`blog_anasayfa.html` şablonumuzu şu şekilde düzenleyelim:

	:::html
	<html>
	  <head>
		<title>{% block baslik %}En güzel Blog! {% endblock %}</title>
	  </head>
	{% if makaleler %}
	  {% for makale in makaleler %}
	  <h1> {{ makale.baslik }}</h1>
	  <p>{{ makale.makale }}</p>
	  {% endfor %}
	{% else %}
	  <p>Malesef makale yok!</p>
	{% endif %}

Burada, bu şablonu temel alarak oluşturulan diğer şablonların üstüne
yazabilmesi için, *baslik* isminde bir blok tanımladık. Şimdi, yeni bir
şablon dosyası oluşturup içine şunları girersek, anasayfa ile tamamen
aynı, ancak başlığı farklı bir şablon elde ederiz.

	:::html
	{% extends "blog_anasayfa.html" %}
	{% block baslik %}Çok kötü bir blog bu!{% endblock %}

Eğer şimdi bir önceki şablon yerine bunu kullanırsanız, başlık kısmının
değiştiğini göreceksiniz. Bir şablonu temel alarak yeni şablon
oluştuduğunuzda, bütün blokların üzerine yazmak zorunda değilsiniz.
Üzerine yazmadığınız bloklar, temel aldığınız şablonda nasıl
tanımlandıysa o şekilde derlenir. Ayrıca tanımladığınız blokların
içerisinde, bütün şablon etiket ve filtrelerini kullanabilirsiniz.

Django şablonlarında bahsettiklerimize benzer daha birçok etiket var.
Bunların hepsinden burada tek tek bahsetmek gibi bir imkanımız olmadığı
için, bunların kullanımından zaman zaman yazacağım ufak yazılarda ayrı
ayrı bahsedeceğim.

Bu yazıyı bitirmeden önce, Django'daki bir kısayoldan bahsetmek
istiyorum. Bu kısayol sayesinde, tek bir satırda, şablonlarınızı işleyip
tarayıcıya gönderebilirsiniz.

	:::python
	from django.shortcuts import render_to_response

	def anasayfaView(request):
		veriler = {
					  'baslik' : 'Benim Blog!'
		}
		return render_to_response("blog_anasayfa.html",veriler)

Bu kısayol, sizin için şablonunuzu bulup, verdiğiniz verilere göre
işeyip size bir HttpResponse nesnesi döndürüyor. Şimdiye kadar
anlattığım kısımlarda kullandığımız yöntem Django'nun şablon sistemini
daha yakından anlamak içindi. Gerçek hayatta kullanılan yöntem
`render_to_response` yöntemidir. Siz de bunu kullanın!

Geliştirdiğimiz blog uygulamasının nasıl görüneceği tamamen kişisel
zevklere kalmış bir durum olduğu için, burada bir şablon
oluşturmayacağım. Şablonların oluşturulmasını size bırakıyorum.
Şablonlarınızı oluşturduktan sonra, elinizde çalışan bir blog sistemi
olmalı. Yazı dizisi boyunca geliştirdiğimiz blog uygulamasının
anlatımında, satır satır her kodu anlatmaktansa, Django'da uygulama
geliştirmenin genel çerçevesinden bahsettim. Bu yüzden, eğer bu noktaya
kadar gelirken atladığım önemli bir kısım olduğunu düşünüyorsanız,
lütfen bunu aşağıdaki yorumlarda belirtin.

Yazı dizisinin bir sonraki bölümünde, blog uygulamamıza site haritası
yapacağız. Herkese iyi geliştirmeler.

  [github deposu]: https://github.com/yasar11732/django-blog