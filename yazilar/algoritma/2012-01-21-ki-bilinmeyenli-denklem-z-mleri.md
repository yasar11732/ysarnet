<!--
.. date: 2012-01-21 01:17:00
.. title: İki bilinmeyenli denklem çözümleri
.. slug: iki-bilinmeyenli-denklem-cozumleri
.. description: Bu yazıda çeşitli iki bilinmeyenleri denklerimlerin python ile çözümünün örnekleri verilmiş. Bu fonksiyonları günlük ihtiyaçlar için kullanabilirsiniz.
-->

Dün Python ile, iki bilinmeyenli denklem çözümleriyle ile birşeyler
yazdım. Paylaşayım dedim. Sonuncusunun biraz daha elden geçmesi lazım,
ama aşağı yukarı çalışıyor. <!-- TEASER_END -->

    :::python
    # -*- coding: utf-8 -*-
    from math import sqrt
    
    def gereksiz(toplam, carpim):
        """
        a + b = toplam
        a * b = carpim
        return a,b
        >>> gereksiz(8,15)
        (3.0, 5.0)
        >>> gereksiz(7,12)
        (3.0, 4.0)
        >>> gereksiz(12,35)
        (5.0, 7.0)
        """
        carpim, toplam = float(carpim), float(toplam)
        try:
            terim1 = sqrt((toplam / 2) ** 2 - carpim)
        except ValueError:
            return (None, None)
        terim2 = toplam / 2
        buyuk = terim1 + terim2
        kucuk = terim2 - terim1
        return (kucuk, buyuk)
    
    def gereksiz2(fark, carpim):
        """
        a - b = fark
        a * b = carpim
        return a,b
        >>> gereksiz2(7,30)
        (3.0, 10.0)
        >>> gereksiz2(2,35)
        (5.0, 7.0)
        >>> gereksiz2(7,78)
        (6.0, 13.0)
        """
        kucuk, buyuk = gereksiz(fark, -carpim)
        try:
            return (buyuk, -kucuk)
        except TypeError:
            return (None, None)
    
    def gereksiz3(toplam, bolum):
        """
        a + b = toplam
        a / b = bolum
        return a,b
        >>> gereksiz3(240,5)
        (200.0, 40.0)
        >>> gereksiz3(6,2)
        (4.0, 2.0)
        >>> gereksiz3(15,4)
        (12.0, 3.0)
        """
        b = float(toplam) / (bolum + 1)
        a = toplam - b
        return (a,b)
    
    def gereksiz4(fark, bolum):
        """
        a - b = fark
        a / b = bolum
        return a,b
        >>> gereksiz4(15,2)
        (30.0, 15.0)
        >>> gereksiz4(4,2)
        (8.0, 4.0)
        >>> gereksiz4(15,4)
        (20.0, 5.0)
        """
        a,b = gereksiz3(fark, -bolum)
        return (a, -b)
    
    def gradient(a,s,p):
        terim1 = sqrt(s - a)
        alttaraf = sqrt((terim1 - (p / a)) ** 2)
        usttaraf_1 = (p / (a ** 2)) - float(1) / (2 * terim1)
        usttaraf_2 = terim1 - (p / a)
        return (usttaraf_1 * usttaraf_2) / alttaraf
    
    def mesafe(a, s, p):
        return abs(sqrt(s - a) - (p / a))
    
    def gereksiz5(s,p,hata=1.0e-15,maxdeneme=100):
        """
        a + b ^ 2 = s
        a * b = p
        için YAKLAŞIK olarak, DENEME YANILMA yoluyla a ve b değerleri bulur.
        işlemler genelde 100 denemeden daha önce bitmeli, eğer çok uzarsa,
        hata değerini artırın.
        """
        a = sqrt(p) / 2
        up_limit = s
        down_limit = -s
        #print "a değerinden başlanıyor: ", a
        m = mesafe(a,s,p)
        prev_m = m
        weight = 1
        counter = 0
        while  m> hata:
            counter += 1
            if counter >= maxdeneme:
                break
            try:
                #print "a=>",a, "hata=>",mesafe(a,s,p)
                grad = gradient(a,s,p)
                #print "gradient:", grad
                a_deneme = a - (1 / (weight * grad))
                m = mesafe(a_deneme,s,p)
                while m > prev_m:
                    counter += 1
                    if counter >= maxdeneme:
                        break
                    a_deneme = a - (1 / (weight * grad))
                    m = mesafe(a_deneme,s,p)
                    weight *= 2
                    #print "weight:",weight, "a:", a_deneme, "hata=>",m
                a = a_deneme
                prev_m = m
            except ValueError:
                print "Valüü erör"
                break
        #print "hata=>",mesafe(a,s,p)
        #print counter,"denemede sonuç bulundu."
        b = p / a
        #return (round(a,2),round(b,2))
        return (a,b)