<!--
.. date: 2014/07/10 03:22
.. slug: threading-vs-multiprocessing
.. title: Threading mi, yoksa multiprocessing mi kullanmalıyım
.. description: Yeni başlayan arkadaşlar genelde multiprocessing ve threading konusunda sıkıntı yaşıyor.
-->
Merhaba,

Uzun süredir blog atıl kalmıştı, kısa bir yazı yazayım istedim.

Python'a yeni başlayan arkadaşlarda, threading ve multiprocessing konusu kafa karıştırıyor. Kafa karıştıran iki önemli husus var;

 - Threading ve Multiprocessing mantığı nedir?
 - Hangisi ne zaman tercih edilmelidir?
 
Bununla birlikte, birkaç koldan çalışan işlemler arasında tesanüd nasıl sağlanır, onu da bilmek gerekiyor. <!-- TEASER_END -->

Threading bir yandan çay demlenirken, diğer yandan kahvaltı hazırlamak demektir, multiprocessing ise, siz kahvaltı hazırlarken, başka birinin de sofrayı
hazırlaması gibidir.

Threading kullanırken, tek bir işlem farklı kollardan iki işi aynı anda yürütür. Multiprocessing'de ise, iki ayrı işlem vardır.

Threading hakkında daha basit bir örnek vermek gerekirse, iş başvurusu yapacağınızı düşünün. Başvurmak istediğiniz 5 farklı iş
yeri var. 2. iş yerine başvurmak için, 1. iş yerinden size dönmelerini beklemek istemezsiniz, çünkü ne zaman size dönüleceğini,
hatta dönülüp dönülmeyeceğini bilmiyorsunuz. Bu sebeple, daha bir yerden cevap gelmeden, diğer işyerlerine de başvuru göndermek
istersiniz, böylece en kısa sürede iş bulabilirsiniz. Örnek yapalım;

	:::python
	from threading import Thread
	from random import randint
	from time import sleep

	def basvuru(basvuru_id):
		sleep(randint(0,60))
		if randint(0,1):
			print "%i başvurusu kabul edildi." % basvuru_id
		else:
			print "%i başvurusu reddedildi." % basvuru_id


	for i in range(5):
		Thread(target=basvuru, args=(i,)).start()
		
Burada, ilk önce hangi başvurudan cevap gelirse, onu hemen ekranda görebiliyoruz. Eğer threading kullanmasaydık, toplamda çok daha fazla beklemiş olacaktık.

Threading aynı iş gücüyle farklı kollardan iş yaparken, Multiprocessing, iş gücünü de artırır. Örneğin, 4 çekirdekli bir işlemcinin her çekirdeğinde farklı bir
process çalıştırıp, bilgisayarın tüm kaynaklarından faydalanabilirsiniz.

Biraz önceki örnekte Threading kullandık, çünkü, bize ekstra iş gücü gerekmiyordu, sadece, boş bekleyeceğimiz zamanda, başka bir işe daha başlıyorduk. O yüzden,
o örnekte Threading kullanmak daha mantıklıydı. Şimdi de şu örneği düşünün; 500.000 ile 1.000.000 arasındaki asal sayıların toplamını almak istiyorsunuz. Bu durumda,
fazladan işlemci gücünü kullanabilirsiniz.

Peki bu durumda, Farklı kollardan nasıl çalışabiliriz? Basitçe, düşünürsek, 500.000 ile 1.000.000 arasındaki sayıları 4 parçaya bölüp, 4 farklı koldan, bu aralıktaki
sayıların asal olanları bulabiliriz. Daha sonra, bulunan sayıları toplarız. Örnek yapalım;

	:::python
	# -*- coding: cp1254 -*-
	from multiprocessing import Pool
	from math import sqrt, floor


	def asal_mi(sayi):
		"sayı asal mı?"
		if sayi < 2:
			raise ValueError("Sayi ikiden buyuk olmalidir.")

		if sayi == 2:
			return True

		if sayi % 2 == 0:
			return False

		bolunecekler = range(3, int(sqrt(sayi)),2)

		for b in bolunecekler:
			if sayi % b == 0:
				return False

		return True


	def sayilar_asal_mi(sayilar):
		"Bir liste içindeki asalları döndür"
		return [x for x in sayilar if asal_mi(x)]


	if __name__ == "__main__": # Bunu yapmanız şart, şimdilik niye diye sormayın.
		p = Pool(processes=4) # 4 işlemden oluşan işlemci havuzu oluştur

		# İşleri işlemler arasında dağıt
		sonuclar = p.map(sayilar_asal_mi, [ range(500000, 625000),
									   range(625000, 750000),
									   range(750000, 875000),
									   range(875000, 1000000) ] )

		alt_toplamlar = map(sum, sonuclar) # Her listenin kendi toplamını al
		print alt_toplamlar
		print sum(alt_toplamlar) # tümünü topla
		
Umarım anlaşılır olmuştur. Anlaşılmayan kısımlar olmuşsa, yorumlardan cevaplamaya çalışırım.