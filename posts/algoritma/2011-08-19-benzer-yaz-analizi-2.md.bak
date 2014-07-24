<!--
.. date: 2011-08-19 19:44:00
.. description: İki döküman arasındaki benzerlik nasıl ölçülür? Bir önceki yazıdaki algoritmayı geliştirdim ve sonuçlar tatmin edici oldu.
.. slug: benzer-yazi-analizi-2
.. title: Benzer Yazı Analizi 2
-->

[Benzer Yazı Analizi 1](benzer-yazi-analizi.html) başlıklı yazıyı okuduysanız, iki yazı
arasındaki benzerlikleri hesaplamaya çalışan bir algoritma yazmaya
çalışıyordum ancak çok da başarılı olamamıştım. Bu yazıda, algoritmayı
biraz geliştirdim ve aldığım sonuçlar tatmin edici oldu.

Bu yeni algoritmanın en önemli farkı, her kelimeye kendine göre katsayı
ataması. Önceki yazıda bahsettiğim, [Text
similarity: an alternative way to search MEDLINE][] yazısını takip
etmeye devam ettim, ve oradaki algoritmayı aynen uygulamaya çalıştım.
Kodlar aşağıda: <!-- TEASER_END -->

	:::python
	# -*- coding:utf-8 -*-
	from django.utils.html import strip_tags

	import os
	import sys
	import math
	import re
	PROJE_DIZINI = os.path.abspath(os.path.dirname(__file__))
	UST_DIZIN = os.path.abspath(PROJE_DIZINI + "/../")
	sys.path.append(UST_DIZIN)

	os.environ["DJANGO_SETTINGS_MODULE"] = "similarity.settings"


	from blog.models import Post




	def kelimeleriAl(post_objesi):
		tumu = post_objesi.title + " " + post_objesi.abstract + " " + post_objesi.post
		
		tumu = strip_tags(tumu.lower())
		
		regex = re.compile("\W+",flags=re.UNICODE)
		return re.split(regex,tumu)
		
	def say(sayilacak,kume):
		sayi = 0
		for obje in kume:
			if sayilacak in obje[1]:
				sayi += 1
		return sayi
		
	a = Post.objects.all()
	b = []
	for post in a:
		b.append((post.title,kelimeleriAl(post)))
	del(a)

	def katsayiAyarla(liste,kelime):
		kacKere = liste.count(kelime)
		if kacKere == 0:
			return 0
		else:
			return math.log(kacKere,1.6)
			

	liste = []
	tekil = []
	for i in range(0,len(b)):
		for kelime in b[i][1]:
			if kelime not in tekil:
				tekil.append(kelime)
				
	for i in range(1,len(b)):
		
		for j in range(0,i):
			
			ust_taraf = 0
			toplam1 = 0
			toplam2 = 0
			
			for kelime in tekil:
				
				# Kelime önemine göre ayarlanmış katsayılar
				ayarli1 = katsayiAyarla(b[i][1],kelime)
				ayarli2 = katsayiAyarla(b[j][1],kelime)
				
				ust_taraf +=  ayarli1 * ayarli2 * math.log(len(b)/say(kelime,b))
				toplam1 += ayarli1
				toplam2 += ayarli2
				
				
			alt_taraf = math.sqrt(toplam1 * toplam2)
			
			liste.append((b[i][0], b[j][0], ust_taraf/alt_taraf))
			
	liste = sorted(liste, key = lambda x: x[2])
	liste.reverse()
	print("\n".join(["%s and %s => %f" % (x,c,v) for x,c,v in liste]).encode("utf-8"))
        
Bu algoritmada, *kelimeleriAl* fonksiyonunu, sadece tekil kelimeleri
değil, tüm kelimeleri geri döndürecek şekilde yeniden ayarladım. Bu yeni
algoritmada, eskisinin aksine, vektör oluştururken (vektörleri
değişkenlere atamaktansa, doğrudan döngü içerisinde hesabı yaptım), her
kelimenin karşılaştırılan yazılarda kaçar kere geçtiğini ve bu kelimenin
önemini de hesaba katıyoruz. Bunu yapmak için, karşılaştırılan
kelimenin, site içerisinde kaç farklı makalede bulunduğuna bakıyoruz. Ne
kadar yaygın bir kelimeyse, o kadar düşük bir öneme sahip olacak. Çünkü,
"ve" "ile" vb. bağlaçlar ve bunlar gibi sık tekrar edilen kelimeler,
tanımlayıcı özelliklerini kaybediyor. Bunu 72. satırdaki
math.log(len(b)/say(kelime,b)) ile yapıyoruz. len(b) ile tüm makalelerin
sayısını alıp, sonra say fonksiyonunda bu kelimenin kaç makalede
geçtiğine bakıyoruz. Son olarak, bunların oranının doğal logaritmasını
alarak katsayıyı oluşturuyoruz. Örneğin bu katsayı,bütün makalelerde
geçen kelimeler için 0 olacak, dolasıyla her makalede geçen kelimeler,
makalelerin benzerliğini hesaplarken göz ardı edilecek. Bu ince ayarlar,
algoritmayı kosinüs yöntemiyle benzerlik bulmakdan biraz uzaklaştırıyor,
ancak, sonuçlarda bariz şekilde bir düzelme sezdim.

Karşılaştırdığımız kelimelerin her iki makaledeki sayısının önemli
olduğunu belirtmiştik, ancak, belli bir yerden sonra kelimenin tekrar
etmesinin çok önemi olmamalı. Bunu 47. satırdaki aldığımız 1.6'ya göre
logaritma sayesinde yaptık. Böylece, 5-6 kadar tekrardan sonra, bir
kelimenin ne kadar tekrar ettiğinin önemi çok düşük kalmış oldu.

Algoritmanın bölünen kısmını bir örnekle açıklamak gerekebilir. Diyelim
ki, "python" kelimesi karşılaştırılan yazıların birisinde 3 kere,
diğerinde 5 kere geçiyor. Ve sitedeki 10 makaleden 7'sinde python var.
Böylece, algoritmanın bölünen kısmı, log~1.6~(3) \* log~1.6~(5) \*
log(10/7) = 2.33 \* 3.42 \* 0.35 = 2.85 olacak. Bölen kısmına da örnek
verelim. Karşılaştırdığımız yazıların birinde 3 kere python, diğerinde
ise 5 kere python yazdığını varsayayım. Yani, tek ilgilendiğimiz kelime
python kelimesi, o yüzden alt taraf, 2.33 \* 3.42 = 8 olur. Böylece, 3
kere python ile 5 kere python yazan iki makale arasındaki sonuç yaklaşık
0.25 olucak.

Aşağıda, bu site için yaptığım analizin bir kısmını görebilirsiniz.
Bence bu sonuçlar oldukça tatmin edici oldu.

<pre>
Django'da Url Taşıma and 0'dan Bloga Django(4) => 1.000976
0'dan Blog'a Django (5) and Django'da Url Taşıma => 0.771432
Django Modelleriyle Paket Yöneticisi and 0'dan blog'a Django(1) => 0.749185
If..Else yada Try..Except, hangisi ne zaman kullanılmalı? and Django ve Url Düzeltme => 0.682939
0'dan Bloga Django(3) and 0'dan Blog'a Django(2) => 0.671333
0'dan Bloga Django(4) and 0'dan Bloga Django(3) => 0.618953
0'dan Blog'a Django (5) and 0'dan Bloga Django(4) => 0.616938
Django ve Url Düzeltme and 0'dan Blog'a Django (5) => 0.552183
Django ve Url Düzeltme and 0'dan Bloga Django(4) => 0.532040
</pre>

En yüksek benzerlik, Django'da url taşıma ve 0'dan bloga django 4
yazıları arasında çıktı. Eğer bu yazılara bakarsanız, ikisinin de url
yapılandırmasından bahsettiğini göreceksiniz. 0'dan Bloga Django yazı
dizisindeki tüm yazıların da birbirileriyle benzerlikleri yüksek çıktı.

Sonuç olarak, bu algoritmayı tatmin edici buldum. Birkaç gün içerisinde
optimizasyonlarını yapar siteye eklerim diye düşünüyorum


İyi Geliştirmeler.

  [Benzer Yazı Analizi 1]: /post/14870524124/benzer-yaz-analizi-1
  [Text similarity: an alternative way to search MEDLINE]: http://bioinformatics.oxfordjournals.org/content/22/18/2298.long