<!--
.. date: 2011-09-17 18:14:00
.. title: Python ile Çeşitli Yazılım Geliştirme Desenleri (Design Patterns)
.. slug: cesitli-yazilim-gelistirme-desenleri
.. description: Design patterns, yazılım geliştirirken sıkça karşılaşılan problemlere tekrar tekrar kullanılabilecek çözümler sunar. Bu yazıda, çeşitli yazılım geliştirme desenlerinin Python ile kullanımı anlatılacak.
-->

İnsan programlamayı kendi çabalarıyla öğrenince, işin okulunu okumuş
insanlardan bazı konularda eksik kalıyor. En azından ben böyle
hissediyorum. Hem aradaki açığı kapatmak, hem de kendimi geliştirmek
adına, birkaç yazılım geliştirme deseni öğrenmek ve bunları Python ile
uygulamaya geçirmek istedim. Bunu yapmanın hem kendi gelişimime faydası
olacağını düşünüyorum, hem de bunu okuyan birkaç kişinin, en azından
konuya giriş yapmış olması açısından, işini kolaylaştıracağını
zannediyorum. <!-- TEASER_END -->

### Singleton

Bu desende, bir sınıfın sadece tek bir sınıf örneği (class instance)
oluşturmasını sağlayacak bir mekanizma oluşturuyoruz.Böylece programın
tüm parçalarının tek bir obje üzerinden işlem yapmasını
sağlayabiliriz<sup>[1]</sup>. Benim uygulamam şu şekilde oldu.

    :::python
    class singleton(object):
        instance = None
     def __new__(cls,*args,**kwargs):
            if cls.instance is None:
                cls.instance = super(singleton, cls).__new__(cls,*args,**kwargs)
            return cls.instance
     def __init__(self):
         if not hasattr(self,"sayi"):
                self.sayi = 5
    
    """        
    >>> a = singleton()
    >>> a.sayi
    5
    >>> a.sayi += 3
    >>> a.sayi
    8
    >>> b = singleton()
    >>> b.sayi
    8
    >>> 
    """

Burada, `instance` isminde bir sınıf değişkeni tuttum. Bu
sınıf değişkenini `None` olarak ayarladım. Bildiğiniz gibi,
`__new__()` metoduyla yeni bir sınıf örneği oluşturulmasını
kontrol ediyoruz. Burada, eğer `instance` değişkeni
`None` ise, yeni bir örnek oluşturup, bunu
`instance` değişkenine atıyorum. Daha sonra, her yeni sınıf
örneği oluşturulmaya çalışıldığında, daha önce oluşturmuş olduğum örneği
döndürüyorum.

`__new__()` metodu her çalıştığında, eğer bir sınıf örneği
döndürüyorsa, `__init__()` metodu da çalışıyor. Bu yüzden,
her seferinde `__init__()` metodunda yapılan işlerin
yinelenmesi, her yeni sınıf çağırılışında, burada tanımlanan değerlerin
sıfırlanması anlamına geliyordu. Bu yüzden, örneğe ait yeni bir değişken
oluştururken, bunun daha önce var olmadığından emin olmak gerekiyor.
Böylece üstüne yazmamış oluyoruz.

Bir google aramasıyla birkaç farklı singleton uygulanışı bulmak mümkün.
Benim bulduklarım arasından en ilginç gelen [bir SO sorusundaki] dekoratör
fonksiyon. Ancak yine de, kendi yazdığım şekli bana daha düzgün bir
kodlama gibi geliyor. Tabii ki bunlar kişisel görüşlere bakan şeyler.

### Sorumluluk Zinciri (Chain Of Responsibility)

Bu yöntem zannımca en çok olay yönetiminde kullanılıyordur. Örneğin
arayüz uygulamalarının çeşitli klavye ve fare olaylarını halledişi gibi.
Bu desende, bir objeden bir iş istediğinizde, mesela bir tuşa basılma
olayının halledilmesi gerektiğinde, eğer bu işi kendi üstlenebiliyorsa,
kendi üstleniyor, yoksa, ebeveyn objeden bu işi yapmasını istiyor.
Ebeveyn obje de aynı şekilde kendisi yapamıyorsa, bir üst objeye
yönlendiriyor ve böylece bir sorumluluk zinciri oluşturulmuş oluyor. Bu
deseni uygulamak için, oluşturduğumuz objenin iki yapıyı kurması
gerekiyor. Birincisi, hangi işi yapabileceğine karar vermek için gereken
bir mantık, ikincisi de ebeveyn objeye ulaşması için gereken bir erişim
noktası. Gerçek hayatta kullanılamayacak kadar aptal bir örnek olsa da,
şöyle birşey yazdım bununla ilgili:

    :::python
	class StringHandler(object):
		def __init__(self,parent=None):
			self.parent = parent
			self.canHandle = []
		def handle(self,string):
			if string in self.canHandle:
				self._handle(string)
			elif self.parent != None:
				self.parent.handle(string)
			else:
				self.defaultHandler(string)
		def _handle(self,string):
			print("handled by %s" % self)
		def defaultHandler(self,string):
			print("default handled by %s" % self)
	 
			 
	class osmanHandler(StringHandler):
		def __init__(self,parent=None):
			super(osmanHandler,self).__init__(parent)
			self.canHandle = ["osman"]
	 
		 
	class orhanHandler(StringHandler):
		def __init__(self,parent=None):
			super(orhanHandler,self).__init__(parent)
			self.canHandle = ["orhan"]
	 
	"""     
	>>> a = osmanHandler()
	>>> a.handle('osman')
	handled by <__main__.osmanHandler object at 0x026D6910>
	>>> a.handle('orhan')
	default handled by <__main__.osmanHandler object at 0x026D6910>
	>>> b = orhanHandler(a)
	>>> b.handle('orhan')
	handled by <__main__.orhanHandler object at 0x026D6810>
	>>> b.handle('osman')
	handled by <__main__.osmanHandler object at 0x026D6910>
	>>> b.handle('cengiz')
	default handled by <__main__.osmanHandler object at 0x026D6910>
	>>> 
	"""

Burada, aslında hiçbir işe yaramayan bir sınıf tanımladım. Bu sınıfın,
`canHandle` listesi, bu sınıfın hangi yazıların
işlenmesinden yükümlü olduğunu belirtiyor. Daha sonra, bu sınıftan miras
alan iki yeni sınıf daha tanımladım. Bunlardan birinin işi "osman"
kelimesini işlemek, diğerinin işi de "orhan" kelimesini işlemek gibi
düşünebilirsiniz. Bu sınıfların yeni bir örneğini oluştururken, hangi
sınıfın bunun ebeveyni olacağını belirleyebiliyoruz. Eğer belirtmezsek,
bu sınıf en tepe sınıfmış gibi kabul edilecek. Herhangi bir sınıfın
`handle(string)` metodu çağırıldığında, kendisi bu yazıyı
işleyebiliyorsa işleyecek, işleyemiyorsa, bir üst objeye gönderecek.
Tepeye kadar işlenmeden gelirse, ve tepe obje de bunu işleyemezse,
öntanımlı metod (defaultHandler) çalışacak.

### Ara objeler (Proxy)

Bu desende, asıl objeye, başka bir obje üzerinden ulaşılıyor. Bunun
amacı, asıl objeye erişimi kontrol etmek. Asıl objeye erişimi neden
kontrol etmek isteyeceğiniz programınızın gereksinimlerine göre değişir.
Ben göstermelik olsun diye, şöyle birşey yaptım.

    :::python
    class kibar(object):
        def __init__(self,main):
            self.main = main
        def __getattribute__(self,attribute):
           main = super(kibar,self).__getattribute__("main")
           if attribute == "main":
             return main
         if not attribute.endswith("_lutfen"):
               raise AttributeError("Kibar olun! -> %s_lutfen" % attribute)
         
            return getattr(main,attribute.rstrip("_lutfen"))
        def __getitem__(self,key):
          return self.main[key]
       def __setitem__(self,key,item):
         self.main[key] = item
       def __str__(self):
          return self.main.__str__()
    
    """   
    >>> a = kibar('osman')
    >>> a
    
    >>> str(a)
    'osman'
    >>> print(a)
    osman
    >>> b = kibar([1,2,3])
    >>> b.append(5)
    
    Traceback (most recent call last):
      File '', line 1, in 
        b.append(5)
      File '', line 9, in __getattribute__
        raise AttributeError('Kibar olun! -> %s_lutfen' % attribute)
    AttributeError: Kibar olun! -> append_lutfen
    >>> b.append_lutfen(5)
    >>> print(b)
    [1, 2, 3, 5]
    >>> b.extend_lutfen([7,8,9])
    >>> print(b)
    [1, 2, 3, 5, 7, 8, 9]
    >>> b.extend
    
    Traceback (most recent call last):
      File '', line 1, in 
        b.extend
      File '', line 9, in __getattribute__
        raise AttributeError('Kibar olun! -> %s_lutfen' % attribute)
    AttributeError: Kibar olun! -> extend_lutfen
    """

Burada kullandığım yöntemin herhalde en can sıkıcı noktası çift alt
çizgili bütün metotların tek tek üzerine yazmanın gerekliliği. Çünkü, bu
metotları çağırmak için `__getattribute__()` metodu
kullanılmıyor. Bunun üstesinden gelmek için, zannediyorum bir çok
akrobasi yapılabilir, ancak, onlara girmeye yeltenmeyeceğim bile.

**Düzenleme:** Onun için de şöyle birşey düşündüm:

    :::python
    def MakeProxy(obje):
       from collections import Counter
     class proxy(obje):
          def __init__(self,*args,**kwargs):
                            super(proxy,self).__init__(*args,**kwargs)
                            self.counter = Counter()
                    def __getattribute__(self,attr):
                            counter = super(proxy,self).__getattribute__("counter")
                            if attr == "counter":
                                return counter
                            counter[attr] += 1
                            return super(proxy,self).__getattribute__(attr)
            return proxy
    """
    >>> list_proxy = MakeProxy(list)
    >>> a = list_proxy((1,2,3,4))
    >>> a
    [1, 2, 3, 4]
    >>> a.extend([7,8,9])
    >>> a
    [1, 2, 3, 4, 7, 8, 9]
    >>> a.counter['extend']
    1
    >>> dict_proxy = MakeProxy(dict)
    >>> b = dict_proxy({})
    >>> b
    {}
    >>> b['osman'] = 'arabaci'
    >>> b
    {'osman': 'arabaci'}
    >>> b.keys()
    ['osman']
    >>> b.counter['keys']
    1
    
    """

  [1]: http://www.python.org/workshops/1997-10/proceedings/savikko.html#sec:singleton
    "Design Patterns in Python"
  [bir SO sorusundaki]: http://stackoverflow.com/questions/42558/python-and-the-singleton-pattern/2752280#2752280
  
*[SO]: Stack Overflow