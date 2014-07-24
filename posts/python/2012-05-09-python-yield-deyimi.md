<!--
.. date: 2012-05-09 06:19:00
.. title: Python yield deyimi nedir? Ne işe yarar?
.. slug: yield
.. description: Python'da bir generator objesi oluşturmak için kullanılan yield sözcüğünün amacını ve kullanımını öğrenmek için bu örnekli anlatımı okuyun.
-->


Yazıya başlamadan önce, kullandığım dil ile ilgili bir açıklamada
bulunmam gerek. Her ne kadar bu yazının dili Türkçe olsa da, bazı
kelimeleri, özellikle de Türkçe'ye tam olarak geçmemiş, veya Türkçe
karşılığı henüz tam olarak yaygınlaşmamış bazı kelime ve terimleri
İngilizcede olduğu gibi kullanmaya karar verdim. Birtakım şeyleri
Türkçeye çevirmeye zorlamak, hem çok anlamsız oluyor, hem de bu
terimleri İngilizce adlarıyla bilenler için kafa karışıklığına neden
oluyor. Bu yüzden, yazının geri kalanında, aralara serpiştirilmiş
İngilizce kelimeler bulacaksınız.

Python dilindeki *yield* deyimini anlamak için, *generator*'ları bilmek
gerekiyor, *generator*'ları anlamak için de, *iterator* ve *iterable*
kavramlarını anlamak gerekiyor. İngilizcede "iterate" kelimesi, tekrar
tekrar uygulanmak veya işlenmek anlamına geliyor. Python'daki *iterable*
ve *iterator* kavramları bu kelimeden türetilmiş. Python'da *iter()*
yerleşik fonksiyona argüman olarak verebildiğimiz objelere iterable
diyoruz. iter() fonksiyonu bize bir iterator döndürüyor. *Iterator*,
objenin elemanları ne şekilde tanımlanırsa tanımlansın, bir koleksiyon
içindeki tüm elemanlara sırasıyla erişebilmemiz için ortak bir arayüz
oluşturan bir mekanizma. Kısacası, elemanları üzerinde sırasıyla
gezinebildiğimiz, listeler ve demetler gibi objelere *iterable* diyoruz.
Bu objeler, `iter()` fonksiyonu ile çağrıldığında, birer *iterator*
döndürüyor, ve bu *iterator*'lar bir koleksiyondan sırasıyla eleman
almak için kullanılıyor. <!-- TEASER_END -->

Şu kod paçasına bir bakalım:

    :::python
    a = [1,2,3,4,5]
    for k in a:
     print k

Bu örnekte, sıradan bir liste ve for döngüsü görüyoruz. Buradaki liste,
for döngüsünde kullandığımız herşey gibi, bir *iterable*. Python'da for
döngüsü, önce *iterable* olarak verilen objeden, döngü sırasında
kullanmak için bir *iterator* elde ediyor. Biz bu aşamayı görmüyoruz, bu
aşama, Python'daki for döngülerinin çalışma yapısının bir parçası. Daha
sonra, bu *iterator* elemanlar tükendi sinyali verene kadar, k
değişkenini bir sonraki elemana atayıp, döngünün gövdesini
çalıştırılıyor. Yani, yukarıdaki for döngüsü ile aşağıdaki kod parçacığı
tamamen aynı çalışıyor.

    :::python
    a = [1,2,3,4,5]
    b = iter(a)
    while True:
        try:
            k = next(b)
     except StopIteration:
           break
       print k

Yukarıdaki örnekte, ikinci satırda listenin elemanlarını sırasıyla elde
etmek için bir *iterator* oluşturup, bunu b değişkenine atadık.
Yukarıdaki for döngüsünde, bu işlem for döngüsü tarafından kendiğinden
yapılıyordu. Daha sonra, 5. satırda, k'yı *iterator'*dan gelen bir
sonraki elemana atadık. Eğer iterator yeni eleman veremiyorsa,
StopIteration durumu oluşturuyor. Bu durumu *catch* ile yakalayıp,
döngüden çıkıyoruz. *Iterator'larla* ilgili son bir
şey;*iteratorlar* tek kullanımlıktır, bir kere tükendikten sonra, aynı
 objenin elemanları içinde tekrar gezinmek için, yeni bir *iterator*'a
ihtiyacımız var.

Python'daki *generator'*lar ise, farklı bir çeşit*iterable*'dır.
Bunların diğer *iterable*'lardan farklarından biri, bunların tek
kullanımlık olmasıdır. Örneğin, bir listeyi istediğiniz kadar for
döngüsünde kullanabilirsiniz, ancak, bir *generator*'u yalnız bir kere
for döngüsünde kullanabilirsiniz. Bunların bir diğer önemli farkı ise,
tüm elemanların hafızada tutulmaması. *Generator*lar, sırası gelen
elemanı üretip döndürür, daha sonra da bu elemanı unuturlar. Örneğin;

    :::python
    generator = (x*x*x for x in range(5))
    for k in generator:
       print k
    """
    Ekrana şunu basar:
    0
    1
    8
    27
    64
    """
    for k in generator:
       print k
    """
    Ekrana hiçbir şey basılmaz, çünkü generator'u bir kere kullandık ve bitti.
    """ 

Yukarıdaki örnekte, ilk satırda bir *generator* oluşturup, bunu
generator isimli bir değişkene atadık. Şimdi bunu, istediğimiz gibi for
döngüsünde kullanabiliriz. Burada dikkat edilmesi gereken nokta, 0,1,8
gibi değerlerin, ilk satırda oluşturulmamış olması. Bu değerler, for
döngüsünde sıraları geldiklerinde oluşup, işleri bittikten sonra
hafızadan siliniyorlar. Genel olarak *generator*ların olayı bu kadar.

Artık *yield* deyimini anlamak için, yeterli altyapıya sahibiz. *yield*
deyimi, *return* deyimi gibi fonksiyonlarda kullanılır, ancak, fonksiyon
bir generator döndürür. Şu örneğe bakalım;

    :::python
    def creategeneratorSquare(l):
        for x in l:
         yield x * x
     
    generator = creategeneratorSquare([1,2,3,4,5])
    for k in generator:
       print k
    
    """
    Ekrana şunu basar:    
    1
    4
    9
    16
    25
    """

Yukarıdaki kod parçacığında, creategeneratorSquare isimli bir fonksiyon
oluşturduk. Bu fonksiyonun, normal fonksiyonlardan farkı, bir generator
döndürmesi. Bu fonksiyonu çağrıdığımızda, normal fonksiyonlardan
beklediğimiz gibi, fonksiyonun gövdesi **çalışmıyor**, bunun yerine
fonksiyon bir *generator* döndürüyor. Bu *generator* for döngüsü içinde
kullanıldığında, fonksiyon içinde yazdığımız kod, *yield* görene kadar
çalışıyor. Burada, *yield* deyimi "x \* x" döndürüyor ve beklemeye
başlıyor. Daha sonra, 6. satırdaki döngü, bir sonraki elemanı istedikçe,
beklemedeki kod bloğu tekrar *yield* görene kadar çalışıp, *yield*
gördüğünde sıradaki elemanı döndürüyor. Böylece, bu kod bloğu
tamamlanıncaya kadar, 6. satırdaki for döngüsü k'ya farklı değerler
atayıp, bunları ekrana bastırıyor.

Bir örneğe daha bakalım;

    :::python
    def fibogenerator():
      a,b = 1,1
       while True:
         yield b
         a,b = b, a + b
    
          
    for k in fibogenerator():
       if k > 10000000:
         print k
         break
    
    """
    Ekrana şunu basar:  
    14930352
    """

Bu örnekte, biz istedikçe bir sonraki fibonacci sayısını veren bir
*generator* kullanmak istedik. Bunun için, fibogenerator isimli bir
fonksiyon yazdık. Bir önceki örnekten farklı olarak, bu sefer
*generator*'u bir ara değişkende tutmaktansa, doğrudan for döngüsü
içinde kullandık. *Generator* zaten tek kullanımlık olduğu için, bunları
bir değişkene atamak çoğu zaman gereksiz. For döngüsünde ise, k 10
milyon'dan büyük olduğunda, k'yı ekrana bas ve döngüden çık dedik. Eğer
döngüden çıkmak için herhangi birşey kullanmazsak, bu for döngüsü
sonsuza kadar çalışırdı, çünkü, yazdığımız *generator* doğal yollardan
sonlanmıyor.

*yield* deyimi ilk görüldüğünde kafa karıştırıcı olabilir. Buna rağmen,
*yield* deyimini anlamaya çalışmakta yarar var, çünkü yeri geldiğinde
bunu bilmek, diğer yollardan çözemeyeceğiniz problemleri bir çırpıda
çözmenize olanak sağlıyor. [Python belgelerindeki itertools
sayfası][] *yield* kullanımıyla ilgili birçok örneğe sahip. Bunları da
incelemekte fayda var.

  [Python belgelerindeki itertools sayfası]: http://docs.python.org/library/itertools.html
    "itertools"