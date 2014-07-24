<!--
.. date: 2012-11-13 11:06:42
.. title: Python string translate() metodu
.. slug: string-translate
.. description: Python'daki string.translate() metodu sayesinde, bir string'deki karakterleri şifreleme veya düzeltme amacıyla başka karakterle değiştirebilirsiniz.
-->


Python'da string objesinin yerleşik (built-in) metotlarından biri olan
translate() metodu, string içindeki karakterin, verilen tablodaki
(maketrans() fonksiyonu ile yapılır) karşılıklarıyla değiştirerek bir
kopyasını oluşturur. Ek olarak, bazı karakterleri silmeye de yarar.
Örneğin; <!-- TEASER_END -->

    :::python
    >>> from string import maketrans # değiştirme tablosunu yapmak için gerekli
    >>> intab = "aeiou" # değişecek karakterler
    >>> outtab = "12345" # karşılıkları
    >>> trantab = maketrans(intab, outtab) # değiştirme tablosunu oluştur.
    >>> mystr = "bu bir translate() metodu ornegidir."
    >>> print mystr.translate(trantab)
    b5 b3r tr1nsl1t2() m2t4d5 4rn2g3d3r.

Karakter silme işlemine de örnek ise şöyledir;

    :::python
    >>> from string import maketrans # değiştirme tablosunu yapmak için gerekli
    >>> intab = "aeiou" # değişecek karakterler
    >>> outtab = "12345" # karşılıkları
    >>> trantab = maketrans(intab, outtab) # değiştirme tablosunu oluştur.
    >>> mystr = "bu bir translate() metodu ornegidir."
    >>> print mystr.translate(trantab,"br") # b ve r harfleri silinecek
    5 3 t1nsl1t2() m2t4d5 4n2g3d3.