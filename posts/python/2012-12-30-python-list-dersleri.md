<!--
.. date: 2012-12-30 00:09:02
.. title: Python list -- Bir çırpıda listeler
.. slug: list-dersleri-tutorial
.. description: Python listeleri hakkında baştan sonra bir yazı. Listelerde ekleme, çıkarma, arama, birleştirme, dilimleme, döngü'de kullanma gibi birçok özellik anlatılıyor.
-->


Python list, yani liste, herhangi bir sayıda diğer objeleri içinde
bulunduran bir sandık vazifesi görüyor. Diğer dillerdeki listelerden en
önemli farkı ise, bir listede birden fazla tip öğenin yanyana
bulunabilmesi. Diğer konteynır tarzı objelerden farkı ise, listeler
mutable olması ve sıralı olması diyebilir. Diğer konteynırlar nedir
derseniz, kümeler (set) ve sözlükler (dict) bunlara örnek olarak
gösterilebilir. <!-- TEASER_END -->

Bir list oluşturmak için, köşeli parantezler arasında, virgüllerle
ayrılmış ifadeler sıralarız;

    :::python
    Listem = [] # boş list
    Listem = [ifade1, ifade2, ...]

Bu açık olarak Python list oluşturma şeklidir. Aynı zamanda hesaplanmış
bir liste oluşturabilirsiniz, ki bunlara Python jargonunda "[List
Comprehension][]" derler. Yazımı da şöyledir;

    :::python
    Listem = [ifade for degisken in sequence]

İfade olarak geçerli herhangi bir Python ifadesi yazılabilir. Bu ifade
sequnence ile belirtilen objenin her elemanı için hesaplanır ve sonuç
listeye dahil edilir. Örneğin;

    :::python
    Listem = [x**2 for x in (1,2,3,4,5)]

Yukarıdaki Python ifadesi bize `[1 4 9 16 25]` listesini verir.

Ayrıca yerleşik (built-in) list tipini kullanarak da liste
oluşturabilirsiniz;

    :::python
    Listem = list() # boş liste
    Listem = list(sequence) # sequence içindeki elemanlardan oluşan liste
    Listem = list(ifade for degisken in sequence) # Hesaplanan bir liste

### Elemanlara Ulaşmak

Benzer objelerde yapabildiğiniz gibi, list objelerinde de Len(Listem)
listedeki eleman sayısını, Listem[n] n'inci sıradaki elamanı,
Listem[n:k] ise n'inci sıradaki elemandan, k'ıncı sıradaki elemana kadar
olan elemanlardan oluşan listeyi döndürür.

    :::python
    uzunluk = len(Listem)
    eleman = Listem[index]
    dilim = Listem[baslangic:bitis]

Eğer index olarak negatif bir sayı girerseniz, Python o sayıya listenin
uzunluğunu ekler. Örneğin, 10 elemanlı bir listeye, `Listem[-1]`
girerseniz, `-1 + 10 = 9` olduğundan 9. indexdeki elemana ulaşırsınız
ki, kendisi son eleman olur. (ilk eleman 0'ıncı indexde olduğundan.)

Eğer listede olmayan bir index girerseniz, Python size bir
**IndexError** hatası verecektir. Ancak, dilimleme yöntemini
kullanıyorsanız, başlangıç ve bitiş indexleri sadece sınır noktaları
olduğundan, **IndexError** hatası vermez.

Liste dilimlerken, adımlama (slice stepping) da kullanabilirsiniz;

    :::python
    dilim = Liste[baslangic:bitis:adim]
    dilim = Listem[::2] # ilk elemandan başlayarak her ikinci elemanı alır.
    dilim = Listem[1::2] # ikinci elemandan başlayarak her ikinci elemanı alır.

### Listeler'de Döngüler

For-in yapısı, liste elemanları üzerinde gezinmek için en basit
yollardan biridir;

    :::python
    for eleman in L:
        print eleman

Eğer elemanların index'ine de ihtiyaç duyuyorsanız, `enumerate()`sizin
en iyi dostunuz olabilir;

    :::python
    for index,eleman in L:
        print index,eleman

Eğer sadece indexlerle ilgileniyorsanız, `len()` ve `range()`
kullanabilirsiniz;

    :::python
    for index in range(len(L)):
        print index

Sık kullanılan liste işleriniz için, Python'un bazı yerleşik
fonksiyonlarını kullanabilirsiniz. Mesela, eğer liste sadece sayılardan
oluşuyorsa, **sum** fonksiyonu bu sayıların toplamını bulur.

    :::python
    toplam = sum(L)
    toplam = sum(L, altoplam) # toplamı altoplama ekler...
    ortalama = float(sum(L)) / len(L)

Eğer liste stringlerden oluştuyorsa, bunları **join **ile
birleştirebilirsiniz;

    :::python
    "".join(L)

### Listeleri Değiştirmek

list belirli bir elemanı veya bir aralığı değiştirmenize imkan sağlar;

    :::python
    L[index] = yenieleman
    L[baslangic:bitis] = sequnce

Bu tarz işlemler listeyi kendi üzerinde değiştirecektir. Eğer bir
kopyasını almak isterseniz dilimleme ve list fonksiyonu
kullanabilirsiniz;

    :::python
    kopyaL = L[:]
    kopyaL = list(L)

Aynı zamanda listeye eklemeler de yapabilirsiniz. Sona tek bir eleman
eklemek için **append**, başka bir listeyi eklemek için **extend**,
belirli bir index'e yerleştirmek için **insert** fonksiyonları
kullanılır.

    :::python
    L.append(eleman)
    L.extend(sequnce)
    L.insert(index,eleman)

Başka bir listeden elemanları belli bir noktaya eklemek isterseniz,
dilimleme notasyonunu kullanabilirsiniz;

    :::python
    L[index:index] = sequence

Aynı zamanda listeden eleman da silebilirsiniz. **del** ifadesi belli
bir elemanı veya aralığı silerken, **pop** belirli bir elemanı siler ve
sildiği elemanı döndürür. **remove** ise bir elemanı arar ve siler.

    :::python
    del L[index]
    del L[baslangic:bitis]
    eleman = L.pop() # son elemanı siler ve döndürür.
    eleman = L.pop(0) # ilk elemanı siler ve döndürür.
    eleman = L.pop(index) # indexdeki elemanı siler ve döndürür.
    L.remove(eleman)

Son olarak, list tipi **reverse** metoduyla yerinde ters çevirilebilir;

    :::python
    L.reverse()

Ters çevirmek oldukça hızlıdır. Dolayısıyla listenin başına ekleme
çıkarmalar yapacaksanız önce ters çevirip, sonra işlemleri yapıp, tekrar
ters çevirerek zaman kazanabilirsiniz, çünkü listenin sonuna ekleme
yapmak, başına ekleme yapmaktan çok daha hızlıdır.

    :::python
    L.reverse()
    # append/insert/pop/delete ile sondaki elemanları değiştirin
    L.reserve() # listeyi eski haline döndürün.

Listelerde sıkça kullanılan işlemlerden biri, her elamanı bir fonksiyona
sokmak, ve bu elemanı fonksiyonun dönüş değeriyle değiştirmektir.

    :::python
    for index, eleman in enumerate(L):
        L[index] = fonksiyon(eleman)
    
    yeni = []
    for eleman in L:
        yeni.append(fonksiyon(eleman))

Yukarıdaki kod **map** veya list comprehension kullanarak daha iyi bir
şekilde yazılabilir.

    :::python
    yeni = map(fonksiyon, L)
    yeni = [fonksiyon(eleman) for eleman in L]

Dümdüz fonksiyon çağırmanın gerekli olduğu zamanlarda **map** fonksiyonu
daha verimlidir. Ancak, eğer biraz daha karmaşık bir şey yapıyorsanız,
list comprehension daha verimli olabilir.

Daha önce de bahsedildiği gibi, eğer hem elemana hem indexe ihtiyacınız
varsa, **enumerate** kullanın.

    :::python
    yeni = [fonksiyon(index,eleman) for index, eleman in enumerate(L)]

### Listede arama

**in** operatörünü bir elemanın listede olup olmadığını anlamak için
kullanırız. 

    :::python
    if eleman in L:
        print "L içinde ", eleman, " var!"

İlk eşleşen elemanın indexini bulmak için **index **metodunu kullanın.

    :::python
    L.index(eleman)

Tüm eşleşen elemanları bulmak için bir döngü kurup, **index**'e
başlangış adresi verebilirsiniz;

    :::python
        i = -1
        try:
            while 1:
                i = L.index(deger, i+1)
                print i," hanesinde eşleşme var."
        except ValueError:
            pass

Eşleşen elemanları saymak için **count** metodunu kullanın.

    :::python
    n = L.count(eleman)

En küçük ve en büyük değerleri bulmak için **max** ve **min**
fonksiyonlarını kullanın.

    :::python
    minik = min(L)
    buyuk = max(L)

  [List Comprehension]: http://www.istihza.com/forum/viewtopic.php?f=25&t=331