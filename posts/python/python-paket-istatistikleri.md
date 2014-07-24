<!-- 
.. description: Python Paket İndeksindeki paketlerle ilgili, paket boyutları, en ihtiyaç duyulan paketler, en çok indirilen paketler gibi istatistikler.
.. date: 2013/10/18 15:32
.. title: Python Paket İstatistikleri
.. slug: python-paket-istatistikleri
-->


Bu yazıyı, Python Paket Indeksindeki paketlerle ilgili tanıtıcı istatistikler vermek için yazıyorum. Python paket
indeksindeki paketlerin sayfalarını indirip, içindeki verileri topladım. 34968 paketin PyPi sayfasını indirdim, bunlardan
34923 tanesinden veri elde edebildim. Python paket indeksinde 35813 paket olduğu rapor ediliyor. Ancak, bunlardan bazıları
aynı paketlerin farklı versiyonları. Ben tekil paket son versiyonları ile çalıştım. 

Neden böyle birşey yaptım? Merak ve boş zaman...<!-- TEASER_END -->

## Paket Boyutları

Çoğu paket, PyPi sayfasında, source veya egg dosyası halinde paketin indirme linkini bulunduruyor. Eğer, paket birden fazla dosya
sunuyorsa, tabloda ilk görüneni aldım. En büyük paketler, şunlar:

 1. b2gpopulate (36MB)
 2. ajenti (35MB)
 3. FinPy (29MB)
 4. django-dojo (28MB)
 5. QSTK (27MB)
 
Toplam boyut 4.2 GB, ortalama paket boyutu 161 KB çıktı. Standart sapma 1 MB.

## En Gerekli Paketler

Her paket için bir gereklilik skoru belirledim. Örneğin, a'nın b'ye, b'nin de c'ye ihtiyacı varsa, c'nin skoru 2, b'nin
skoru 1 oluyor, çünkü, doğrudan ve dolaylı olarak c'ye ihtiyaç duyan 2 paket var. Bu rakamı bulmak için, PyPi sayfalarındaki
Requires satırını kullandım. Her paket Requires satırını düzgün yazmamış, ama bulduğum sıralama doğru gibi görünüyor.

 1. numpy (1500)
 2. django (860)
 3. scipy (555)
 4. python (425)
 5. matplotlib (370)
 6. simplejson (310)
 7. requests (310)
 8. pil (275)
 9. pyyaml (265)
 10. lxml (255)
 
Galiba bir kısım paketler Requires kısmına *python* yazmış...

## İndirmeler

Her paketin PyPi sayfasında, günlük, haftalık ve aylık indirme rakamları var. Ben bu rakamları, 17 Ekim 2013'ü, 18'ine bağlayan gece topladım.

### Günlük

 1. distribute (67 417)
 2. setuptools (52 184)
 3. requests (50 486)
 4. ssl (50 201)
 5. certifi (49 738)
 
Toplam 1 880 974, ortalama 54, standart sapma 900.

### Haftalık

 1. distribute (445 006)
 2. setuptools (414 556)
 3. ssl (379 201)
 4. certifi (378 729)
 5. wincertstore (375 158)
 
Toplam 14 097 027, ortalama 403.6, standard sapma 6 425.

### Aylık

 1. distribute (1 743 309)
 2. setuptools (1 607 116)
 3. certifi (1 546 749)
 4. ssl (1 537 270)
 5. wincertstore (1 532 424)
 
Toplam 53 281 293, ortalama 1525.7, standard sapma 25058.7

## Python kodu satır sayısı

Rastgele 30 tane paket seçip (random.sample ile), bunların kaynak kodlarındaki `.py` dosyalarındaki dolu satırları saydım. *setup.py*
dosyalarını hariç tuttum. Elimdeki örneklerde, satır sayısı en az 2, en fazla 47 453 idi. Paket başı ortalama satır sayısı 2212.6 olarak çıktı.
Standart sapmasını 8729.7 olarak buldum. Paket başı ortalama satır sayısı için %95 güven aralığı oluşturduğumda, üst sınır 5336.4 çıktı.
Dolayısıyla, Paket indeksindeki paketlerde kaba taslak `2212 * 35813 = 79 239 844` satır Python kodu bulunuyor. Üst sınır olarak da,
`5336.4 * 35813 = 191 112 493` satır diyebiliriz (%95 güven oranı ile).

## Veri

[Paketlerin meta verileri](https://docs.google.com/file/d/0B_hwkDj0Is2Wdkl0S21kN29YUVk/edit?usp=sharing) (5 MB rar dosyası)
google drive üzerinden erişilebilir durumda. rar dosyasını açtığınızda, all_in_one isminde, 23 MB civarında bir dosya
elde edeceksiniz. Bu dosya, pickle edilmiş bir Python sözlüğü. Bunu yüklemek için:

	:::python
	from pickle import load

	with open("all_in_one") as d:
		package_metas = load(d)
		
Elde ettiğiniz sözlükteki anahtarlar, paket isimlerinin küçük harfle yazılmış hali. Değerler ise, paket hakkında bilgileri bulunduran
başka bir sözlük. Çoğu pakette en az şu bilgiler bulunuyor; `packagename`, `daily`, `weekly`, `monthly`, `Author`, `Home Page`. Diğer
bilgiler, paketten pakete değişiklik gösteriyor.