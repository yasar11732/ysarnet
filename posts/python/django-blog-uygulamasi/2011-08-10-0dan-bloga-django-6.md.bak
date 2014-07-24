<!--
.. date: 2011-08-10 22:20:00
.. description: Django'da google site haritası (sitemap.xml) nasıl yapılır? Rss nasıl yapılır?
.. slug: sitemap-rss
.. title: Django ile Blog Geliştirme - Rss ve Site Haritası
-->

Site haritaları ve rss beslemeleri bir blogun olmazsa olmazlarındandır.
Django'da bunların ikisini de yapmak çok kolay. sitemap ve rss beslemesi
yapmak için gerekli sınıflar, django'nun içindeki contrib paketiyle bize
sunuluyor. <!-- TEASER_END -->

Bu yazı dizisinde bahsedilen blog uygulamasının son haline [github
deposu][]ndan ulaşabilirsiniz.

Bu makale kullandığım örneklerde, halen bu gördüğünüz site için
kullandığım kodları kullanacağım. Bu siteyi yazmaya başladığımda birkaç
nedenden dolayı ingilizce olarak yazmaya başladığım için, değişken
isimleri şimdiye kadar yaptığımız örneklerden farklı olacak. Ancak,
gerekli açıklamaları yapacağımdan dolayı, bu örnekleri kendi projenize
kolaylıkla uygulayabileceğinizi düşünüyorum. Atladığım bir nokta varsa,
aşağıda gördüğünüz yorumlardan beni uyarırsanız sevinirim. Şimdi rss ile
ilgili olan kodları görelim:

	:::python
	# -*- coding:utf-8 -*-
	from django.contrib.syndication.views import Feed
	from django.shortcuts import get_object_or_404
	from portal.blog.models import Post, Tag

	class LatestPosts(Feed):
		title = "yasar11732: En Son Yazılar"
		link = "/"
		description = "Yeni yazilarin güncellemeleri"

		def items(self):
			return Post.objects.filter(yayinlandi=True).order_by("-pub_date")[:5]

		def item_title(self,item):
			return item.title

		def item_description(self,item):
			return item.abstract
		def item_pubdate(self,item):
			return item.pub_date

	class TagFeed(Feed):

		def get_object(self,request,tag):
			return get_object_or_404(Tag, text=tag)

		def title(self,obj):

			return "yasar11732: %s ile ilgili makaleler" % obj.text
		def item_description(self,obj):
			return obj.abstract

		def link(self,obj):
			return "/tag/%s/" % obj.text
		
		def description(self, obj):
			return "%s ile ilgili tum yazilar" % obj.text

		def items(self,obj):

			return obj.post_set.filter(yayinlandi=True).order_by("-pub_date")[:15]
		
		def item_pubdate(self,item):
			return item.pub_date

Bu modül, uygulamızın içerisinde herhangi bir isimle kayıtlı olabilir.
Bunu url tanımlamasına nasıl kaydedeceğimize birazdan değineceğim. Bu
modülde önemli olan nokta, import ettiğimiz Feed sınıfının alt
sınıflarını oluşturmak. Feed sınıfı rss beslemesi oluşturmak için
tanımlanmış genel bir görünüm sınıfı, bizim istediğimiz ise, bunu
kendimize göre özelleştirmek. LatestPost sınıfında, birkaç tane sınıf
değişkeni tanımladım. Bu sınıf değişkenleri sırasıyla rss beslemesinin
başlık, link ve tanım öğelerini belirliyor. Link değişkenini "/"
şeklinde belirtmemin nedeni, bu rss beslemesinin ait olduğu sayfasının
blog'umun anasayfası olması. LatestPosts sınıfında tanımladığım metodlar
ise, bu rss beslemesinin hangi öğelerden oluşacağı (items metodu), bu
öğelerin tanımlarının nasıl elde edileceği (item\_description) ve bu
öğelerin yayınlanma tarihinin nasıl elde edileceği (item\_pubdate) gibi
yöntemleri belirliyor. İsmi item\_ önekiyle başlayan metodlar, items
metodudan döndürdüğünüz nesne listesindeki nesnelerin her biri için
çalıştırılarak, rss beslemeniz oluşturuluyor. Bu metodların ikinci
parametleri, items metodundan dönen nesnelerden bir tanesi olduğu için,
ve ben Post objemin abstract, pub\_date vb. özelliklere sahip olduğunu
bildiğim için, bu özellikleri kullanarak rss beslememi oluşturmuş
oluyorum. Ben burada item\_ önekiyle başlayan 3 tane metod yazmış olsam
da, django'nun içerisinden açıp Feed sınıfını okursanız, burada
tanımlayabileceğiniz metodların listesi şöyle olmalı:

 - title
 - link
 - description
 - unique\_id
 - enclosure
 - pubdate
 - author\_name
 - author\_email
 - author\_link
 - categories
 - item\_copyright

TagFeed sınıfının LatestPost sınıfından farkı, her farklı etiket için,
farklı bir rss beslemesi üretmesi. Hangi etiket için besleme üreteceğini
`get_object` metodunun 3. argümanı sayesinde belirliyor. Bu argümanı bu
işleve gönderme işlemini, birazdan url'leri tanımlarken göreceğiz. Bu
sınıfın bir LatestPost sınıfından bir diğer farkı da, title, description
ve link öğelerini basit bir değişkene atayarak belirtmektense, bir metod
aracılığıyla belirtmiş olmamız. Bu sınıf her etiket için farklı bir rss
beslemesi üretmek durumunda olduğundan, her etiket için farklı bir
başlık, link ve tanım üretebilmek adına bu metodları `get_object`
metodundan aldığı nesneyle birlikte çağırıyor. Bu sınıfın diğer
özellikleri ise `LatestPost` sınıfıyla tamamen aynı.

Bu örnekte göremediğimiz şöyle bir nokta var ki, rss beslemesi
oluşturulacak her nesne için, Feed sınıfı bir link üretmeye çalışıyor,
bundan dolayı, ya tanımladığımız sınıfta bir item\_link metodu olmasını,
ya da nesne'nin kendisinin bir get\_absolute\_url metodu olmasını
bekliyor. Ben modellerimde get\_absolute\_url metodu tanımladığım için,
item\_link metodu yazmaya gerek duymadım.

Url tanımlaması yaparken, örnekte yazdığımız sınıfların views.py'de
yazdığımız işlevlerden bir farkı yok.

	:::python
	from feeds import LatestPosts, TagFeed
	urlpatterns += patterns('',
		(r'^rss/$', LatestPosts()),
	 (r'^tag/(?P[^/]+)/rss/$', TagFeed()),
	)

Burada, url'lerimiz için geriçağırım (callback) işlevi olarak biraz önce
yazdığımız sınıfların birer örneklerini (parentezlere dikkat edin!)
atıyoruz. Gerisini Feed sınıfından türettiğimiz sınıflarımız hallediyor.
Artık rss beslemelerimiz çalışır vaziyetteler.

Site haritası yapmak da, rss beslemesi yapmak kadar kolay, kodları
görelim :

	:::python
	from django.contrib.sitemaps import Sitemap
	from portal.blog.models import Post, Tag

	class PostSitemap(Sitemap):
	  changefreq = "never"
		priority = 0.5
	  
		def items(self):
			return Post.objects.filter(yayinlandi=True)
	 
		def lastmod(self,obj):
		  return obj.pub_date
		 
	class TagSitemap(Sitemap):
	  
		changefreq = "weekly"
	   priority = "0.4"
		
		def items(self):
			return Tag.objects.all()
		
		def lastmod(self,obj):
		  posts =  obj.post_set.all().order_by('-pub_date')
		   if len(posts) > 0:
			   return posts[0].pub_date
			else:
			   return None
Site haritası oluşturmak, rss beslemesi oluşturmaya çok benzer
olduğundan örnek kodları gösterip bırakıyorum. Siz okuyucuların genel
fikri aldığını düşünüyorum. Url yapılandırması da şu şekilde:

	:::python
	from sitemaps import PostSitemap, TagSitemap
	sitemaps = {
	'posts' : PostSitemap,
	'tags' : TagSitemap,
	}
	urlpatterns = patterns('',
	  (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps' : sitemaps}),

Burada, rss beslemesi örneğinden farklı olarak, yazdığımız sınıfları
geriçağırım metodu olara değil, django'nun sitemaps paketinin görünüm
fonksiyonuna argüman olarak verdik. sitemaps sözlüğü içinde iki farklı
sınıf belirttiğim için, son oluşan xml belgesinde iki sınıftan gelen
nesnelerin toplamında bir site haritası oluşturulmuş olacak.

Bu bölümde verdiğimiz örneklerde, dikkat çekmek istediğim diğer bir
nokta ise, dikkat çekmek istediğim noktaları belirtmek için, kodların
altında açıklama yapmak zorunda kalmam. Eğer kodların içerisinde
yorumlar yazmış olsaydım, sadece kodları burada göstererek bu yazıyı
tamamlayabilirdim. Bu da benim kendi ayıbım olmuş. Boş satır kullanmak
konusundaki düzensizliğime ise diyecek söz bulamıyorum. Siz böyle
yapmayın, hem kendiniz, hem de kodlarınızı okuyacak insanlar için.

Bu yazıyla birlikte, yazı dizisinin sonuna geldik. Artık elinizde
bir Django uygulaması olduğuna göre, [Django sunucusu olarak dotcloud](../dotcloud.html) yazısını
okumak isteyebilirsiniz.



  [github deposu]: https://github.com/yasar11732/django-blog