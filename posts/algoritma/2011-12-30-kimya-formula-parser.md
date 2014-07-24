<!--
.. date: 2011-12-30 10:52:00
.. title: Kimya formülü ayrıştırıcısı
.. slug: kimya-formula-parser
.. description: Python'la yazılmış bir parser örneği. Bu program element analizi yapıyor ve bir kapalı formüldeki atom miktarlarını buluyor.
-->


[Şurada][] yazmıştım, buraya da kopyalayayım dedim. Yoksa yaptığım
şeylerin takibini yapmak zor oluyor. <!-- TEASER_END -->

    :::python
    # -*- coding: utf-8 -*-
    def kimyaparser(formul):
        harfler = []
        sayilar = []
        state = 0
        sonuc = {}
        formul = formul.upper()
        
        for karakter in formul:
            try:
                karakter = int(karakter)
                #karakter bir sayı
                sayilar.append(karakter)
                state = 1 # en son bir sayı ekledik.
    
            except ValueError:
                #karakter bir harf
                if state == 1:
                    # en son bir sayı eklenmiş
                    # demek ki yeni bir atoma geçiliyor.
                    anahtar = "".join(harfler)
                    if len(sayilar) > 0:
                        deger = int("".join([str(i) for i in sayilar]))
                    else:
                        deger = 1
                    if anahtar in sonuc:
                        # eğer daha önce bu atom eklendiyse, sayıyı artır
                        sonuc[anahtar] += deger
                    else:
                        sonuc[anahtar] = deger
                    harfler = [karakter]
                    sayilar = []
                else:
                    harfler.append(karakter)
                state = 0
        # en son kalanları da ekle:
        anahtar = "".join(harfler)
        if sayilar:
            deger = int("".join([str(i) for i in sayilar]))
        else:
            deger = 1
        if anahtar in sonuc:
            sonuc[anahtar] += deger
        else:
            sonuc[anahtar] = deger
        return sonuc

Kullanımından örnek:

    :::python
    >>> kimyaparser("H2SO4")
    {'H': 2, 'SO': 4}
    >>> kimyaparser("C78H127N16S8O8")
    {'H': 127, 'C': 78, 'S': 8, 'O': 8, 'N': 16}
    >>> kimyaparser("C44189H71252N12428O14007S321")
    {'H': 71252, 'C': 44189, 'S': 321, 'O': 14007, 'N': 12428}

  [Şurada]: http://www.istihza.com/forum/viewtopic.php?f=25&t=538