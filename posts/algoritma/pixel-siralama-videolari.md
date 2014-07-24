<!-- 
.. description: Bir kedi resmindeki pixellerin farklı algoritmalarla sıralanmasından oluşan 5 farklı algoritma videosu.
.. date: 2013/10/28 12:37:17
.. title: Pixel Sıralama Videoları
.. slug: pixel-siralama-videolari
-->


Geçen gün [Python ile tersine erime efekti](http://miratcan.tumblr.com/post/25087436669/python-ile-tersine-erime-efekti)
yazısını gördüm. Yaptığı şey çok hoşuma gitti, ben de özendim, o tarz birşey yapayım dedim. Tam olarak ne yapsam diye
düşünürken, aklıma sorting algoritmaları geldi. Sort algoritmalarını bir resim üzerinde uygulasam ve ara adımlardan
bir video oluştursam ilginç olabilir diye düşündüm, ve çeşitli sıralama algoritmaları ile birkaç video hazırladım.
Buyurun bakalım, umarım beğenirsiniz: <!-- TEASER_END -->

**Uyarı**: Videoların süreleri algoritmaların çalışma hızını göstermez.

**Uyarı 2**: Aşağıdaki Python algoritmaları sadece algoritmayı açıklamak için konmuştur, Python'da listeleri sıralamak için sorted veya liste.sort kullanın.

## Insertion Sort (Eklemeli Sıralama)
<iframe width="640" height="480" src="//www.youtube.com/embed/nqR-NYtEogc" frameborder="0" allowfullscreen></iframe>

### Algoritma

	:::python
	for i in range(1,len(liste)):
		for k in range(i,0,-1):
			if liste[k] < liste[k-1]:
				liste[k], liste[k-1] = liste[k-1], liste[k]
			else:
				break

## Selection Sort (Seçmeli Sıralama)
<iframe width="640" height="480" src="//www.youtube.com/embed/X3lT4eUO1B0" frameborder="0" allowfullscreen></iframe>

### Algoritma

	:::python
	for i in range(len(liste)-1):
		minelem = min(liste[i+1:])
		minindex = liste.index(minelem)
		liste[i], liste[minindex] = liste[minindex], liste[i]
		
## Bubble Sort (Kabarcık Sıralaması)
<iframe width="640" height="480" src="//www.youtube.com/embed/RoPPbtFgUdo" frameborder="0" allowfullscreen></iframe>

### Algoritma

	:::python
	while True:
		swapped = False
		for i in range (1,len(liste)):
			if liste[i-1] > liste[i]:
				liste[i-1], liste[i] = liste[i], liste[i-1]
				swapped = True
		if not swapped:
			break
			
## Merge Sort (Birleştirmeli sıralama)
<iframe width="640" height="480" src="//www.youtube.com/embed/S3i1Vvs5MG0" frameborder="0" allowfullscreen></iframe>
 
### Algoritma
Listeyi ortadan böl, iki parçayı recursive olarak sort et. Sonra sort edilmiş parçaları iç içe geçirerek sıralı biçimde birleşir.

## Quick Sort (Hızlı Sıralama)
<iframe width="640" height="480" src="//www.youtube.com/embed/stGBeQTPwY0" frameborder="0" allowfullscreen></iframe>

### Algoritma
Listeden bir eleman seç, o elemandan küçükleri bir listeye, büyükleri başka listeye kopyala, bu listeleri recursive olarak sırala, sonra bu iki kısmı birleştir.

[Bunları hazırlarken yazdığım kodlara](https://gist.github.com/yasar11732/7198414) her zamanki gibi gist üzerinden ulaşabilirsiniz. 