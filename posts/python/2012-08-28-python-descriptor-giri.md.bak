<!--
.. date: 2012-08-28 02:44:00
.. title: Python 'descriptor' - giriş
.. slug: descriptor
.. description: Python'daki descriptor'ler, diğer dillerdeki protected alanlara benzer obje özellikleri oluşturmamızı sağlıyor. Böylece, obje elemanlarına erişimi kontrol altında tutabiliyoruz.
-->

Python'a taa [2.2 sürümünde girse][] de, çok fazla kullanılmayan bir
özellik bu descriptor. Peki ne işe mi yarıyor bu? Muhtemelen bilirsiniz,
java ve c++ gibi nesne bazlı dillerde "protected" denen bir nane var.
Bir nesne'nin protected özelliklerini ancak kendisi değiştirebiliyor.
Bunu da getter ve setter diye nitelendirilen public fonksiyonlar ile
yapıyor.

Yine muhtemelen bilirsiniz, Python'da "protected" diye bir olay yok. Her
nesnenin her özelliğini herkes kafasına göre değiştirebiliyor. İşte
descriptor'ler burada devreye giriyor. Bu 'descriptor' denen şey bizim
bunların erişimi kontrol altında tutmamıza yardımcı oluyor. <!-- TEASER_END -->

Peki, tam olarak nedir bu descriptor? Özetle, aşağıdaki metotlardan
herhangi birini tanımlamış objelere descriptor diyoruz;

    :::python
    __get__(self, instance, owner)
    __set__(self, instance, value)
    __delete__(self, instance)

Şimdi uygulamalı olarak, çok basit bir descriptor görelim;

    :::python
    class SayiDescriptor(object):
        def __init__(self,name):
            self.name = name
        
        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise ValueError("%s bir sayi degil." % value)
            else:
                setattr(instance, self.name, value)
    
        def __get__(self, instance, owner):
            return getattr(instance, self.name)
        
    class Insan(object):
        yas = SayiDescriptor("_yas")
        
        def __init__(self,yas):
            self.yas = yas
            
    a = Insan(12)
    print a.yas
    b = Insan("osman")
    print b.yas

Bu kodu çalıştırdığımızda, alacağımız çıktı şu şekilde olacak;

<pre>
12
Traceback (most recent call last):
  File "C:\Users\muhammed\workspace\adsensebomb\main.py", line 22, in 
    b = Insan("osman")
  File "C:\Users\muhammed\workspace\adsensebomb\main.py", line 18, in __init__
    self.yas = yas
  File "C:\Users\muhammed\workspace\adsensebomb\main.py", line 7, in __set__
    raise ValueError("%s bir sayi degil." % value)
ValueError: osman bir sayi degil.
</pre>

Gördüğünüz gibi, a objesinin yas degeri 12 oldu, ancak b objesini yas
degeri osman olmadı. Ancak, "osman bir sayi degil." diye bir hata aldık.
İstediğimiz de buydu. Kodları incelersek, öncelikle SayiDescriptor
isimli bir sınıf oluşturduk. İşte, descriptor dediğimiz şey bu sınıf,
çünkü bu sınıf yukarıda bahsi geçen 3 fonksiyondan iki tanesini
tanımlıyor. Bir de `__init__(self, name)` var. Bunu, her descriptor'un
kendini tanımlayacağı bir ismi olması için kullanacağız.

`__set__(self, instance, value)` metodu, bu descriptor'a bir değer
atanırken Python tarafından çağırılan fonksiyon. Aldığı `instance`
argümanı, bu değişim hangi objeyi hedef alıyorsa o. Yukarıdaki
örneğimizde, `a` ve `b` objeleri, bu `__set__(self, instance, value)`
fonksiyonuna `instance` değişkeniyle gönderilecek. `value` ise, yeni
değer. Bu fonksiyonda, ilk önce `value` ile gelen yeni değer bir sayı mı
diye kontrol ediyoruz. Eğer değilse, bir hata veriyoruz. Aksi takdirde
ise, `instance`'ın bize verilen isimdeki değerini değiştiriyoruz. Bizim
örneğimizde bunun karşılığı, `a._yas = 12` olarak görülebilir. `b`
objesi için ise, bu satıra gelmeden hata verilecek.

`__get__(self, instance, owner)` ise, bu descriptor'dan değer almak için
kullanılıyor. `instance` argümanı, yukarıdakiyle aynı. `owner` ise, bu
objenin oluşturulduğu sınıf. Yani örneğimizde `owner` olarak alacağı
argüman `Insan` sınıfı olacak. Bu metodun yaptığı iş ise, bu
descriptor'un değerini döndürmek. Örneğimizde, `print a.yas` satırında,
her ne kadar biz görmesek de, bu metot çağırılıyor. Bu metot ise
`a._yas` değerini döndürüyor. Dikkat ederseniz, yukarıdaki `__set__`
metodu da bu değeri bu değişkende saklamıştı.

**Bkz:** [isinstance][], [setattr][], [getattr][]

Dikkat etmemiz gereken bir diğer nokta da, bu descriptor `Insan`
sınıfında, fonksiyonları içinde değil de, en dışta örneklendi. Buna
dikkat etmezseniz, descriptor düzgün çalışmayacaktır.

Açıklaması biraz uzunca görünse de, aslında kullanım açısından çok zor
değil. Her ne kadar yukarıdaki basitçe bir örnek olsa da, bu örneğe
bakarak email veya telefon numarası için descriptor yapabilirsiniz.

Descriptor oluşturmanın bir diğer yolu ise, [property][] fonksiyonu.
Aşağıdaki örnek, hem yukarıdakiyle eşdeğer, hem de daha temiz görünüyor;

    :::python
    class Insan(object):
        
        def __init__(self,yas):
            self._yas = yas
            
        def yget(self):
            return self._yas
        
        def yset(self,value):
            if isinstance(value, int):
                self._yas = value
            else:
                raise ValueError("%s bir sayi degil." % value)
        def ydel(self):
            del self._yas
            
        yas = property(yget, yset, ydel, "bana property derler!")
            
           
    a = Insan(12)
    print a.yas
    a.yas = "osman"
    print a.yas

Bu örnek de, yukarıdakine benzer bir çıktı verecek. Burada, descriptor
için ayrı bir sınıf kullanmak yerine, `property()` fonksiyonu ile bir
descriptor oluşturduk. Bu yöntem ilk yönteme göre biraz daha derli
toplu, ancak, yukarıdaki descriptor, birkaç farklı sınıf tarafından
kolayca örneklenebilir. Bu ise, oluşturulduğu sınıfın sınırları içine
sıkışmış bir descriptor.

Son olarak da, [decorator][] kullanarak nasıl descriptor
oluşturabileceğimize bakalım;

    :::python
    class Insan(object):
        
        def __init__(self,yas):
            self._yas = yas
        
        @property
        def yas(self):
            return self._yas
        
        @yas.setter
        def yas(self,value):
            if isinstance(value, int):
                self._yas = value
            else:
                raise ValueError("%s bir sayi degil." % value)
            
           
    a = Insan(12)
    print a.yas
    a.yas = "osman"
    print a.yas

Bu fonksiyonda, `yas` isimli fonksiyon için `property` decorator'u
kullandık. Böylece, bu aynı isimle erişilebilecek bir özellik ve bu
özelliğin değerini verecek bir fonksiyon olmuş oldu. Daha sonra, yine
aynı isimle bir fonksiyon için `yas.setter` decoratoru kullanarak, bu
fonksiyonu da değerin atanmasından sorumlu kıldık.

Böylece vereceğim örneklerin sonuna gelmiş olduk. Kolaylıklar...

  [2.2 sürümünde girse]: http://docs.python.org/whatsnew/2.2.html#descriptors
    "Python 2.2 changes - descriptor"
  [isinstance]: http://docs.python.org/library/functions.html#isinstance
  [setattr]: http://docs.python.org/library/functions.html#setattr
  [getattr]: http://docs.python.org/library/functions.html#getattr
  [property]: http://docs.python.org/library/functions.html?highlight=propert#property
  [decorator]: http://yasararabaci.tumblr.com/post/22751163382/python-decorator-nedir