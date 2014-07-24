<!--
.. date: 2011-08-29 20:43:00
.. title: Python Hakkında Birkaç Soruya Cevap
.. slug: birkac-soruya-cevap
.. description: Python'daki __init__ gibi fonksiyonların amacı, java'da olduğu gibi mouse ve key listener yapma, PyQT olayları, raise kullanmanın amacı, map, filter, global fonksiyonlarının amacı anlatıldı.
-->


Bir arkadaşımın Python hakkındaki birkaç sorusu üzerine, bu soruları
blog'umdan cevaplamayı ve aynı soruların cevaplarını arayan diğer
arkadaşlarla da paylaşmış olmayı istedim.

Sorulara ve cevaplara geçmeden önce, şunu belirtmek istiyorum, python
öğrenmeye başlamış eski bir C veya Java geliştiricisiyseniz, bu
geçmişiniz Python öğrenmeniz açısından talihsiz bir durum. Python
öğrenmeden önce, C, Java, Php gibi diğer dilleri kullanmış
geliştiriciler, bu dillerdeki alışkanlıklarını Python'a taşımaya
meyillidir. Ancak, Python'un iş yapış şekli, kendine özgüdür. Bu yüzden,
Python öğrenmeye başlarken, daha önce programlama ile öğrendiğiniz
herşeyi gözardı etmeye çalışın, ve Python felsefesini öğrenmeye çalışın.
Bu konuda anlaştıysak, soru-cevap bölümüne geçebiliriz. <!-- TEASER_END -->

### Tkinter'de `Frame.__init__` gibi bir ibare var. Buradaki mantık nedir?

Açıkcası ben Tkinter bilmiyorum, hiç kullanmadım, ama genel olarak iki
alt tireli değişkenler ve sınıf metotlarından bahsetmek isterim.
Python'la yeni tanışanlar için, iki alt tireli değişkenler ve metot
isimlerinin kafa karıştırıcı olabileceğini, birkaç farklı şekilde
gördüm. Eğer bunlar sizin de kafanızı karıştırıyorsa, bunlar hakkında
benimsemeniz gereken ilk şey, bunların diğer sınıf metotlarından veya
değişkenler bir farkı olmadığıdır.

#### 2 Alt Tireli Değişkenlerin Özellikleri

Python'da ismi iki alt tireli değişkenlerin çoğu, Python tarafından
tanımlanan değişkenlerdir, ancak isterseniz, siz de ismi
*\_\_benimdegisken\_\_* gibi bir değişken tanımlayabilirsiniz. Bu
öntanımlı değişkenler, Python'un iç dinamikleri açısından önemlidir.
İsimlerinin bu şekilde olmasının nedeni de budur. Böylece
geliştiricilerin, farkında olmadan önemli değişkenlerin üzerine
yazmasının önüne geçilmiş olur. Bu da demek oluyor ki, bu değişkenleri
çalışma anında değiştirebilirsiniz. Ancak, yapmayın, kendi akıl
sağlığınız için... Bunlardan sık kullanılan birkaçına örnek vermek
istiyorum:

**\_\_name\_\_:** Bu değişken, bir modülün veya sınıfın çalışma anındaki
adını tutar. Çalışma anında ilk çalıştırılan modülün adı "\_\_main\_\_"
olur. Gerek doğrudan, gerekse dolaylı olarak içe aktarılan diğer
modülüllerin adı ise, paket\_adı.modül\_adı gibi noktalı gösterim olur.
Sınıfların adı ise, nasıl tanımladıysanız, o şekildedir.

    :::python
    """
    bisiler.py
    Eğer bu modül, doğrudan çalıştırıldıysa, bisiler_yap fonksiyonunu çalıştırıyor.
    Eğer import ile içe aktarıldıysa, hiçbirşey yapılmıyor.
    """
    class a:
        def benim_adim(self):
            return self.__class__.__name__
    """
    >>> b = a()
    >>>b.benim_adim()
    'a'
    >>>b.__name__
    AttributeError: a instance has no attribute __name__
    >>> Sınıf instance'ı (tr:örnek) için __name__ tanımlı değildir.
    """
    if __name__ == "__main__":
        bisiler_yap()
    

**\_\_file\_\_:** Bu değişken, bir modülün dosya yolunu tutar.

    :::python
    """
    os_nerde.py
    Bu modül, doğrudan çalıştırıldığında, ekrana os modülünün dosya yolunu
    basar.
    """
    import os
    if __name__ == "__main__":
        print(os.__file__)
    

**\_\_package\_\_:** Bu değişken, bir modülün hangi pakete ait olduğunun
bilgisini tutar. Eğer modül hiçbir paketin içerisinde değilse, *None*
döndürür.

    :::python
    """
    hangi_paket.py
    """
    import os
    from django.db import models
    print(os.__package__)
    # None
    print(models.__package__)
    # django.db.models

**\_\_doc\_\_:** Bu değişken, bir modülün belgelendirmesini döndürür.
Modül içerisinde iki tırnak arasında (tek satırlık belgelendirme) veya 2
tane 3 tırnak arasında (çok satırlı belgelendirme) arasında kalan
yazılar, o modülün belgelendirmesini oluşturur. \_\_doc\_\_değişkeni
aynı zamanda, fonksiyonlar, sınıflar ve metotlar için de tanımlıdır.

    :::python
    """
    os_belgeleri.py
    """
    import os
    print(os.__doc__)
    #OS routines for Mac, NT, or Posix depending on what system we're on.
    #
    #This exports:
    #  - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
    #  - os.path is one of the modules posixpath, or ntpath
    #  - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
    #  - os.curdir is a string representing the current directory ('.' or ':')
    #  - os.pardir is a string representing the parent directory ('..' or '::')
    #  - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
    #  - os.extsep is the extension separator ('.' or '/')
    #  - os.altsep is the alternate pathname separator (None or '/')
    #  - os.pathsep is the component separator used in $PATH etc
    #  - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
    #  - os.defpath is the default search path for executables
    #  - os.devnull is the file path of the null device ('/dev/null', etc.)
    #
    #Programs that import and use 'os' stand a better chance of being
    #portable between different platforms.  Of course, they must then
    #only use functions that are defined by all platforms (e.g., unlink
    #and opendir), and leave all pathname manipulation to os.path
    #(e.g., split and join).
    #

Aklıma gelen özel değişkenler bunlar. Bunlardan başka var mıydı emin
değilim.

#### Özel sınıf metotları

Aynı yukarıda bahsettiğimiz değişkenler gibi, Python için özel anlamı
olan sınıf metotları, iki alt tireli olarak isimlendirilir. Bunlardan
bazıları şunlardır:

**\_\_new\_\_():** Bu metot, yeni bir sınıf örneği (eng:instance)
oluşturulacağı zaman çağırılır. Görevi yeni bir sınıf örneği
döndürmektir. Bu metoda python manyağı değilseniz hiçbir zaman ihtiyaç
duymazsınız. Şahsen ben hiç kullanmadım. İngilizce bilenler, daha
detaylı bilgi için: [metaclass hakkındaki So sorusuna](http://stackoverflow.com/questions/395982/metaclass-new-cls-and-super-can-someone-explain-the-mechanism-ex "Python meta sınıflar")
bakabilirler.

**Ekleme:** *5 Ekim 2013* Bununla ilgili ingilizce bir kaynağı çevirdim. [Python metaclass örnekleri](orneklerle-meta-classes-siniflar.html "Örneklerle Python Metasınıflar") ile ilgili yazıyı okuabilirsiniz.

**\_\_call\_\_():** Bu metot sınıfı çağırmak için kullanılır.
`b = a()` gibi bir kodla, sınıfı çağırmış olursunuz. yani,
`b = a()` python tarafından `b = a.__call__()`
şekline çevirilir. Eğer bu metodun üzerine yazmazsanız, bu metot,
`__new__()` metoduyla yeni bir sınıf örneği oluşturur, daha
sonra bu örneği döndürür.

**\_\_init\_\_():** `__new__()` metodu tarafından, yeni bir
sınıf örneği oluşturulduktan hemen sonra çağırılır. Çok sık kullanılan
bir sınıf metodudur. Sınıf örneğinin kullanıma hazır olması için gereken
tüm işlemler `__init__()` metodu içerisinde yapılır.

    :::python
    class Foo:
        def __init__(self):
            "yeni bir sınıf örneği oluşturulduğunda, bu örneğin _sayi özelliği 10 olarak atanır."
            self._sayi = 10
    
    class Bar:
        def __init__(self,sayi=10):
            """
            bu sınıfı oluşturuken, sayıyı değiştirmenize izin verir. Öntanımlı değeri 10dur
            a = Bar()
            b = Bar(20)
            a._sayi => 10
            b._sayi => 20
            """
            self._sayi = sayi
    
    class keyword_args:
        def __init__(self,**kwargs):
            "Oluşturulduğu anda aldığı kelime argümanları kendi özelliği olarak ayarlar."
            for anahtar, deger in kwargs:
                setattr(self,anahtar,deger)
    
    a = keyword_args(hebele = 2,hubele = "yazi", hubelop = [1,2,4])
    print(a.hebele)
    # 2 çıktısı basar.

**\_\_getitem\_\_() ve \_\_setitem\_\_():**köşeli parantez gösterimiyle
anahtar alma ve anahtar ayarlama işlemlerinde çağırılır.
`b = a[5]` gibi bir ifade kullandığınızda, Python bunu
`b = a.__getitem__(5)` şeklinde çalıştırır.

    :::python
    class Foo:
        def __init__(self):
            self._sozluk = dict()
        def __setitem__(self,anahtar,deger):
            self._sozluk[anahtar] = deger
        def __getitem__(self,anahtar):
            return self._sozluk[anahtar]
    
    a = Foo()
    a[25] = "yirmibes" # Aslında burada a.__setitem__(25,"yirmibes") çalıştırılıyor
    b = a[25] # burada da a.__getitem__(25) çalıştırılıyor.

**\_\_add\_\_() ve \_\_mul\_\_():**Bunlar, iki obje toplanırken veya
çarpılırken kullanılır. Örneğin `a + b` yazdığınızda,
aslında çalışan şey `a.__add__(b)` fonksiyon çağrısıdır.

**\_\_eq\_\_(), \_\_ne\_\_(), \_\_gt\_\_(), \_\_ge\_\_():** Bunlar iki
obje karşılaştırılırken kullanılır. Çoğu zaman `True` ya da
`False` döndürürler. Örneğin, `if a == b`
python tarafından `if a.__eq__(b)` şeklinde yorumlanır.

    :::python
    from random import randint
    class BasariSansi:
        def __eq__(self,oran):
            if randint(0,oran-1) == 0:
                return True
            else:
                return False
        def __ne__(self,oran):
            return not self.__eq__(oran)
    a = BasariSansi()
    for i in range(0,100)
    if a == 3:
        print("1/3 şansın yaver gitti!")
    else:
        print("Şansın yaver gitmedi!")

#### Sonuç olarak

Python'un en büyük zenginliklerinden birisi de, bize birçok konuda
özgürlük sağlıyor olmasıdır. Burada bahsettiğim özel sınıf metotları,
tüm sınıf metotlarının çok az bir kısmını içine alıyor. Eğer merak edip
diğerlerine de bakmak isterseniz, [Python'da veri modelleri][] ile
ilgili belgedeki özel metot isimleri ile alakalı bölüme göz
atabilirsiniz.

### Python ile Java'daki gibi mouse listener, veya key listener nasıl yapılır?

Soruyu soran arkadaş, hangi uygulamada klavye ve mouse olaylarını takip
etmek istediğini söylememiş, o yüzden birkaç farklı uygulamada bakalım.

#### Tkinter de fare ve klavye olaylarına geriçağırım fonksiyonu

Ben aslında Tkinter bilmiyorum, ama, biraz araştırdım ve [Events and
Bindings][] makalesini buldum. Bu makalede anlatılana göre, Tkinter
objelerine bind metoduyla geriçağırım fonksiyonu eklenebiliyor. İlk
argüman, olay türünü, ikinci argüman ise, çağırılacak fonksiyonu
gösteriyor.

    :::python
    # Kaynak: http://www.pythonware.com/media/data/an-introduction-to-tkinter.pdf
    from Tkinter import *
    
    uygulama = Tk()
    
    def mouseOlayi(olay):
        print("%s x %s noktasına tıklandı" % (olay.x,olay.y))
    
    frame = Frame(uygulama, width=100, height=100)
    frame.bind("", MouseOlayi)
    frame.pack()
    
    uygulama.mainloop()

Bunun detaylarına yukarıda verdiğim linkden bakabilirsiniz.

#### PyQt Olayları

PyQt'de farklı olaylarla uğraşmanın birkaç farklı yolu. Bunlardan bir
tanesi şöyle birşey:

    :::python
    from PyQt4.QtCore import * 
    from PyQt4.QtGui import *
    
    class BenimYaziAlani(QLineEdit):
        def event(self,event):
            if event.type() == QEvent.KeyPress:
                self.emit(SIGNAL("TusaBasildi"),event.key())
    class Uygulama(QMainWindow):
        def __init__(self,*args,**kwargs):
            QMainWindow.__init__(self,*args,**kwargs)
            self.yazi_alani = BenimYaziAlani()
            self.connect(self.yazi_alani,SIGNAL("TusaBasildi"),self.basilan_tus)
        def basilan_tus(self,tus):
            print("%s tusuna basildi" % tus)

### Python'da `raise` ne işe yarar

Python'da raise, bir hata yükseltmek için kullanılır. Daha sonra
istenirse, bu hata try..except bloğuyla yakalanabilir.

    :::python
    class CokAcayipHata(Exception):
        pass
    
    def basitToplama(ilk_sayi,ikinci_sayi):
        "İki sayıyı toplar, argüman olarak sayı verilmediyse hata verir!"
        if issubclass(ilk_sayi,int) and issubclass(ikinci_sayi,int):
            return ilk_sayi + ikinci_sayi
        else:
            raise CokAcayipHata
    
    try:
        sonuc = basitToplama("osman",7)
    except CokAcayipHata:
        print("Çok acayip bir hata oluştu, öyle böyle değil!")

### Python'da `map()` ve `filter()` fonksiyonları ne işe yarar?

#### `map()`

`map()` fonksiyonu, ilk argümanı olarak bir fonksiyon,
ikinci argümanı olarak sırayla elemanlarını alabileceği bir nesne alır.
Bu nesnenin her elemanını fonksiyona sokar ve sonucunu bir liste olarak
döndürür.

    :::python
    def mumdur(kac):
        return str(kac) + " mumdur"
    a = map(mumdur,[1,2,5,15])
    
    #a = ["1 mumdur","2 mumdur","5 mumdur","15 mumdur"]
    """
    map(mumdur,[1,2,5,15]) aşağıdaki şeyin kısa yoludur:
    """
    bos_liste = []
    for i in [1,2,5,15]:
        bos_liste.append(mumdur(i))
    

#### `filter()`

`filter()` fonksiyonu, ilk argümanı olarak bir fonksiyon,
ikinci argümanı olarak sırayla elemanlarını alabileceği bir nesne alır.
Bu nesnenin her elemanını fonksiyona sokar ve fonksiyonun sonucunun True
olduğu elemanları bir liste olarak döndürür.

    :::python
    def cift_sayi(kac):
        return kac % 2 == 0 and True or False
    a = fillter(cift_sayi,xrange(0,10))
    
    #a = [0,2,4,6,8]
    """
    filter(cift_sayi,xrange(0,10)) aşağıdaki şeyin kısa yoludur:
    """
    bos_liste = []
    for i in xrange(0,10):
        if cift_sayi(i):
            bos_liste.append(i)
    

### `global` kelimesi ne işe yarar

Python'da fonksiyonlar gibi kod blokları içerisinde tanımlı olan
değişkenler, yerel değişken olur. Buralarda tanımlı olan değişkenler, bu
kod bloklarının dışında tanımlı değildir. Böyle kod bloklarının
içersinde tanımladığınız değişkenin tüm modül içerisinde kullanılabilir
olması için, `global` kullanılır.

    :::python
    x = 0
    def yerel(asdf):
        x = asdf
    def genel(asdf):
        global x
        x = asdf
    
    yerel(10)
    print(x) # 0 yazar, fonksiyon içindeki x'in dışardaki x'e bir etkisi yoktur.
    genel(15)
    print(x) # 15 yazar, fonksiyonun içinde, genel x değiştirilmiştir.

  [Python'da veri modelleri]: http://docs.python.org/reference/datamodel.html#special-method-names
  [Events and Bindings]: http://www.pythonware.com/media/data/an-introduction-to-tkinter.pdf