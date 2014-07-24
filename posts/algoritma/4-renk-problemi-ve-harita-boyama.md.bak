<!-- 
.. description: 4 renk teoreminin tanımı, tarihi ve harita boyama algoritması. Definition, history of 4 color theorem and map coloring algorithm in Python.
.. date: 2013/10/23 16:00
.. title: 4 renk teoremi ve harita boyama
.. slug: 4-renk-teoremi-ve-harita-boyama
-->

4 renk teoremi, verilen bir yüzeysel haritayı, komşu bölgeler farklı renklerde olacak şekilde
boyamak için 4 rengin yeterli olacağını savunuyor. Komşuluk, köşe olmayan ortak bir
sınıra sahip olmak olarak tanımlanmış. Bu teoremin geçerli olması için, bölgelerin
bir bütün halinde olması gerekiyor. Dünya haritası bu kurala uymuyor, çünkü, Alaska'nın
Amerikayla kara bağlantısı yok. <!-- TEASER_END -->

4 renk teoremine dün [Foundations of Mathematical and Computational Economics]
kitabını karıştırırken rastladım. 1976 yılında, Kenneth Appel ve Wolfgang Haken
tarafından bilgisayar kullanılarak kanıtlanmış. Bilgisayar kullanılarak kanıtlanan
ilk elle tutulur teoremmiş. *Every planar map is four colorable* diye aratırsanız,
orjinal makalenin pdf'leri var internette.

Bu renk problemi, haritacılardan daha çok matematikçilerin ilgisini çekmiş. Muhtemelen
çoğu haritacının böyle bir teoremden haberi bile yok.

Bir haritayı, bölgeleri köşe, sınıfları kenar oluşturacak şekilde bir diyagram şeklinde
göstererek soyutlayabiliyoruz. Bu durumda, problem "Graph Theory"nin ilgi alanına giriyor.

![map to graph conversion](/images/graph.png)

Bir diyagramı renklendirme fikri oldukça basit ve net, dolayısıyla bu renklendirmeyi
bulma algoritmalarının da basit olmasını bekleyebilirsiniz. Ama tam olarak öyle değil.
Diyagram renklendirmesi için bir algoritmayı tarif etmesi oldukça basit ama bu algoritmanın
çalışma süresi bir hayli uzun. [NP-hard] dedikleri problem sınıfına giriyor. Yani, optimum
diyagram boyama için bilinen algoritmalar exponensiyonel zamanda işlem yapıyor.

Bu boyama probleminin tek çözümü, bütün ihtimalleri değerlendirmek. Önce bir köşe seçip
ona bir renk ata, sonra onunla komşu olmayan her köşeye aynı rengi atayarak devam et. Sonra,
geri kalan köşelerden birine farklı bir renk ata ve aynı şekilde ilerle gibi bir algoritması
var. Bir takım kestirme yollarla da algoritmayı hızlandırmak mümkün. Ortalama durumda,
renlendirmeyi oldukça hızlı bir şekilde elde edebiliriz ancak, her zaman optimum bir renklendirme
istiyorsak, bunun tüm ihtimalleri denemekten başka bir yolu yok.

Basit bir renlendirme algoritmasının Python'da uygulanmış hali:

	:::python
	from collections import deque
	from copy import copy

	def degrees(vertices):
		counts = {}
		for v1, v2 in vertices:
			counts[v1] = counts.get(v1,0) + 1
			counts[v2] = counts.get(v2,0) + 1
		return sorted(counts.items(), key=lambda x:x[1], reverse=True)

	def neighborof(vertex, othervertices, completemap):
		"Check if vertex is a neighbor of any of other vertices in completemap"
		for v1, v2 in completemap:
			if (v1 == vertex and v2 in othervertices) or (v2 == vertex and v1 in othervertices):
				return True
		return False

	def color(mmap):
		verticedegree = degrees(mmap)
		uncolored = deque((x[0] for x in verticedegree))
		currentcolor = 0
		colors = {}
		while uncolored:
			coloredwithcurrent = set()
			a = uncolored.popleft()
			colors[a] = currentcolor
			coloredwithcurrent.add(a)
			for vertex in copy(uncolored):
				if not neighborof(vertex, coloredwithcurrent, mmap):
					uncolored.remove(vertex)
					colors[vertex] = currentcolor
					coloredwithcurrent.add(vertex)
			currentcolor+=1
		return colors
					

	if __name__ == "__main__":
		mymap = set([("a","b"),("a","c"),("a","e"),("b","c"),("b","d"),("c","f"),
			 ("c","d"),("c","e"),("d","f"),("e","f")])
		print color(mymap)
		
Buradaki tek incelik, komşu sayısı fazla olan köşelere önce renk atamak. Komşu sayısı
yüksek olan köşelere önce renk atamak, çoğu zaman rastgele renk atamaktan daha hızlı
çözüm verecektir.

Ben bu algoritmayı, boş bir sudoku üretmek için kullanmak istedim. Sudoku bir diyagrama
dönüştürebilir. Her sudoku karesi bir köşe olacak şekilde, aynı 3x3, aynı satır ve aynı sütün
içindeki kareler birbirilerine komşu olarak şekilde bir diyagram oluşturursak, bunun harita
boyama probleminden bir farkı yok. Bu komşuları elle oluşturmak uzun süreceğinden, şöyle
birşey kullandım:

	:::python
	def findgroup(item, groups):
		for g in groups:
			if item in g:
				return g
		raise ValueError("Row is not one of \"%s\"" % "".join(groups))

	def same3x3(vertice):
		row, column = vertice
		rg = findgroup(row,["ABC","DEF","GHI"])
		cg = findgroup(column,["123","456","789"])
		ingroup = ["".join([x,y]) for x in rg for y in cg]
		ingroup.remove(vertice)
		return ingroup
		
		
	def makesudokuedges():
		vertices = ["".join([x,y]) for x in "ABCDEFGHI" for y in "123456789"]
		edges = []
		visitedvertices = set()

		for vertice in vertices:
			gridmembers = same3x3(vertice)
			
			for other in gridmembers:
				if other in visitedvertices:
					continue
				edges.append((vertice,other))

			# add same row
			for column in "123456789":
				current = vertice[0] + column
				if current == vertice:
					continue
				if current in visitedvertices:
					continue
				if current in gridmembers:
					continue
				edges.append((vertice, current))

			# add same column
			for row in "ABCDEFGHI":
				current = row + vertice[1]
				if current == vertice:
					continue
				if current in visitedvertices:
					continue
				if current in gridmembers:
					continue
				edges.append((vertice, current))

			visitedvertices.add(vertice)
		return edges

Bu 81 köşeli, 810 kenarlı bir diyagram oluşturuyor. Satırlara A-I arasında harfler ve sütunlara 1-9 arasında sayılar verdim.
Örnek olarak, A1'in bağlantılı olduğu köşeler şu şekilde bulundu:
<pre>
A1 - A2
A1 - A3
A1 - B1
A1 - B2
A1 - B3
A1 - C1
A1 - C2
A1 - C3
A1 - A4
A1 - A5
A1 - A6
A1 - A7
A1 - A8
A1 - A9
A1 - D1
A1 - E1
A1 - F1
A1 - G1
A1 - H1
A1 - I1
</pre>

Bu oluşturulan diyagramı, aynı algoritmaya soktuğumda, şu sonucu elde ettim:

<pre>
2  4  1  5  3  7  6  9 8
5  10 3  2  9  6  7  1 4
6  7  9  4  1  8  2  5 3
11 1  8  9  2  10 3  4 6
3  5  4  7  6  1  9  2 11
7  2  6  3  4  5  10 8 1
9  8  7  6  5  4  1  3 2
4  6  5  1  10 2  8  7 9
1  3  2  8  7  9  4  6 5
</pre>

Gördüğünüz gibi, çıkan sonuç tek farkla sudoku kurallarına uyuyor. Oluşturulan
sonuçta 10 ve 11 rakamları da kullanılmış. Bunun nedeni algoritmanın optimum
sonucu değil, optimuma yakın bir sonuç üretmesi. Eğer optimum renklendirmeyi
elde etmek istersek, bütün ihtimalleri teker teker denemek gerekiyor. Bu
da işlem zamanı olarak oldukça uzun sürecektir.

Dolayısıyla, algoritma bu haliyle sudoku oluşturmak veya çözmek için
uygun değil. Ben bu algoritmanın üzerine bir tane sudoku çözücü yazdım
ama dediğim gibi o da çok yavaş çalışıyor galiba. Galiba diyorum çünkü
bitinceye kadar bekleyemedim, belki çalışmıyordur...

[Foundations of Mathematical and Computational Economics]: http://www.springer.com/economics/game+theory/book/978-3-642-13747-1