<!--
.. date: 2011-09-05 18:50:00
.. title: Python'da Asal Sayı Bulma Algoritmaları ve Bunların Evrimi
.. slug: asal-yolculuk
.. description: Çeşitli asal sayı algoritmalarının incelenmesi ve yeni geliştiricilerin zamanla hangi algoritmaları kullanmaya başladıkları ile ilgili bir yazı.
-->


Kimse inkar etmesin, herkes programlama öğrenme sürecinin bir aşamasında
asal sayı hesaplamaya çalışmıştır. Bu ilk algoritmalar, çoğu zaman
verimsiz algoritmalardır. Biraz kendi deneyimlerimden yola çıkarak,
Python'dan asal sayı hesaplama fonksiyonlarının evrim sürecinden
bahsedeceğim. <!-- TEASER_END -->

### Tanımdan Gitme - Prosedürel

Asal sayıları biz birden ve kendinden başka bir sayıya kalansız
bölünemeyen sayılar olarak biliriz. Bu doğru bir tanımdır. Programlama
dilini yeni öğrenenler, ilk olarak tanımdan yola çıkan algoritmalar
yazarlar.

    :::python
    # -*- coding:utf-8 -*-
    # 1000 tane asal sayı bulan program
    
    print 2
    # xrange değil henüz...
    for i in range(3,1000):
    
        bolundu = False
        for j in range(2,i):
                if i % j == 0:
                    bolundu=True
                    # break yok...
        if bolundu == False:
            print i

### Tanımdan Gitme - Fonksiyonel

Asal sayı bulan ilk algoritmasını yazan programcılar, daha sonra bunu
bir fonksiyon haline getirmeyi ve tekrar tekrar kullanabilmeyi düşünür.
Aynı zamanda, birkaç önemli detay da algoritmaya eklenmiştir.

	:::python
	# -*- coding:utf-8 -*-
	 
	def asal(kaca_kadar):
		"""Asal sayı bulan fonksiyon
		Girdi olarak bir sayı alır
		Bu sayıya kadar olan asal sayıları ekrana basar.
		"""
		if kaca_kadar < 2:
			return
		elif kaca_kadar == 2:
			print 2
			return
		else:
			print 2
			for i in range(3,kaca_kadar):
				bolundu = False
				for j in range(2,i):
					if i % j == 0:
						bolundu=True
						break
				if bolundu == False:
					print i
				
### Fonksiyondan Liste Döndürme
    
Fonksiyon içinden direk ekrana değer basma karşıtı görüşler okuyan
programcı, fonksiyondan bir liste döndürür. Daha sonra listeyi ekrana
basar.

	:::python  
	# -*- coding:utf-8 -*-
	 
	def asal(kaca_kadar):
		"""Asal sayı bulan fonksiyon
		Girdi olarak bir sayı alır
		Bu sayıya kadar olan asal sayıları ekrana basar.
		"""
		asallar = [2]
		if kaca_kadar < 2:
			return None
		elif kaca_kadar == 2:
			return asallar
		else:
			for i in range(3,kaca_kadar):
				bolundu = False
				for j in range(2,i):
					if i % j == 0:
						bolundu=True
						break
				if bolundu == False:
					asallar.append(i)
		return asallar
     
	if __name__ == "__main__":
		# join kullanmak için, listedekiler str olmalı.
		print "\n".join(map(str,asal(1000)))
		"""
		Bu aşamada map() bilinmiyorsa, list comprehension veya for döngüsü kullanılır.
		print "\n".join([str(asal) for asal in asal(1000)])
		for asal in asal(1000)
			print asal
		"""

### Performans Kaygıları

Programcı artık algoritmasının performansını kafaya takacak aşamaya
gelmiştir. Çift sayılar artık hesaplanmaz, sayılar yarısından büyük
sayılarla bölünmeye çalışılmaz.

	:::python
	# -*- coding:utf-8 -*-
	 
	def asal(kaca_kadar):
		"""Asal sayı bulan fonksiyon
		Girdi olarak bir sayı alır
		Bu sayıya kadar olan asal sayıları ekrana basar.
		"""
		asallar = [2]
		if kaca_kadar < 2:
			return None
		elif kaca_kadar == 2:
			return asallar
		else:
			for i in xrange(3,kaca_kadar,2):
				bolundu = False
				for j in xrange(3,(i/2) + 1, 2):
					if i % j == 0:
						bolundu=True
						break
				if bolundu == False:
					asallar.append(i)
		return asallar
		 
	if __name__ == "__main__":
		# join kullanmak için, listedekiler str olmalı.
		print "\n".join(map(str,asal(10000)))
		"""
		Bu aşamada map() bilinmiyorsa, list comprehension veya for döngüsü kullanılır.
		print "\n".join([str(asal) for asal in asal(1000)])
		for asal in asal(1000)
			print asal
		"""
    
### Sadece asallarla bölmeye çalışmak

Programcı, asal sayı bulmak için, o sayıyı sadece asal sayılarla bölmeye
çalışmanın yettiğini hatırlar, bir önceki yöntemle bunu birleştirir.

	:::python
	# -*- coding:utf-8 -*-
	 
	def asal(kaca_kadar):
		"""Asal sayı bulan fonksiyon
		Girdi olarak bir sayı alır
		Bu sayıya kadar olan asal sayıları ekrana basar.
		"""
		asallar = [2]
		if kaca_kadar < 2:
			return None
		elif kaca_kadar == 2:
			return asallar
		else:
			for i in xrange(3,kaca_kadar,2):
				bolundu = False
				for j in asallar:
					 
					if i % j == 0:
						bolundu=True
						break
					if j > (i / 2):
						break
				if bolundu == False:
					asallar.append(i)
		return asallar
		 
	if __name__ == "__main__":
		# join kullanmak için, listedekiler str olmalı.
		print "\n".join(map(str,asal(20000)))
		"""
		Bu aşamada map() bilinmiyorsa, list comprehension veya for döngüsü kullanılır.
		print "\n".join([str(asal) for asal in asal(1000)])
		for asal in asal(1000)
			print asal
		"""
    
    
### Kareköke kadar bölme

Bir sayının asal bölenleri, o sayının karekökünden büyük olamaz.

	:::python
	def asal(kaca_kadar):
		"""Asal sayı bulan fonksiyon
		Girdi olarak bir sayı alır
		Bu sayıya kadar olan asal sayıları ekrana basar.
		"""
		asallar = [2]
		if kaca_kadar < 2:
			return None
		elif kaca_kadar == 2:
			return asallar
		else:
			for i in xrange(3,kaca_kadar,2):
				bolundu = False
				# karekökün aşağı yuvarlanma ihtimaline karşı, + 1 ekliyoruz.
				limit = (i ** 0.5) + 1
				for j in asallar:
					 
					if i % j == 0:
						bolundu=True
						break
					if j > limit:
						break
				if bolundu == False:
					asallar.append(i)
		return asallar
    
### Eratosthenes'in Elemesi

Bu yöntemde, 3'den verilen sayıya kadar olan tek sayılar bir listede
toplanır. Daha sonra, 3'er 3'er atlanarak, üzerine gelinen sayılar 0'a
eşitlenir. Böylece, 3'ün katları elenmiş olur. Daha sonra, ilk 0 olmayan
sayı kadar atlanarak üzerine gelinen sayılar 0'a eşitlenir. Böylece, o
sayının da katları elenmiş olur. Bu şekilde, en büyük sayının kareköküne
kadar devam edilir. Biraz önce bahsettiğimiz gibi, bir sayının kendi
karekökünden büyük asal böleni olamaz. Ve, bu sayının karekökü,
listedeki bütün sayıların karekökünden büyüktür. Dolayısıyla, bu sayının
kareköküne ulaşıldığında, elemeye son verilebilir.

	:::python
	# -*- coding:utf-8 -*-
	 
	def asal(kaca_kadar):
		"""Asal sayı bulan fonksiyon
		Girdi olarak bir sayı alır
		Bu sayıya kadar olan asal sayıları ekrana basar.
		"""
		 
		if kaca_kadar < 2:
			return None
		elif kaca_kadar == 2:
			return [2]
		else:
			# 3,5,7...,kaca_kadar
			sayilar = range(3,kaca_kadar + 1, 2)
			kok =  kaca_kadar ** 0.5
			 
			for i in xrange(0,len(sayilar)):
				sayi = sayilar[i]
				if sayi > kok:
					break
				if sayi:
					ilk_sil_index = i + sayi
					 
					for j in xrange(ilk_sil_index,len(sayilar),sayi):
						sayilar[j] = 0
				 
				 
				 
		return [2] + [sayi for sayi in sayilar if sayi]
		 
	if __name__ == "__main__":
		# join kullanmak için, listedekiler str olmalı.
		print "\n".join(map(str,asal(500)))
		"""
		Bu aşamada map() bilinmiyorsa, list comprehension veya for döngüsü kullanılır.
		print "\n".join([str(asal) for asal in asal(1000)])
		for asal in asal(1000)
			print asal