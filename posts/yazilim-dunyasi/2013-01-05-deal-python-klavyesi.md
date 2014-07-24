<!--
.. date: 2013-01-05 14:07:16
.. slug: ideal-python-klavyesi
.. title: İdeal Python klavyesi
.. description: Python kodlarını tarayan ve en çok kullanılan karakter, ikili, üçlü ve kelimeleri bulan program ve programın çıktıları.
-->


Saçma sapan şeylerimi koyduğum yan bloğumda, ideal Python klavyesi
diye birşey yapmıştım. Bunu hazırlarken kullandığım kodlar aşağıda. Veri
olarak Python standard kütüphanesini kullandım, çünkü hem elimin altında
hazır vardı, hem de Python camiasında genel eğilimleri doğru bir şekilde
yansıttığını düşünüyorum. <!-- TEASER_END -->

    :::python
    from itertools import izip
    from os import walk
    from os.path import join
    from collections import Counter
    import re
    
    nonword = re.compile("\W+")
    chars = Counter()
    bigrams = Counter()
    words = Counter()
    
    for root, dirs, files in walk("C:\Python27\Lib"):
        for f in files:
            if f.endswith(".py"):
                with open(join(root,f),"r") as dosya:
                    a = dosya.read()
                    for k in a:
                        chars[k.lower()] += 1
                    for k in izip(a,a[1:]):
                        bigrams["".join(k).lower()] += 1
                    for k in nonword.split(a):
                        words[k.lower()] += 1
    
    print chars.most_common(100)
    print bigrams.most_common(70)
    print words.most_common(30)

En sık kullanılan karakterler ikililer ve kelimelerin sıklıkları da şu
şekilde:

##### Karakterler

<pre>
"boşluk" -> 0.2777 # Python kodlarının %27'sini boşluk oluşturuyor :)
"e" -> 0.0733
"t" -> 0.0504
"s" -> 0.0458
"a" -> 0.0377
"r" -> 0.0371
"i" -> 0.0343
"n" -> 0.0340
"o" -> 0.0313
"l" -> 0.0312
"enter" -> 0.0271
"f" -> 0.0214
"d" -> 0.0205
"c" -> 0.0200
"u" -> 0.0167
</pre>

##### İkililer

<pre>
"boşlukboşluk" -> 0.1825
"enterboşluk" -> 0.0207
"se" -> 0.0136
", " -> 0.0108
"in" -> 0.0092
" s" -> 0.0091
"er" -> 0.0090
"te" -> 0.0090
"el" -> 0.0086
" t" -> 0.0073
"e " -> 0.0073
"re" -> 0.0071
"st" -> 0.0070
"lf" -> 0.0067
"es" -> 0.0067
</pre>

Yukarıdaki ikilileri birleştirince `self` elde edebiliyoruz. :)

##### Kelimeler

<pre>
"self" -> 0.0066
"the" -> 0.0020
"def" -> 0.0018
"a" -> 0.0017
"if" -> 0.0016
"1" -> 0.0015
"u" -> 0.0014
"0" -> 0.0012
"in" -> 0.0011
"return" -> 0.0010
"is" -> 0.0010
"none" -> 0.0009
"assertequal" -> 0.0009
"for" -> 0.0009
"s" -> 0.0009
</pre>