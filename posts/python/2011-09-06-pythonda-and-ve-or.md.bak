<!--
.. date: 2011-09-06 10:57:00
.. title: Python'da and ve or
.. slug: and-ve-or
.. description: Python'da mantıksal "and" ve "or" bağlaçlarının özellikleriyle alakalı bir yazı. 
-->

Python'daki and ve or dil yapısının biraz akılda kalması güç bir
özelliği var. Bu yüzden buraya biraz özet geçmek istedim. Daha sonra
kendim ve başkaları referans olarak bakabilelim diye. <!-- TEASER_END -->

### and

`and` dil yapısı, yanlış ile karşılaştığında, o öğeyi direk
döndürür. Eğer yanlış öğe bulamazsa, son öğeyi döndürür. Yanlış olarak
değerlendirilebilecek öğeler, boş `str`, `list`, `dict` nesneleri, 0, False veya `None`
olabilir. Bunların dışında neredeyse herşey doğru olarak
değerlendirilir.

    :::python
    "K = 'b' olur, tüm öğeler doğru olduğu için, son öge döndürülür."
    K = "a" and "b"
    
    "K = 0 olur. İlk yanlış öge olduğu için 0 döner."
    K = 0 and "b"
    
    " K = 0 olur, İki yanlış öge olsa da, ilk yanlış öğe olan 0 döndü."
    K = "a" and 0 and "" and "c"
    
    def x():
        print "x fonksiyonu"
        return True
    
    "0 döner, x() çalışmaz. İlk öge yanlış olduğu için, ikinci öge degerlendirilmeye çalışılmaz."
    0 and x()
    

### or

`and` yapısının tersine `or` yapısı ilk doğru
ögeyi döndürmeye çalışır.

    :::python
    "K = [] olur, tüm öğeler yanlış olduğu için, son öğe döner."
    K = 0 or []
    
    "K = 'b' olur. 'b' ilk doğru öğedir."
    K = 'b' or 0
    
    " K = 'a' olur, 'a' ilk doğru öğedir."
    K = None or {} or False or "a" or "c"
    
    def x():
        print "x fonksiyonu"
        return True
    
    "0 yanlış olarak değerlendirildiği için, x() fonksiyonu çalışır ve değeri döndürülür."
    0 or x()
    

### Zincirleme

`and` ve `or` zincirlendiğinde soldan sağa
doğru, sırasıyla değerlendirme yapılır.

    :::python
    " 'yasar' döner. 1 and 'yasar', 'yasar' olarak değerlendirilir. 
    "'yasar' or 'b', 'yasar' olarak değerlendirilir. "
    1 and "yasar" or "b"
    
    """
    'osman' döner.
    0 and 'yasar', 0 olarak değerlendirilir. Dönen 0, 'osman' ile karşılaştırılır.
    0 or 'osman', 'osman' olarak değerlendirilir ve bu değer döner. 
    """
    0 and "yasar" or "osman"
    
	"""
    1 döner. 
    1 or 'yasar', 1 olarak değerlendirilir. Dönen 1 ile 'osman' karşılaştırılır.
    1 and 'osman', 1 olarak değerlendirilir.
    """
    1 or "yasar" and "osman"
    
    """
    'osman' döner.
    0 or 'yasar' => 'yasar'
    'yasar' and 'osman' => 'osman'
    """
    0 or "yasar" and "osman"

### If Yapısıyla and-or kullanımı

`and` ve `or`, `if` yapısıyla
birlikte kullanıldığında, bunlardan dönen değer, if ile değerlendirilir.

    :::python
    # If içerisine girmez. '' and "b" den '' döner, if bunu yanlış olarak değerlendirir.
    if '' and "b"
    
    # If içerisine girer. "" or "b" den "b" döner. if "b"yi doğru olarak değerlendirir.
    if "" or "b"
    
    # If içerisine girmez. 0 or None içinde doğru öğe olmadığı için, son öğe olan None döner.
    if 0 or None
    
    # If içerisine girmez. 0 or None, 0 döndürür. 0 yanlış olarak değerlendirilir.
    if 0 and None