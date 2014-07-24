<!--
.. date: 2011-08-31 16:34:00
.. title: Python'da str Objesini Genişletmek
.. slug: str-objesini-genisletmek
.. description: Python'da Immutable (oluşturulduktan sonra değiştirilemeyen) sınıfların alt sınıflarını oluştururken karşılaşılabilecek sorunlar ve çözümleri
-->


Python'da str ve unicode gibi objelerin alt sınıflarını oluşturmak
istediğinizde, biraz sıkıntıya düşebilirsiniz. Bunlar, yerinde
değiştirilemeyen nesneler olduğu için, bunların metotlarını kullanmak,
kendi objenizin kaybolmasına neden olur. Bu problemin önüne geçmek için,
`__getattribute__()` metodunun üzerine yazabilirsiniz. Aşağıdaki
örnekte, çoğul eki, iyelik eki ve ismin hallerini bulan bununla
birlikte, bir unicode objesinin de tüm metotlarına erişebilen bir sınıf
tanımlayacağız. <!-- TEASER_END -->

    :::python
    # -*- coding:utf-8 -*-
    kalin = (u"a",u"ı",u"o",u"u")
    ince = (u"e",u"i",u"ö",u"ü")
    
    yumusayan = {
        u"k": u"ğ",
        u"t": u"d",
        u"p": u"b"
    }
    
    sertlestirenler = (u"f",u"s",u"t",u"k",u"ç",u"ş",u"h",u"p")
    
    class kelime(unicode):
    
        def __getattribute__(self, isim):
            "unicodedan gerekli metodu alır, sonucu kelime olarak döndürür."
            att = super(kelime, self).__getattribute__(isim)
    
            if not callable(att):
                return att
    
            def sonra_cagir(*args, **kwargs):
                sonuc = att(*args, **kwargs)
                if isinstance(sonuc, unicode):
                    return kelime(sonuc)
                return sonuc
            return sonra_cagir
            
        def __add__(self,other):
            "iki kelimeyi unicode toplamıyla toplar, sonucu kelime olarak döndürür"
            return kelime(unicode.__add__(self,other))
            
        def __mul__(self,other):
            "bir kelimeyi bir sayıyla unicode olarak çarpar. Sonucu kelime olarak döndürür"
            return kelime(unicode.__mul__(self,other))
        
        @property
        def lar(self):
            "Kelimeye çoğuk eki ekler"
            for harf in reversed(self):
                if harf in kalin:
                    return kelime(self + u"lar")
                elif harf in ince:
                    return kelime(self + u"ler")
                    
            return kelime(self + u"lar")
        
        @property
        def in_(self):
            "kelimeye iyelik eki ekler"
            _kelime = self
            if _kelime[-1] in yumusayan:
                _kelime = _kelime[:-1] + yumusayan[_kelime[-1]]
            elif _kelime[-1] in kalin:
                return kelime(_kelime + u"nın")
            elif _kelime[-1] in ince:
                return kelime(_kelime + u"nin")
            
            for harf in reversed(_kelime):
                if harf in kalin:
                    return kelime(_kelime + u"ın")
                elif harf in ince:
                    return kelime(_kelime + u"in")
            
            return kelime(_kelime + u"ın")
        @property   
        def e(self):
            "kelimeye ismin e halini ekler"
            _kelime = self
            if _kelime[-1] in yumusayan:
                _kelime = _kelime[:-1] + yumusayan[_kelime[-1]]
            elif _kelime[-1] in kalin:
                return kelime(_kelime + u"ya")
            elif _kelime[-1] in ince:
                return kelime(_kelime + u"ye")
            
            for harf in reversed(_kelime):
                if harf in kalin:
                    return kelime(_kelime + u"a")
                elif harf in ince:
                    return kelime(_kelime + u"e")
            
            return kelime(_kelime + u"a")
        
        @property
        def i(self):
            "kelimeye ismin i halini ekler"
            _kelime = self
            
            if _kelime[-1] in yumusayan:
                _kelime = _kelime[:-1] + yumusayan[_kelime[-1]]
            elif _kelime[-1] in kalin:
                return kelime(_kelime + u"yı")
            elif _kelime[-1] in ince:
                return kelime(_kelime + u"yi")
            
            for harf in reversed(_kelime):
                if harf in kalin:
                    return kelime(_kelime + u"ı")
                elif harf in ince:
                    return kelime(_kelime + u"i")
            
            return kelime(_kelime + u"ı")
        @property   
        def de(self):
            "kelimeye ismin de halini ekler."
            if self[-1] in sertlestirenler:
                ek = u"t"
            else:
                ek = u"d"
            
            for harf in reversed(self):
                if harf in kalin:
                    return kelime(self + ek + u"a")
                elif harf in ince:
                    return kelime(self + ek + u"e")
            
            return kelime(self + u"da")
        @property   
        def den(self):
            "kelime ismin den halini ekler"
            return kelime(self.de + u"n")

Yukarıdaki örneği şu şekilde çalıştırabilirsiniz.

    :::python
    a = kelime(u"yaşar")
    """
    Normalde unicode'a ait metotları kullanmak, farklı bir unicode döndürmesi
    gerekir. Ama __getattribute__ metodunun üzerine yazarak, bunun üstesinden geldik.
    """
    type(a.lower()) # <class 'kelime'>
    """
    Her defasından kendi sınıfımız döndürüldüğü için, unicode sınıfının ve kendi sınıfımızın metotlarını
    istediğimiz gibi zincirleyebiliriz.
    """
    print(a.capitalize().lar.de) # "Yaşarlarda"
    type(a.lar.capitalize().de) # <class 'kelime'>
    print(a + " hebele") # "yaşar hebele"
    type(a + hebele) # <class 'kelime'>

Bu sistemin bütün mahareti, `__getattribute__()` içinde tanımladığımız
sonra\_cagir fonksiyonu. Örneğin, `kelime.lower()` çağırıldığında,
aslında çalışan fonksiyon şöyle oluyor.

    :::python
    sonuc = unicode.lower(self)
    if issubclass(sonuc,basestring):
        # sonuc bir unicode idi, döndürmeden önce bunu tekrar kelime yapıyoruz.
        return kelime(sonuc)
    
    # unicode objesinin bazı metotları, yazı harici şeyler döndürebilir. Bu durumlarda
    # ne aldıysak onu döndürüyoruz.
    return sonuc