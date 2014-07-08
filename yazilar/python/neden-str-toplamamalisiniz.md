<!-- 
.. description: Döngü içerisinde str objelerini toplamak çok uzun sürüyor. En hızlı şekilde string birleştirmek için map ve join kullanın.
.. date: 2013/10/27 15:27
.. title: Neden str toplamamalısınız
.. slug: neden-str-toplamamalisiniz
-->

Günlerden pazar, bir yandan çay içip bir yandan Python kurcalarken, aklıma döngü optimizasyon
yöntemlerini denemek geldi. Daha önce bir yerde gördüğümü hatırladığım için, bir liste içindeki
int'leri karaktere dönüştürüp, bir str içinde birleştirmeyi deniyorum. Bu yöntem bu kadar hızlı,
şu yöntem bu kadar yavaş derken, acaba str objelerini + ile toplamak
ne kadar kötü olabilir ki diye merak ettim. 1 milyon karakter ile şunu denedim: <!-- TEASER_END -->

	:::python
	string = ""
	for i in bytelist:
		string += chr(i)
		
Bekledim, bekledim, bekledim... Bir türlü bitmek bilmedi. Ben de daha küçük liste üzerinde
deneyeyim dedim. Önce 10 bin, sonra 20 bin derken bir döngü içerisinde 420 bin uzunluklu
listeye kadar denedim. Sonuçlar şöyle oldu:

![scatter plot time versus number of chars](/images/scatter.png)

Grafikten de görüleceği üzere, çalışma süresinin artışı biraz exponansiyel gibi görünüyor.
İlk bakışta şaşırdım, lineer bir artış bekliyordum. Sonra kafama dank etti! Döngünün
her etabında, bir önceki str'nin başka bir yere kopyalanması ve yeni karakterin eklenmesi
gerekiyor. Döngü büyüdükçe, kopyalanması gereken string sayısı ile birlikte
kopyalanan stringlerin uzunluğu da artıyor. Dolayısıyla, ` n * (n - 1) / 2` karakter taşıma
işlemi yapılıyor. Yani gerçekten döngünün büyüklüğü ve harcanan zaman arasında <del>exponansiyonel</del> <ins>kuadratik</ins>
bir ilişki var. Kabataslak bir hesap yaptım, eğer işlemin bitmesini bekleseydim, 13-14 saat
beklemem gerekecekmiş. Aynı hesapla, eğer 10 milyon karakterle işlem yapsam, 57 gün beklemem
gerekecekti. İşte bu yüzden, özellikle döngü içerisinde str toplamak çok hoş sonuçlar doğurmuyor.

Bunlar da 10 milyon karakterle denediğim diğer algoritmalar:

	:::python
	# for loop 1
	chars = []
	for i in bytelist:
		chars.append(chr(i))
	string = "".join(chars)

	def looper():
		chars = []
		_chr = chr
		_append = chars.append
		for i in bytelist:
			_append(_chr(i))
		string = "".join(chars)

	# for loop 2
	looper()

	# map
	string = "".join(map(chr, bytelist))

	def looper2():
		_chr = chr
		string = "".join(map(chr, bytelist))

	# local map
	looper2()

Sonuçlar:

<pre>
for loop 1 took 4.05400013924 seconds
for loop 2 took 2.70499992371 seconds
map took 2.22099995613 seconds
map local took 2.24699997902 seconds
</pre>

Evet, şampiyonumuz:

	:::python
	string = "".join(map(chr, bytelist))
	
[Bu ölçümleri yapmak için kullandığım dosyaya](https://gist.github.com/yasar11732/7181985) gist üzerinden erişebilirsiniz.