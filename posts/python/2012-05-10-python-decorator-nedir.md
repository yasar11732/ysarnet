<!--
.. date: 2012-05-10 04:00:56
.. title: Python ve decorator... Nedir, ne işe yarar?
.. slug: decorator
.. description: Python'da fonksiyon adlarından önce gelen, '@' ile başlayan ve fonksiyonları modifiye eden decorator'ler neler yapılır, nasıl kullanılır?
-->


Python dilindeki decorator'ları anlamadan önce, fonksiyonların Python
dilinde "first class citizen" olduklarını bilmek gerekir. "first class
citizen" birebir çevirildiğinde, birinci sınıf vatandaş demek.
Programlama dilleriyle ilgili kullanıldığında bu deyim, o dildeki bir
varlığın, şu özellikleri taşıdığı anlamına gelir;

-   Çalışma anında oluşturulabilir.
-   Parametre olarak geçirilebilir.
-   Fonksiyonlardan döndürülebilir.
-   Bir değişkene atanabilir.

Python'da fonksiyonların birinci sınıf objeler olduğunu anlamak o kadar
da zor değil. Python'daki her şey gibi, fonksiyonlar da birer obje. Ve
biz, objelerin yukarıdaki tüm özellikleri taşıdıklarını biliyoruz.
Dolayısıyla, fonksiyonlar da bu özellikleri taşıyor. <!-- TEASER_END -->

Pythondaki objelerin bir diğer özelliği de, diğer fonksiyonlar
içerisinde tanımlanabilmeleri. Örneğin, aşağıdaki kod Python dilinde
tamamen normal bir koddur.

    :::python
    def yazdiricifonksiyon(yazi):
      def gereksiz():
         print yazi
      return gereksiz
    
    merhabade = yazdiricifonksiyon("merhaba")
    merhabade()
    """
    Ekrana şunu basar:
    merhaba
    """

Yukarıdaki örnekte, fonksiyonların nasıl birinci sınıf vatandaş
olduklarını görüyoruz. İlk satırda tanımladığımız fonksiyon
çağırıldığında, kendi içerisinde gereksiz isminde bir fonksiyon
oluşturuyor. Daha sonra, bu fonksiyon, yazdiricifonksiyon'un dönüş
değeri olarak döndürülüyor. Gördünüz gibi, bu fonksiyonu bir değişkene
atayabiliyor ve istediğimizde çağırabiliyoruz.

Python'daki bu özellik sayesinde, şöyle şeyler de yapmak mümkün;

    :::python
    def acikla(fonksiyon):
     print "Su fonksiyonu cagiriyorum: %s" % fonksiyon.__name__
      return fonksiyon()
    
    acikla(gereksiz)
    """
    Su fonksiyonu cagiriyorum: gereksiz
    """
    def unlemekle(f,*args,**kwargs):
     return f(*args,**kwargs) + "!"
    
    def yazidondur(yazi):
     return yazi
    
    unlemekle(yazidondur,"osman")
    """
    'osman!'
    """

Yukarıdaki örneklerden göreceğiniz gibi, argüman olarak fonksiyon alan
fonksiyonlar sayesinde, asıl fonksiyon çağrılmadan önce fazladan bir iş
yapabilir veya, fonksiyonun dönüş değeri üzerinde düzenleme yapabiliriz.

İşte decorator'lar da, tam bu işi yapmaya yarıyor. Python'da
decorator'lar, argüman olarak fonksiyon alıp, sonuçta yine fonksiyon
döndüren fonksiyonlara deniyor. Örneğin;

    :::python
    def kalinyaz(f):
      def wrapper():
          return "" + f() + ""
     return wrapper
    
    def osman():
      return "osman"
    
    kalinosman = kalinyaz(osman)
    kalinosman()
    """
    '<b>osman</b>'
    """
    osman()
    """
    'osman'
    """

Yukarıdaki örnekte, kalinyaz bir decorator. Bu fonksiyon, argüman olarak
bir fonksiyon alıp, yine bir fonksiyon döndürüyor. Döndürdüğü fonksiyon
çağırıldığında, asıl fonksiyonun dönüş değeri, html \ tagları
arasına alınıyor.

Python bu işi kolaylaştırmak için, bize decorator söz dizimi gibi bir
kolaylık da sağlıyor. O da şöyle;

    :::python
    @kalinyaz
    def yasar():
        return "yasar"
    yasar()
    """
    '<b>yasar</b>'
    """

Burada @ işaretiyle, fonksiyona uygulamak istediğimiz decorator'u
belirtiyoruz. Bunun yukarıda yaptığımızdan pek bir farkı yok aslında.
Tek özelliği daha temiz ve düzenli görünmesi.

Özetle, Python'daki her şey gibi, fonksiyonlar da birer obje ve bu
nedenle fonksiyonlar diğer fonksiyonlara argüman olarak verilebilir veya
fonksiyonlardan döndürülebilir. Python'un bu özelliğini, fonksiyonlar
üzerinde oynamalar yapmak için kullanabiliriz.

Bu yazı giriş niteliğinde olduğu için, decorator'lardan sadece yüzeysel
olarak bahsettim. Eğer bu konuyla ilgiliyseniz, [Python wiki'nin ilgili
sayfasında][] çeşitli amaçlara yönelik profesyonelce yazılmış birçok
decorator bulup inceleyebilirsiniz.

  [Python wiki'nin ilgili sayfasında]: http://wiki.python.org/moin/PythonDecoratorLibrary