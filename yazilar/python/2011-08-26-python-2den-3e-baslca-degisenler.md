<!--
.. date: 2011-08-26 20:41:00
.. title: Python 2.x ve 3.x Arasındaki Bazı Farklılıklar
.. slug: surumler-arasi-gecis-rehberi
.. description: Kodlarını Python 3'e taşımak isteyenler için, Python versiyonları arasındaki farklara değineceğiz, ve kodlarımız yeni Python sürümüne taşımakla alakalı bilgi vereceğiz.
-->

Python 2'den 3'e geçiş aşamasında, el altında bulundurmak için, en sık
ihtiyaç duyulacağını düşündüğüm farklılıklar, ve 2'den 3'e geçme
ipuçlarının bir listesinden oluşan kısa bir rehber oluşturma ihtiyacı
hissettim. Benim gibi bu aşamada el altında bir geçiş rehberi
bulundurmak isteyenlerle de paylaşmış olmak için, blogumdan yazayım
dedim. Eksikleri farkettikçe buraya ekleyeceğim.

Bilgilerin kaynakları (Şimdilik tek kaynak): [Python Belgeleri][]

**Not:** Eğer python öğrenmeye başlayacaksanız, ve hangi sürümden
başlayacağınıza karar vermeye çalışıyorsanız, bu rehberin size pek bir
faydası olmayacaktır. Python 2.6 veya 2.7 ile öğrenmeye başlayın. Ancak,
kodlarınızı çalıştırırken python yorumlayıcısını "-3" anahtarıyla
başlatın. Böylece, python 3'de değişen özelliklerle ilgili bilgi
alabilirsiniz. <!-- TEASER_END -->Örneğin:

    :::python
    python -3 merhaba-dunya.py

Eğer python konusunda deneyimliyseniz, ve python 3'e geçiş yapacaksanız,
okumaya devam edin.

    :::python
    "print artık bir fonksiyon"
    
    # python 2.x
    print "Python 2\'de böyle yazılıyordu."
    
    # python 3.x
    print("python 3\'de böyle yazılıyor.")
    
    """
    sözlük metodları dict.keys(), dict.items() dict.values() artık liste değil, sözlük görünüm 
    döndürüyor. Bunlar, sözlük değiştikçe dinamik olarak yenileniyor.
    """
    
    # python 2.x
    a = {1:"a",2:"b"}
    b = a.keys()
    print b
    # ekrana [1,2] basar.
    a[3] = "c"
    print b
    # ekrana [1,2] basar
    
    # python 3.x
    a = {1:"a",2:"b"}
    b = a.keys()
    print(b)
    # ekrana [1,2] basar.
    a[3] = "c"
    print(b)
    # ekrana [1,2,3] basar
    
    # python 3 de dict.iterkeys() dict.iteritems() dict.itervalues() artık yok.
    # Anladığım kadarıyla, bunlar yerine yukarıda bahsedilen yeni 
    # fonksiyonları kullanacağız.
    
    # map() ve filter() da artık iterator döndürüyor.
    
    map(lambda x: x-2, [5,7,10]).append(15) # python 3 de bunu yapamazsınız!
    
    # Python 3'de range bir iterator, xrange kaldırıldı.
    # bkz: http://yasararabaci.tumblr.com/post/14857699745/python-range-ve-xrange
    
    # zip() de bir iteratör döndürüyor.
    
    ####
    # Int ve long Objeleri
    ####
    
    # Python 3'de long objesi yok, int objesinin alabileceği maksimum değer kalktı.
    # Dolayısıyla, sys.maxint sabiti de yok!
    # ONEMLI : sys.maxsize sabiti hala var!
    
    # long int'lerin repr() metodu artık sonda bir L döndürmüyor. (GICIKTIM BUNA ZATEN!)
    

### Python 3'de unicode() yok

Unicode objeleri, str objeleri, bytearray objeleri ve bunlar arasında
işlem yapmak çok kaygan bir zemindi, python 3'de bu işe de bir el
atıldı.

-   Python 3'de yazı ve byte var. Tüm yazılar unicode.
-   unicode objesi yok, python 3'de yazılar str objesi kullanıyor, ancak
    bunlar python 2 deki unicode'lar gibi.
-   Bir önceki madde dolayısıyla, u"..." da python 3'de yok!
-   İki önceki madde dolayısıyla unichr() fonksiyonu da yok. chr()
    fonksiyonu unichr() gibi oldu.
-   Yazılar ve byte'lar arasında işlem ve karşılaştırma yok.
-   yazı -\> byte : str.encode() yada, bytes(str,encoding="bir kodlama")
-   byte -\> yazı : byte.decode() yada, str(byte,encoding="bir kodlama")
-   byte ve yazı objelerinde yerinde değiştirme yapılamıyor (mutable
    değil), bunun için bytearray() var. byte kullanacağınız neredeyse
    her yerde bytearray kullanabilirsiniz.

### Python 3'de except ve raise

Hata yakalama ve ayıklama konusunda da bazı değişiklikler oldu. En
önemli değişiklik, artık raise ile kullanacağınız *exception*, doğrudan
veya dolaylı olarak *BaseException* sınıfının bir alt sınıfı olmak
**zorunda**. Python 3'e geçiş yaparken, eğer BaseException sınıfının alt
sınıfı olmayan herhangi birşeyi raise ile kullanıyorsanız, bunları
baştan yazmanız gerekecek. Ancak halen tavsiye edilen, kendi
hatalarınızı *Exception* sınıfının bir alt sınıfı olarak yazmanız.
Bununla birlikte, yazımda da değişiklikler oldu.

    :::python
    # python 2.x
    raise Hata, arguman
    # python 3.x
    raise Hata(arguman)
    
    # python 2.x
    except Hata, degisken:
        print(degisken.ozellik)
    # python 3.x
    except Hata as degisken:
        print(degisken.ozellik)
    

### reduce() callable() gibi fonksiyonlar yok.

Hepsini yazmak uzun olacak diye, önemli bulduklarımı yazdım.

-   dict.has\_key(a) kullanımı kalktı, bunun yerine "a in dict"
    kullanmak gerekiyor.
-   callable(a) kalktı. Bunun yerine issubclass(a,collections.Callable).
    Bunun hakkındaki şahsi görüşüm saçmalığın daniskası olduğu yönünde.
-   reduce() fonksiyonu da kalktı. Bunun yerine for döngüsü kullanın
    diyorlar. İlla ki reduce kullanmak isteyenler functools.reduce()
    kullanacaklarmış.
-   raw\_input(), input() olarak adlandırıldı. Eski input davranışı için
    eval(input()) kullanın deniliyor.

Burada yazılanlar tüm değişiklikleri kapsamıyor. Sadece, kendi en sık
kullandığım python özelliklerini göz önünde bulundurarak, değişiklikleri
özet geçtim. Buraya eklenmesi gereken birşey olduğunu düşünüyorsanız,
yorumlarda belirtebilirsiniz.

Son bir not olarak, python 3'e geçiş için henüz çok erken olduğunu
düşünüyorum. Halen python 3'ün ne olduğu belirsiz ve aktif
geliştirilmesi devam ediyor. Ben şahsen, 3.5 gibi geçmeyi düşünüyorum.

  [Python Belgeleri]: http://docs.python.org/release/3.1.3/whatsnew/3.0.html