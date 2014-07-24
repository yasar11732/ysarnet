<!--
.. date: 2011-12-23 08:54:00
.. title: Örneklerle Python Metasınıflar
.. slug: orneklerle-meta-classes-siniflar
.. description: Python meta sınıflar sizin de kafanızı karıştırıyorsa bu yazıyı okuyun. Eli Bendersky anlatmış, ben de çevirdim.
-->


Bugün [Eli Bendersky][]'ye ait [Python metaclasses by example][]
makalesini okudum. Metasınıflar benim için hep üç aşağı beş yukarı
havada kalan kavramlar olmuşlardır. Bahsettiğim makaleyi okuduktan
sonra, kafamda bir nebze daha iyi oturtabildim bunları. Bunun üzerine bu
makaleyi Türkçe'ye çevirip paylaşmaya karar verdim. Tabi ki, Eli
Bendersky'nin izni ile. Aşağıda makalenin tam metninin çevirisini
bulabilirsiniz:

Python, çalışma yapısını ve özelliklerini gizleyen birçok "sihir"
olmayışından ve diğerlerinden daha açık bir dil olduğundan haklı olarak
gurur duyar. Diğer yandan, bazen, ilgi çekici soyutlamalara imkan
sağlamak için olağandandan daha sihirli dil yapıları bulunan Python’un
daha kirli ve anlaşılması güç kısımları deşilebilir. *Metasınıflar*
böyle özelliklerdir. <!-- TEASER_END -->

Malesef, metasınıfların namı, "sorun arayan çözümler" olarak bilinir. Bu
makalenin amacı, sıkça kullanılan Python kodlarının içerisinde,
metasınıfların gerçek kullanımından birkaç örnek göstermektir.

İnternette Python metasınıflarıyla ilgili birçok materyal var (ÇN:
Türkçe yok malesef), yani bu sadece metasınıflar üzerine başka bir ders
değil (*Referanslar* bölümünde faydalı bulduğum linklere
bakabilirsiniz.). Metasınıfların ne olduğu konusuna biraz değineceğim
fakat, benim amacım örnekler. Bunu söylemişken, bu makale kendi yağında
kavrulmayı hedefler – metasınıfların ne olduğunu bilmiyorsanız bile
okumaya başlayabilirsiniz.

Başlamadan önce bir diğer hatırlatma – bu makale Python 2.6 & 2.7’e göre
yazılmıştır, çünkü internette bulacağınız birçok kod hala bu sürümler
içindir. Python 3.x’de metasınıflar benzer şekilde çalışsa da bunları
belirtmenin söz dizimi birazcık farklıdır. Sonuç olarak, bu makalenin
büyük bir kısmı 3.x’e de uygundur.

### Sınıflar da objedir

*metasınıflar*’ı anlamak için *sınıflar* hakkındaki bazı şeyleri
açıklığa kavuşturmalıyız. Python’da *herşey bir objedir*. Sınıflar da
dahil. Aslına bakarsanız, Python’da sınıflar [birinci-sınıf
objeler][]dir – çalışma anında yaratılabilir, parametre olarak
gönderilebilir ve fonksiyonlardan döndürülebilir ve değişkenlere
atanabilir. Sınıfların bu özelliklerini gösteren interaktif komut
satırından bir örnek:

	:::python
	>>> def make_myklass(**kwattrs):
	...   return type('MyKlass', (object,), dict(**kwattrs))
	...
	>>> myklass_foo_bar = make_myklass(foo=2, bar=4)
	>>> myklass_foo_bar
	<class __main__.MyKlass>
	>>> x = myklass_foo_bar()
	>>> x
	<__main__.MyKlass object at 0x01F6B050>
	>>> x.foo, x.bar
	(2, 4)

Burada `type` yerleşik fonksiyonunun 3 argümanlı şeklini `MyKlass`
isimli, `object`’den miras alan, bazı özellikleri argüman olarak
sağlanmış bir sınıfı dinamik olarak oluşturmak için kullanıyoruz. Daha
sonra böyle bir sınıf yaratabiliriz. Görebileceğiniz gibi,
` myklass_foo_bar ` şuna eşittir:

    :::python
    class MyKlass(object):
      foo = 2
      bar = 4
      

Ancak çalışma anında oluşturulmuş, fonksiyondan döndürülmüş ve bir
değişkene atanmıştır.

### Sınıf’ın sınıf’ı

Python’daki her obje (yerleşikler de dahil) bir sınıfa sahiptir. Biraz
önce sınıfların da obje olduklarını gördük, yani sınıfların da bir
sınıfı olmak zorunda, değil mi? Kesinlikle. Python ` __class__ `
özelliği ile bir objenin sınıfını incelememize izin verir. Bunu
çalışırken görelim:

	:::python
	>>> class SomeKlass(object): pass
	...
	>>> someobject = SomeKlass()
	>>> someobject.__class__
	<class __main__.SomeKlass>
	>>> SomeKlass.__class__
	<type 'type'>
		
      

Bir sınıf ve bu sınıfın bir objesini yarattık. `someobject` objesinin
` __class__ ` özelliğini inceleyerek, bunun SomeKlass olduğunu gördük.
İlginç kısım şimdi geliyor. `SomeKlass`’ın sınıfı ne? `__class__` ile
bunu tekrar inceleyebiliriz ve bunun `type` olduğunu görüyoruz.

Yani `type`, Python sınıflarının sınıfıdır. Diğer bir deyişle,
yukarıdaki örnekteki `someobject` bir *SomeKlass* objesiyken,
`SomeKlass`’ın kendisi de bir `type` objesidir.

Sizi bilmem ama ben bunu güven tazeleyici buluyorum. Madem sınıfların
Python’da obje olduklarını öğrendik, bunların da bir sınıflarının olması
mantıklı ve bir yerleşik sınıfın (type) sınıfların sınıfı rolünü
oynaması güzel.

### Metasınıf

Metasınıf "sınıfın sınıfı" olarak tanımlanır. Kendi örnekleri de bir
sınıf olan her sınıfa metasınıf denir. Öyleyse, yukarıda gördüklerimize
göre bu `type`’ı bir metasınıf yapar – aslında, sınıfların öntanımlı
metasınıfı olduğu için en çok kullanılan metasınıftır.

Metasınıf bir sınıfın sınıfı olduğu için, sınıf oluşturmakta kullanılır
(sınıfların obje oluşturmakta kullanıldığı gibi). Bir dakika, biz
sınıfları standart `class` tanımıyla oluşturmuyor muyuz? Kesinlikle, ama
Python merdiven altında şunları yapıyor:

-   `class` tanımı gördüğünde Python bunu çalıştırarak özellikleri
    (metotlar da dahil) bir sözlüğe toplar.
-   `class` tanımı bittiğinde Python sınıfın metasınıfını belirler.
    Şimdilik buna `Meta` diyelim.
-   Daha sonra Python ` Meta(name, bases, dct) ` deyimini çalıştırır ki
    burada: 

    

    -   ` Meta ` metasınıftır ki bunu çağırmak bir örneğini
        oluşturmaktır.
    -   ` name ` yeni oluşturulan sınıfın ismidir.
    -   ` bases ` sınıfın temel sınıflarının bir demetidir.
    -   ` dct ` Sınıf’ın tüm özelliklerini listeleyerek özellik
        isimlerini objelerle eşletirir.

Bir sınıfın metasınıfını nasıl belirleriz? Basitçe eğer sınıf veya
temelleri `__metaclass__` özelliği tanımlıyorsa, bu metasınıf olarak
alınır. Aksi takdirde metasınıf `type`dır.

O halde şunu tanımladığımızda olan nedir:

    :::python
    class MyKlass(object):
        foo = 2
      

Şudur: `MyKlass`’ın `__metaclass__` özelliği yok, yani bunun yerine
`type` kullanılıyor, ve sınıf oluşumu şu şekilde yapılıyor:

    :::python
    MyKlass = type(name, bases, dct)

Ki bu, makalenin başında gördüğümüzle tutarlı. Ancak diğer yandan eğer
`MyKlass` bir metasınıf *tanımlasaydı*:

    :::python
     class MyKlass(object):
      __metaclass__ = MyMeta
      foo = 2
      

O zaman sınıf oluşumu şöyle olurdu:

    :::python
    MyKlass = MyMeta(name, bases, dct)
      

O halde, `MyMeta` bu şekilde çağırılmayı destekleyecek ve bir sınıf
döndürecek şekilde uygulanmalı. Aslına bakarsanız bu, önceden
tanımlanmış yapıcı imzası olan normal bir sınıf yazmaya benzer.

### Metasınıf’da ` __new__ ` ve ` __init__ `

Sınıfın metasınıf içinde oluşturulmasını ve ilklenmesini (ÇN:
initialization) kontrol etmek için, metasınıf’da `__new__` metodunu
ve/veya `__init__` yapıcısını uygulayabilirsiniz (ÇN: implement). Çoğu
gerçek-hayat metasınıfları muhtelemen sadece bir tanesinin üstüne
yazar.`__new__` yeni obje yaratılmasını kontrol etmek istediğinizde
(bizim durumumuzda bu bir sınıf) ve `__init__` yeni obje yaratıldıktan
sonra, ilklenmesini istediğinizde uygulanmalıdır.

Yani, `MyMeta` çağırıldığında, merdiven altında yapılan şey:

    :::python
    MyKlass = MyMeta.__new__(MyMeta, name, bases, dct)
    MyMeta.__init__(MyClass, name, bases, dct)
      

Burada olup biteni göstermek için daha sağlam bir örnek var. Haydi bir
metasınıf için şu tanımı yazalım:

    :::python
    class MyMeta(type):
        def __new__(meta, name, bases, dct):
            print '-----------------------------------'
            print "Sınıf için hafıza ayırılıyor", name
            print meta
            print bases
            print dct
            return super(MyMeta, meta).__new__(meta, name, bases, dct)
        def __init__(cls, name, bases, dct):
            print '-----------------------------------'
            print "Sınıf başlatılıyor", name
            print cls
            print bases
            print dct
            super(MyMeta, cls).__init__(name, bases, dct)
      

Python aşağıdaki class tanımını çalıştırdığında:

    :::python
    class MyKlass(object):
        __metaclass__ = MyMeta
    
        def foo(self, param):
            pass
    
        barattr = 2
      

Ekrana basılan şudur (güzel görünmesi için biraz düzenlenmiştir):

<pre>
-----------------------------------
Sınıf için hafıza ayırılıyor MyKlass

(,)
{'barattr': 2, '__module__': '__main__',
 'foo': ,
 '__metaclass__': }
-----------------------------------
Sınıf başlatılıyor MyKlass

(,)
{'barattr': 2, '__module__': '__main__',
 'foo': ,
 '__metaclass__': }
</pre>
  

Bu örneği iyice anlayın ve metasınıf yazmakla ilgili bilinmesi
gerekenlerin çoğunu kavrayacaksınız.

Bu ekrana yazdırmaların *sınıf oluşturma anında* yapıldığını hatırlatmak
burada önem arz ediyor, yani, bu sınıfı içeren modülün içe aktarıldığı
zamanda. Bunu aklınızın bir köşesine yazın.

### Metaclass’da ` __call__ `

Bazen üzerine yazılması faydalı olabilecek bir diğer metasınıf metodu
`__call__`’dur. Bunu `__new__` ve `__init__` metotlarında ayrı ele
almamın nedeni, `__call__` metodunun, bu ikilinin sınıf oluşturulması
anınında çalışmasının aksine, zaten oluşturulmuş sınıfın, yeni bir obje
örneklenmesi (ÇN:instantiate) için "çağırıldığında" çalıştırılması. İşte
bunu açıklığa kavuşturmak için biraz kod:

    :::python
    class MyMeta(type):
        def __call__(cls, *args, **kwds):
            print '__call__ of ', str(cls)
            print '__call__ *args=', str(args)
            return type.__call__(cls, *args, **kwds)
    
    class MyKlass(object):
        __metaclass__ = MyMeta
    
        def __init__(self, a, b):
            print 'MyKlass object with a=%s, b=%s' % (a, b)
    
    print 'Şimdi foo oluşturacağım'
    foo = MyKlass(1, 2)
      

Bu şunu yazdırır:

<pre>
Şimdi foo oluşturacağım
__call__ of  
__call__ *args= (1, 2)
MyKlass object with a=1, b=2
</pre>
  

Burada `MyMeta.__call__` sadece bizi argümanlardan haberdar edip, işi
`type.__call__` metoduna devrediyor. Ama aynı zamanda işleme müdahale
edip, sınıflardan nasıl obje yaratıldığını etkileyebilir. Bir bakıma,
sınıfın kendisindeki `__new__` metodunu yazmaya benzer, ancak yinede
birkaç farkı vardır.

### Örnekler

Şimdiye kadar metasınıflar nedir ve nasıl yazılır konularını anlamak
için yeteri kadar teori işledik. Bu noktada, konuyu açacak örneklerin
zamanı geldi. Yukarıda bahsettiğim gibi, sentetik örnekler yazmaktansa,
*gerçek* Python kodu içerisindeki metasınıf kullanımını incelemeyi
tercih ederim.

### string.Template

İlk metasınıf örneği Python standart kütüphanesinden alınmıştır. Python
ile birlikte gelen çok az sayıdaki metasınıf örneklerinin bir tanesidir.

`string.Template` kullanımı kolay, yazı doldurma (ÇN: string
substitution) özelliği sağlar ve çok basit bir şablonlama sistemi görevi
yapar. Eğer bu sınıfla aşina değilseniz, şimdi belgeleri okumak için
güzel bir zaman. Ben sadece metasınıfları nasıl kullandığını
açıklayacağım.

İşte ` class Template ` içerisinden ilk birkaç satır:

    :::python
    class Template:
        """A string class for supporting $-substitutions."""
        __metaclass__ = _TemplateMetaclass
    
        delimiter = '$'
        idpattern = r'[_a-z][_a-z0-9]*'
    
        def __init__(self, template):
            self.template = template
      

Ve bu da ` _TemplateMetaclass ` :

    :::python
      class _TemplateMetaclass(type):
        pattern = r"""
        %(delim)s(?:
          (?P%(delim)s) |   # Escape sequence of two delimiters
          (?P%(id)s)      |   # delimiter and a Python identifier
          {(?P%(id)s)}   |   # delimiter and a braced identifier
          (?P)              # Other ill-formed delimiter exprs
        )
        """
    
        def __init__(cls, name, bases, dct):
            super(_TemplateMetaclass, cls).__init__(name, bases, dct)
            if 'pattern' in dct:
                pattern = cls.pattern
            else:
                pattern = _TemplateMetaclass.pattern % {
                    'delim' : _re.escape(cls.delimiter),
                    'id'    : cls.idpattern,
                    }
            cls.pattern = _re.compile(pattern, _re.IGNORECASE | _re.VERBOSE)
      

Bu makalenin ilk kısmında sağlanan açıklama `_TemplateMetaclass`’ın
nasıl çalıştığını anlamaya yeterli olmalı. Bunun `__init__` metodu bazı
sınıf özelliklerine bakar (özellikle `pattern`, `delimeter` ve
`idpattern`) ve bunu kullanarak (veya kendi sağladığı öntanımlıları)
derlenmiş bir düzenli ifade oluşturur ki, bu daha sonra sınıf’ın kendi
`pattern` özelliğine depolanır.

Belgelerine göre, `Template` miras alınarak, özel delimeter ve ID
yapısı, veya tam bir düzenli ifade sağlanabilir. Metasınıf *sınıf
oluşturma anında* bunları derlenmiş düzenli ifadelere dönüştürür, yani
bu bir nevi optimizasyondur.

Demek istediğim, aynı özelleştirme metasınıf kullanmadan, basitçe,
derlenmiş düzenli ifadeyi \_\_init\_\_ içerisinde oluşturarak
yapılabilir. Ancak, bunun anlamı, derlenme işleminin her `Template`
objesi örneklendiğinde yapılacak olmasıdır.

Şu kullanımı düşünün, ki bu kendi dürüst fikrime göre `string.Template`
için sıkça görülür:

    :::python
    >>> from string import Template
    >>> Template("$name is $value").substitute(name='me', value='2')
    'me is 2'
      

Düzenli ifade derlenmesini `Template` oluşturma zamanına bırakmak, böyle
bir kod her çalıştığında bunun oluşturulması ve derlenmesi demektir. Bu
bir ayıp, çünkü düzenli ifade şablondaki yazıya bağlı değil, sadece
*sınıfın özelliklerine* bağlı.

Bir metasınıf ile sınıfın `pattern` özelliği modül yüklenip
`class Template` (veya bir alt sınıfı) tanımı çalıştırıldığında
oluşturuluyor. Bu `Template` objesi yaratıldığında zaman kazandırır, ve
anlamlıdır çünkü sınıf oluşturma zamanında düzenli ifadeyi derlemek için
gerekli tüm bilgilere sahibiz – öyleyse neden bekleyelim?

Bunun henüz olgunlaşmamış bir optimizasyon olduğu iddia edilebilir, ve
bu doğru olabilir. Metasınıfın bu (veya herhangi bir) kullanımını
savunmayı düşünmüyorum. Buradaki niyetim çeşitli görevler için
metasınıfların gerçek kodlarda nasıl kullanıldığını sergilemek. Yani,
eğitsel amaçlar için iyi bir örnek, çünkü ilginç bir kullanımı
gösteriyor. Olgunlaşmamış bir optimizasyon veya değil, metasınıf bir
hesaplamayı kod çalıştırma sürecinde bir adım önceye alarak kodu daha
etkin hale getiriyor.

### twisted.python.reflect.AccessorType

Aşağıdaki örnek metasınıfları gösterirken/anlatırken sıkça kullanılır.
Bunun belgelerinden bir alıntı:

> 
>
> 
>
> Kendiliğinden sınıf özellikleri üreten bir metasınıf. Bu metasınıfı
> kullanmak, sınıfınıza açık erişici metotları (ÇN: explicit accessor
> methods) sağlar; set\_foo isimli bir metot, kendi kendine, set\_foo
> metodunu setter olarak kullanan ‘foo’ özelliğini oluşturacak. get\_foo
> ve del\_foo için de aynı şekilde. (ÇN: [bakınız][])
>
> 
>
> 
> 

İşte metasınıf, önemli kısımlara vurgu yapmak için biraz kısaltılmış
olarak:

    :::python
      class AccessorType(type):
        def __init__(self, name, bases, d):
            type.__init__(self, name, bases, d)
            accessors = {}
            prefixs = ["get_", "set_", "del_"]
            for k in d.keys():
                v = getattr(self, k)
                for i in range(3):
                    if k.startswith(prefixs[i]):
                        accessors.setdefault(k[4:], [None, None, None])[i] = v
            for name, (getter, setter, deler) in accessors.items():
                # create default behaviours for the property - if we leave
                # the getter as None we won't be able to getattr, etc..
    
                # [...] some code that implements the above comment
    
                setattr(self, name, property(getter, setter, deler, ""))
      

Bunun yaptığı dümdüz bir işlem:

1.  Sınıfın ` get_ ` , ` set_ ` veya ` del_ ` ile başlayan tüm
    özelliklerini bul.
2.  Kontrol etmeyi hedefledikleri özelliklere göre sınıflandır
    (altçizgiden sonra gelen kısım)
3.  Böylelikle bulunan her getter, setter, deleter üçlüsü için
    1.  Üçünün hepsinin var olduğundan emin ol, veya uygun öntanımlılar
        oluştur.
    2.  Bunları sınıf içinde bir ` property ` olarak ayarla

Böyle bir metasınıf ne kadar faydalıdır? Söylemesi zor aslında.
Twisted’ın kendisi bunu kullanmıyor ama bunu public API olarak sağlıyor.
Eğer birçok property ile birkaç sınıf yazacaksanız, bu metasınıf sizi
birçok kodlamadan kurtarabilir.

### pygments Lexer ve RegexLexer

[pygments][] kütüphanesi metasınıf kullanımının ilginç bir deyimini
sunar. Bir temel sınıf özel bir metasınıf ile oluşturulmuş. Kullanıcı
sınıfları bu temel sınıfdan miras alıp, metasınıf’ı yanında bir bonus
olarak alırlar. Öncelikle ` LexerMeta ` metasınıfına bir bakalım. Bu
`Lexer` için bir metasınıf olarak kullanılır – pygments içindeki
lexerlar için temel sınıf:

    :::python
    class LexerMeta(type):
        """
        This metaclass automagically converts `analyse_text` methods into
        static methods which always return float values.
        """
    
        def __new__(cls, name, bases, d):
            if 'analyse_text' in d:
                d['analyse_text'] = make_analysator(d['analyse_text'])
            return type.__new__(cls, name, bases, d)
      

Bu metasınıf, `analyse_text` mesajının tanımını yakalayıp, bunu herzaman
kayan noktalı bir değer döndüren statik bir metot’a çevirmek için
`__new__` metodunun üstüne yazar (`make_analysator` fonksiyonunun
yaptığı budur.).

Burada ` __init__ ` yerine ` __new__ ` kullanımına dikkat edin. Neden
` __init__ ` kullanılmadı? Benim düşüncem, bunun sadece bir tercih
meselesi olduğu – aynı etki ` __init__ ` metodunun üstüne yazarak da
başarılabilirdi.

pygments’den ikinci örnek biraz daha karmaşık, ama daha önceki
örneklerde görmediğimiz birkaç özelliği içerdiği için açıklama zahmetine
değer. ` RegexLexerMeta ` için kod bir hayli uzun, bu yüzden ilgili
kısmı bırakmak için kodu keseceğim:

    :::python
     class RegexLexerMeta(LexerMeta):
        """
        Metaclass for RegexLexer, creates the self._tokens attribute from
        self.tokens on the first instantiation.
        """
    
        # [...] kesilen kısım
    
        def __call__(cls, *args, **kwds):
            """Instantiate cls after preprocessing its token definitions."""
            if not hasattr(cls, '_tokens'):
                cls._all_tokens = {}
                cls._tmpname = 0
                if hasattr(cls, 'token_variants') and cls.token_variants:
                    # don't process yet
                    pass
                else:
                    cls._tokens = cls.process_tokendef('', cls.tokens)
    
            return type.__call__(cls, *args, **kwds)
      

Çoğunlukla, kod oldukça temiz; metasınıf `tokens` sınıf özelliğini
inceliyor, ve bundan `_tokens` oluşturuyor. Bu sadece sınıfın
oluşturulması sırasında yapılıyor. Burada özellikle ilgilendiğimiz iki
şey var:

1.  `RegexLexerMeta` `LexerMeta`’dan miras alır, böylece bunun
    kullanıcıları da `LexerMeta`’nın sağladığı hizmetleri alır.
    Metasınıfların miras alınması, bunların Python’daki en güçlü dil
    yapılarından birisi olmasının nedenlerinden birisidir. Bunları sınıf
    dekoratörleriyle yanyana koyun mesela. Bazı basit işler için, sınıf
    dekoratörleri metasınıfların yerine geçebilir, ama metasınıfların
    miras ilişkisi kurabilmesi dekoratörlerin yapamaycağı birşeydir.
2.  `process_tokendef` hesaplamaları `__call__` içerisinde yapılıyor –
    ve özel bir kontrol bunun sadece sınıfın ilk örneklenmesinde
    çalıştığından emin oluyor. (`__call__`’un kendisi tüm
    örneklenmelerde çalışsa da). Neden böyle yapılsın, bunu sınıf
    üretimi anında yapmak varken (metasınıf’ın `__init__`’inde mesela)?
    Bana öyle geliyor ki, bu bir çeşit optimizasyon olabilir. pygments
    bir çok lexer ile birlikte gelir, ama belirli bir kod için bunların
    sadece bir veya ikisini kullanmak isteyebilirsiniz. Sadece
    kullandığınız lexer yerine, neden kullanmadığınız lexerlara yükleme
    zamanı harcayasınız? Gerçek sebep bu olsa da olmasada, bence yine de
    bu, metasınıfların kafa yorulması gereken ilginç bir yönü –
    meta-işlerinin nerede ve ne zaman yapıldığını seçmenize olanak
    sağlayan muhteşem esnekliği.

### Sonuç

Bu makaleyi yazmaktaki amacım Pythondaki metasınıfların nasıl
çalıştığını açıklamak ve gerçek Python kodundan sağlam metasınıf
kullanım örnekleri göstermekti. Metasınıfların kötü bir şöhreti olduğunu
biliyorum, çoğu insan bunları olması gerektiğinden daha fazla sihirli
olarak görüyor. Benim bu konudaki düşüncem, diğer dil yapılarında olduğu
gibi, metasınıfların bir *araç* olduğu ve programcının sonuçta bunu
doğru kullanmaktan sorumlu olduğu. Her zaman iş gören en basit kodu
yazın, ama ihtiyacınız olanın metasınıflar olduğunu hissederseniz,
bunları kullanmakta özgürsünüz.

Umarım bu makale sınıfların oluşturulması ve kullanılması için
metasınıfların sağladığı esnekliği göstermiştir. Örnekler metasınıfların
uygulanması ve kullanılmasında çeşitli yönlerini göstermiştir;
`__init__`,`__new__` ve `__call__` metotlarının üstüne yazılması,
metasınıfın miras alınması, sınıflara özellikler eklenmesi, obje
metotlarının statik metotlara dönüştürülmesi ve gerek sınıf tanımında
gerekse de örneklenme zamanında optimizasyonlar yapılması.

Python içinde metasınıfların kullanılmasının en dikkate değer örnekleri
muhtemelen ORM (Object Relational Mapping) çatılarıdır, Django’nun
modellerinde olduğu gibi. Gerçekten, bunlar metasınıfların neler
yapabileceğini göstermekte güçlü örneklerdir, ancak ben bunları burada
göstermemeye karar verdim çünkü onların kodları karmaşık ve birçok
alana-özel detaylar metasınıfları sergilemek olan asıl amaca zarar
verirdi. Diğer yandan, bu makaleyi okumuş olmakla, daha karmaşık
örnekleri anlamak için gereken herşeye sahip oldunuz.

Ekleme: Eğer metasınıfların diğer ilginç örneklerini bulursanız lütfen
bana bildirin. Daha fazla gerçek-hayat kullanımı görmekle bir hayli
ilgileniyorum.

### Referanslar

-   Resmi belgelerdeki [Data model sayfası][]
-   [Python’da metasınıf programlama][] – metasınıfları açıklayan bir
    dizi makale
-   [What is a metaclass in Python?][] – muhteşem bir StackOverflow
    tartışması.
-   [Python 2.2 içinde type ve sınıfları birleştirme][] – Guido von
    Rossum tarafından yazılan metasınıflara da dokunan bir hayli bilgi
    verici makale
-   `__new__` ve `__init__` arasındaki fark konusunda [bir StackOverflow
    tartışması][] .
-   [metasınıfların sağlam kullanımı][] hakkında bir diğer
    StackOverlflow tartışması. .

  [Eli Bendersky]: http://eli.thegreenplace.net/
    "Eli Bendersky's website  "
  [Python metaclasses by example]: http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example/
  [birinci-sınıf objeler]: http://en.wikipedia.org/wiki/First-class_object
  [bakınız]: http://docs.python.org/library/functions.html#property
  [pygments]: http://pygments.org/
  [Data model sayfası]: http://docs.python.org/reference/datamodel.html
  [Python’da metasınıf programlama]: http://www.ibm.com/developerworks/linux/library/l-pymeta/index.html
  [What is a metaclass in Python?]: http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
  [Python 2.2 içinde type ve sınıfları birleştirme]: http://www.python.org/download/releases/2.2.3/descrintro
  [bir StackOverflow tartışması]: http://stackoverflow.com/questions/4859129/python-and-python-c-api-new-versus-init
  [metasınıfların sağlam kullanımı]: http://stackoverflow.com/questions/392160/what-are-your-concrete-use-cases-for-metaclasses-in-python