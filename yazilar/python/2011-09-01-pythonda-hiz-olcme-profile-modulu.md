<!--
.. date: 2011-09-01 16:55:00
.. title: Python'da Hız Ölçme: profile Modülü
.. slug: profile-modulu
.. description: Python'da programların performansını ölçmek için, profile ve cprofile modülleri kullanılabilir. Bu modüllerin kullanımını ve örneklerini bu yazıda bulabilirsiniz.
-->

Python'da hız ölçmek için profile veya cprofile modülleri
kullanılabilir. Bu modüllerin arasındaki fark, ilkinin saf python ile
diğerinin ise C ile uygulanmış olmasıdır. Performans açısından, cprofile
modülü daha verimlidir. profile modülü, cprofile modülüne göre yavaş
kalır, ancak, saf python ile yazıldığından dolayı, genişletmeye daha
müsaittir. Bir de, bazı platformlarda, cprofile modülü bulunmayabilir. <!-- TEASER_END -->

### `profile.run('foo()')`

Bu modülün en basit kullanım şekli, bu modüldeki `run()`
fonksiyonunu kullanmaktır. Bu fonksiyon, argüman içerisinde verdiğiniz
ifadeyi çalıştırır ve ekrana bazı bilgiler yazar.

    :::python
    import profile
    def foo(bar):
        return bar * 2
    profile.run('foo(40)')

Bunun çıktısı da şuna benzer:

<pre>              
	4 function calls in 0.000 CPU seconds
    Ordered by: standart name

    ncalls  tottime  percall  cumtime  percall  filename:lineno(function)
           1   0.000    0.000      0.000   0.000  :0(setprofile)
# böyle devam ediyor.
</pre>

En üst satırda, toplam kaç fonksiyon çağırıldığı ve bunların kaç CPU
saniyesi sürdüğünü gösteriyor. Altta, gösterimin sıralamasıyla ilgili
bir bilgi var, daha sonra, öğrenmek istediğimiz bilgiler bir tablo
halinde sunulmuş. Her satırda, bir fonksiyon için bilgiler sunuluyor.
İlk sütun o fonksiyonun toplamda kaç kere çağırıldığını gösteriyor.
İkinci sütün ise, o fonksiyon içerisinde, toplamda ne kadar vakit
harcandığını gösteriyor. Ancak buna, bu fonksiyon içinde çağırılan diğer
fonksiyonların harcadığı zaman dahil değil. Bir başka deyişle, sadece bu
fonksiyon içinde yapılan işlemlerin harcadığı zaman bu hesaba dahil. 3.
sütundaki percall, tottime/ncalls değerini veriyor. Daha sonraki iki
satırda ise, alt fonksiyonların harcadığı zamanı da hesaba katarak, 2.
ve 3. satırda yapılan işlemleri tekrarlıyor. Son satırda ise, bu
bilgilerin hangi fonksiyona ait olduğu, dosyaadı:satır(fonksiyon)
şeklinde gösteriliyor.

### `profile.run('foo()','bar.txt')` ve pstats

`run()` ile hesaplanan bilgileri bir dosyaya kaydedip
yazılımınızı geliştirdikçe referans olarak kullanmak isteyebilirsiniz.
Bunu, `run("foo()","bar")` şeklinde, `run()`
fonksiyonuna ikinci argüman olarak bir dosya adı vererek yapabilirsiniz.
Böylece, ölçüm bilgileri, python'un anlayacağı bir dilde, bar isimli
dosyaya kaydolur, daha sonra, bu bilgileri okumak için pstats modülü
kullanılır.

    :::python
    import pstats
    istatistik = pstats.Stats("bar") # argüman olarak, bilgilerin tutulduğu dosyanın yolu.
    
    # Stats sınıfının bazı metotları:
    
    istatistik.strip_dirs().sort_stats(-1).print_stats()
    # modül isimlerinden fazlalık olan dosya yollarını siler, son sütuna göre sıralar, bilgileri ekrana yazar.
    
    istatistik.sort_stats('cumulative').print_stats(10)
    # en çok vakit harcayan fonksiyona göre sıralar, tepeden 10 tane listeler.
    
    istatistik.sort_stats('time').print_stats(5)
    # yukarıdaki gibi, ancak, tottime sütununa göre sıralıyor.
    
    istatistik.sort_stats('dosyaadı').print_stats('hebele')
    # dosya adına göre sıralama yapar, ve sadece içinde hebele geçen satırları listeler.
    
    istatistik.print_callers('foo')
    # bu fonksiyonu çağıranları listeler. Yukarıdaki print_stats örneklerinin hepsi print_callers ile de yapılabilir.

Burada yazılan bilgiler, muhtemelen python'da programlarınızın profilini
çıkarmaya başlamak için yeterli olacaktır. Zaten benim bildiğim de bu
kadar. Daha fazlasını öğrenmek isteyenler, [Python Profil Modülü
Belgeleri][]'ne bakabilir. Kolay Gelsin.

  [Python Profil Modülü Belgeleri]: http://docs.python.org/library/profile.html