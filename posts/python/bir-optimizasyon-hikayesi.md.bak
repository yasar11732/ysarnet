<!-- 
.. description: Basit bir Python fonksiyonunu optimize ederek, 10 kattan fazla bir hız artışı elde ettim.
.. date: 2013/11/02 21:00
.. title: Bir optimizasyon hikayesi
.. slug: bir-optimizasyon-hikayesi
-->

Birazdan okuyacaklarınız, Python'da yazdığım basit bir fonksiyonu optimize etme hikayemdir.

Çözmeye çalıştığım problem şu; bir string ve alt string verildiğinde, büyük string'in hangi
indexlerindeki karakterleri birleştirerek alt string'i elde edebileceğimi bulan bir algoritma
yazmak. Örneğin, büyük string "yasar arabaci", küçük string de "aa" olduğu zaman, algoritmanın
vereceği sonuç `[(1, 3), (1, 6), (1, 8), (1, 10), (3, 6), (3, 8), (3, 10), (6, 8), (6, 10), (8, 10)]`
olmalı. Örnekten de anlayacağınız üzere, alt stringi oluşturmak için, büyük string'den alacağım
karakterlerin sırasının değişmesini istemiyorum. Diğer bir deyişle, sonuçlar içinde (3,1) istemiyorum.

Bu problemi çözmek için yazdığım ilk algoritma şu oldu: <!-- TEASER_END -->

	:::python
	def makesubstr(string, substring):
		if not substring:
			yield tuple()
			raise StopIteration

		lookfor = substring[0]
		for i,c in enumerate(string):
			if c == lookfor:
				for remaining in makesubstr(string[i+1:], substring[1:]):
					yield tuple((i,)) + tuple(map(lambda x: x+i+1, remaining))
		raise StopIteration
	
Algoritma basit, recursive bir algoritma. Substring'deki ilk karakteri büyük string içinde bulup, devamını bulmak
için kendini tekrar çağırıyor. Bu algoritmayı kullanarak, şu dosyanın içinde lorem'leri aradım.

<pre>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut arcu nibh, ultriciesat
scelerisque bibendum, posuere rutrum velit. Donec sollicitudin scelerisque purus,
eu viverra leo. Vivamus rhoncus dui nulla, vitae condimentum metus ullamcorper vel.
Fusce condimentum mauris non accumsan tristique. Mauris eget ornare leo, eu lobortis
massa. Phasellus elementum neque ligula, quis rutrum purus vehicula at. Pellentesque
habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras
id elit laoreet, accumsan est ut, rutrum orci. Suspendisse vitae urna eget metus ullamcorper
congue cursus ac augue. Quisque erat libero, rhoncus eu tincidunt quis, rutrum in ipsum.
Sed sodales in libero et accumsan.

Maecenas hendrerit venenatis lacus, tincidunt dapibus lacus dignissim tincidunt. Sed
lobortis sapien vitae rhoncus convallis. Cras feugiat adipiscing libero. Quisque pretium
sed.
</pre>

Algoritmanın sonucu bulması, birkaç denemenin ortalaması alındığında, yaklaşık 13.5 saniye
sürdü. Daha iyisini yapabilirim diye düşündüm. İlk dikkatimi çeken, recursive fonksiyon
çağrısına bize verilen string'lerin bir dilimini göndermiş olmam oldu. Bu her fonksiyon
çağrısında, bunlar kopyalanacak demek. Yukarıdaki girdi için, fonksiyon 1138342 kere kendini
çağırıyor. Dolayısıyla, dilimlemek yerine, aşağıdaki gibi bir fonksiyon yazsak, bir hayli
iş yükünden kurtulmuş oluyoruz:

	:::python
	def makesubstr2(string, substring, strstart=0, substart=0):

		if not len(substring) > substart:
			yield tuple()
			raise StopIteration

		c = substring[substart]
		strlen = len(string)

		while strstart < strlen:
			if string[strstart] == c:
				for rest in makesubstr2(string, substring, strstart+1, substart+1):
					yield tuple((strstart,)) + rest
			strstart += 1

		raise StopIteration
		
Evet, stringleri kopyalamak yerine, sadece indeksleri recursive olarak gönderdiğimiz
için, bu fonksiyon ortalama 9 saniye sürdü. Evet, tam olarak 4 saniye kazandık!

Daha iyisini de yapabiliriz. Şu anda fonksiyon recursive. Python'da fonksiyon çağırmak
pahalı bir operasyon. Bu yüzden recursion'dan vazgeçip, fonksiyonu şu şekilde yazabiliriz:

	:::python
	def makesubstr3(string, substring):

		strlen = len(string)
		substrlen = len(substring)

		callstack = deque([(0,0, tuple())])
		
		while True:
			try:
				strstart, substart, positions = callstack.popleft()
			except IndexError:
				break

			if not substrlen > substart: # position of last added to positions
				yield positions
				continue

			c = substring[substart]
			while strstart < strlen:
				if string[strstart] == c:
					callstack.append((strstart+1, substart+1, positions + (strstart,)))
				strstart+=1

		raise StopIteration
		
Burada işler biraz daha komplike bir hal aldı. Aslına bakarsanız bunu doğru bir şekilde yazabilmek beni
biraz uğraştırdı. Ama özetle, recursion tarafından oluşturulacak call stack'i fonksiyon içinde kendim
oluşturdum. Böylece ek fonksiyon çağrısı yükünden kurtulmuş oldum. Fonksiyonun çalışması bu haliyle
ortalama 6.95 saniye sürdü. Yaklaşık 2 saniye daha kazandık! Ama, daha iyisini de yapabiliriz.

Python'da loop içinde Attribute erişimi (yani ali.veli gibi, alinin bir attribute'una erişmek) yerine
bu işlemi loop dışına taşıyarak, biraz daha verim elde edebiliriz:

	:::python
	def makesubstr4(string, substring):

		strlen = len(string)
		substrlen = len(substring)

		callstack = deque([(0,0, tuple())])

		_csappend = callstack.append
		_cspopleft = callstack.popleft

		
		while True:
			try:
				strstart, substart, positions = _cspopleft()
			except IndexError:
				break

			if not substrlen > substart:
				yield positions
				continue

			c = substring[substart]
			while strstart < strlen:
				if string[strstart] == c:
					_csappend((strstart+1, substart+1, positions + (strstart,)))
				strstart+=1

		raise StopIteration
		
Bu haliyle ortalam çalışma süresi 6.85 saniye oldu. Pek dişe dokunur bir gelişme değil, ama biraz daha
hızlandık. Ama, daha iyisini de yapabiliriz!

Algoritmamızda şöyle bir sıkıntı var ki, aynı string üzerinde belki milyonlarca defa karakter
araması yapıyoruz. Bunun yerine, karakterleri bir defa arayıp, pozisyonlarını bir sözlük
içine kaydedebiliriz. Yani şöyle:

	:::python
	def makesubstr6(string, substring):
		posdict = {}
		sublen = len(substring)
		
		for i,c in enumerate(string):
			if c in substring:
				try:
					posdict[c].append(i)
				except KeyError:
					posdict[c] = [i]

		callstack = deque([(0,0,tuple())])

		_popleft = callstack.popleft
		_append = callstack.append

		while True:
			try:
				start, subindex, positions = _popleft()
			except IndexError:
				break

			if subindex >= sublen:
				yield positions
				continue

			for i in posdict[substring[subindex]]:
				if i > start:
					_append((i, subindex+1, positions + (i,)))

		raise StopIteration

Bu algoritma ortalama 1.25 saniye sürdü. İlk algoritmaya göre 10 kattan daha fazla bir hız artışı
elde ettik. Bundan daha iyisini yapabilir miyiz? Muhtemelen yapılabilir. Ben birkaç şey daha denedim,
ama bununla kafa kafaya sonuç verdiler. Sizce bunu daha iyi bir şekilde yazabilir miyiz?