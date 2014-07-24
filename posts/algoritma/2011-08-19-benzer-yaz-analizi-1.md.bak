<!--
.. date: 2011-08-19 11:13:00
.. description: Blog yazılımlarında ilgili makale bulmak için çeşitli yöntemler var. Bu yazıda, dökümanlar arasında benzerlik skoru oluşturan bir algoritma denemesi yapılıyor.
.. slug: benzer-yazi-analizi
.. title: Benzer yazı analizi 1
-->

Benzer yazıları bulup, ziyaretçiye öneri göstermek zannettiğimden çok
daha zor gibi görünüyor. Bir yandan düzgün bir algoritma oluşturmaya
çalışırken, bir yandan da şu anda katettiğim yolu (her ne kadar çok
olmasa da) aktarayım istedim.

Yazıların benzerliklerini hesaplamak için, [Text similarity: an
alternative way to search MEDLINE][] adlı makalede kosinüs katsayısı
(Cosine Coefficient) formülünü gördüm (daha önce de başka bir yerde
görmüştüm bu formülü, ama çıkartamıyorum şimdi :) ) ve denemeye karar
verdim. Şimdilik, kelime ağırlıklarını formüle eklemeden bir deneme
yaptım. Şu şekilde bir python dosyası ortaya çıktı: <!-- TEASER_END -->

	:::python
	# -*- coding:utf-8 -*-
	from django.utils.html import strip_tags

	import os
	import sys
	from math import sqrt
	PROJE_DIZINI = os.path.abspath(os.path.dirname(__file__))
	UST_DIZIN = os.path.abspath(PROJE_DIZINI + "/../")
	os.environ["DJANGO_SETTINGS_MODULE"] = "similarity.settings"
	sys.path.append(UST_DIZIN)
	from blog.models import Post

	# Son makaleden geriye sarıcaz!

	sonMakale = Post.objects.latest("pub_date")

	i = sonMakale.id
	imla = [".",",","?","!","\"","\'",":",";"]
	def kelimeleriAl(post_objesi):
		tumu = unicode(post_objesi.title) + unicode(post_objesi.abstract) + unicode(post_objesi.post)
		tumu = strip_tags(tumu)
		for karakter in imla:
			tumu.replace(karakter,"")
		kelimeler = tumu.split(" ")
		tekil = []
		for kelime in kelimeler:
			if kelime not in tekil:
				tekil.append(kelime)
		return tekil

	benzerlikler = []
	while i > 0:
		j = i-1
		birisi = Post.objects.get(pk=i)
		birisi = kelimeleriAl(birisi)
		while j > 0:
			tumKelimeler = birisi
			
			oburu = Post.objects.get(pk=j)
			oburu = kelimeleriAl(oburu)
			
			
			
			for kelime in oburu:
				if kelime not in tumKelimeler:
					tumKelimeler.append(kelime)
			
			# vektör oluştur!
			birisi_vektor = []
			oburu_vektor = []
			for kelime in tumKelimeler:
				birisi_vektor.append(kelime in birisi and 1 or 0)
				oburu_vektor.append(kelime in oburu and 1 or 0)
			
			toplam = float(0)
			# Formül karelerini almamızı istiyor
			# ancak, 0 ve 1 sayılarının kareleri almak çok mantıklı gelmedi

			for k in range(0,len(tumKelimeler)):
				toplam += birisi_vektor[k] * oburu_vektor[k]
			
			birisi_toplami = 0
			for sayi in birisi_vektor:
				birisi_toplami += sayi
			
			oburu_toplami = 0
			for sayi in oburu_vektor:
				oburu_toplami += sayi
			
			bolen = sqrt(birisi_toplami * oburu_toplami)
			benzerlikler.append((Post.objects.get(pk=i), Post.objects.get(pk=j), toplam/bolen))
			j -= 1
		i -= 1
	print("\n".join([ "%s ve %s => %2f" % (a,b,c) for a,b,c in sorted(benzerlikler, key = lambda x: x[2])]))

Bahsettiğim yazıda geçen formülü birebir uygulamaya çalıştım.
*kelimeleriAl* fonksiyonunda, bir makelede geçen tüm tekil kelimeleri
döndürüyorum. Sonra döngünün içerisinde karşılaştırılan her iki makale
için bir vektör (vektör denir değil mi ona?) oluşturuyorum.

Vektör oluşturma işleminde, tumKelimeler (içinde tüm tekil kelimeleri
barındıran liste) içerisinde her kelime için, eğer o kelime makaleye
dahilse, o makalenin vektörüne 1, değilse 0 ekliyorum. Daha sonra da,
bahsettiğim linkde gösterilen formülü uyguluyorum. Birkaç sonuç örneği
verirsek:

<pre>
Django şablonlarında php ve 0'dan blog'a Django(1) => 0.951225
Django South göçünde "unique" alan hatası ve 5 Django İpucu => 0.923972
Django'da Abstract Modeller ve 0'dan Bloga Django(3) => 0.917118
Django'da Url Taşıma ve 0'dan Bloga Django(4) => 0.851807
.
.
.
Django ve Url Düzeltme ve Python range ve xrange => 0.161989
If..Else yada Try..Except, hangisi ne zaman kullanılmalı? ve Python range ve xrange => 0.158546
Django Modelleriyle Paket Yöneticisi ve Python range ve xrange => 0.155110
</pre>
Doğrusunu söylemek gerekirse, bu algoritmadan aldığım sonuçlar çok
tatmin edici olmadı. Bunun nedeninin de kelime ağırlıklarını algoritmaya
dahil etmememe bağlıyorum.

Bu algoritmanın şu anda bir diğer büyük eksikliği ise, gereksiz
kelimeleri (bağlaçlar gibi) de hesaplamaya dahil etmesi. Bir gereksiz
kelimeler listesi oluşturup, bir de onları çıkararak denemek gerek diye
düşünüyorum. Eğer bu konuda bir yol katedersem, yeni yazılarda
bahsedeceğim.

İyi geliştirmeler.

  [Text similarity: an alternative way to search MEDLINE]: http://bioinformatics.oxfordjournals.org/content/22/18/2298.long