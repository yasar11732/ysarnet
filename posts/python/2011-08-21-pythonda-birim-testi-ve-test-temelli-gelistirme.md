<!--
.. date: 2011-08-21 23:30:00
.. title: Python'da Birim Testi ve Test Temelli Geliştirme
.. slug: birim-testi-ve-test-temelli-gelistirme
.. description: Python kullanarak birim testi nasıl yapılır? Test odaklı yazılım geliştirme yöntemi nedir? Örnekleriyle bu yazıda anlatılıyor.
-->


Yazılım geliştirmede birim testi, kısaca, yazılımı oluşturan birimlerin
belirlenen girdiler ve beklenen çıktılar kullanılarak, programatik
olarak test edilmesidir. Birim ile kastedilen olgu bahsi geçen konuya
göre değişebilse de, genelde, bir programı oluşturan en küçük parçadır.
Test temelli geliştirme ise, birimi geliştirmeye başlamadan önce, bu
birimden beklenenlerin belirlenip, beklentiye uygun testler
yazılmasıdır. Daha sonra, tüm testler başarılı oluncaya kadar birimin
geliştirilmesine devam edilir.

Birim testlerinin ve test temelli yazılım geliştirmenin birkaç avantajı
vardır. [dive into python][]'da bu avantajları çok iyi anlatmış, orayı
çevirmekle yetineceğim:

-   Kod yazmadan önce, sizi gereksinimlerinizi faydalı bir şekilde
    detaylandırmaya zorlar.
-   Kod yazarken, sizi gereksiz kod yazmaktan kurtarır. Tüm testler
    başarılıysa, kod yeterli demektir.
-   Kodları yenilerken, yeni sürümün eskisi gibi davrandığından emin
    olmanızı sağlar. (Benim en sevdiğim özellik!)
-   Kodların bakımını yaparken, son yaptığınız değişiklik eski kodu
    bozdu diye size bozuk atanlara karşı kendinizi savunmanızı
    sağlar.("Ama birim testleri başarılı oldu...")
-   Bir ekip çalışması yapıyorsanız, kodlarınızın diğer geliştiricilerin
    kodlarını bozmadığından emin olmanızı sağlar. Değişikliklerinizi
    onaylayıp, ortak depolara yollamadan önce diğer geliştiricilerin
    testlerini uygulayabilirsiniz.

Python'da birim testi yapmak için, *unittest* modülü kullanılır. Testler
*unittest* modülündeki *TestCase* sınıfının bir alt sınıfında yazılır.
Bu alt sınıfın, adı test ile başlayan tüm metotları, farklı bir test
tanımlar. Bu metotların içerisinde, TestCase sınıfının belirli
metotlarıyla, birimin beklenen davranışı sergileyip sergilemediği test
edilir.[Python Belgelerinin unittest ile ilgili bölümü][]'nde belirtilen
bu metotlar şunlardır: <!-- TEASER_END -->


| Metot                     | Neyi Test Eder   | Gerekli Versiyon  |
|---------------------------|------------------|-------------------|
| assertEqual(a, b)         | a == b           |                   |
| assertNotEqual(a, b)      | a != b           |                   |
| assertTrue(x)             | bool(x) is True  |                   |
| assertFalse(x)            | bool(x) is False |                   |
| assertIs(a, b)            | a is b           | 2.7               |
| assertIsNot(a, b)         | a is not b       | 2.7               |
| assertIsNone(x)           | x is None        | 2.7               |
| assertIsNotNone(x)        | x is not None    | 2.7               |
| assertIn(a, b)            | a in b           | 2.7               |
| assertNotIn(a, b)         | a not in b       | 2.7               |
| assertIsInstance(a, b)    | isinstance(a, b) | 2.7 
| assertNotIsInstance(a, b) | not isinstance(a, b) | 2.7


2.7'de eklenen özellikler, Python 2.3'den sonrası için unittest2
modülüyle sağlanıyor. Bu modülü ayrıca indirip kurarak bu özellikleri de
kullanabilirsiniz. Yukarıda bahsedilen metotlara ek olarak, şu iki metot
da mevcuttur.


| Metot                                                 | Kontrol eder                                                                            | Gerekli Versiyon |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------|------------------|
| assertRaises(exc, asdf, \*args, \*\*kwargs)           | asdf(\*args, \*\*kwargs) exc hatası verir.                                              |                  |
| assertRaisesRegexp(exc, re, asdf, \*args, \*\*kwargs) | asdf(\*args, \*\*kwargs) exc hatası verir, ve hata mesajı re düzenli ifadesiyle eşleşir | 2.7              |


*assertRaisesRegexp* metodunu 2.7 öncesi versiyonlarda yine unittest2
ile kullanabilirsinz.

Şimdi örnek birkaç test göstermek istiyorum. Öncelikle, neyi test
edeceğimize karar vermemiz gerek. Benim aklıma bir karakter dizgesi
olarak 4 işlemden oluşan bir matematiksel ifadeyi alan ve sonucu
döndüren bir fonksiyon örneği yapmak geldi. Testleri yazmaya başlamadan
önce, bu fonksiyondan ne beklediğimi kesinleştirmem gerekiyor.

-   Matematiksel ifadenin sonucunu doğru vermeli :)
-   Fonksiyonumun boşluklara takılmamasını, boşluklu veya boşluksuz
    çalışmasını istiyorum
-   Çarpma ve bölmenin işlem önceliğine dikkat etmeli.
-   Negatif sayıları dikkate almalı.
-   Yanlış bir ifadeyle çağırılırsa hata vermeli.
-   Mantıksal olarak, toplama ve çarpma işlemlerinde ifadelerin yerinin
    değişmesi sonucu değiştirmemeli

Artık istediklerimizi bildiğimize testlerimizi yazmaya başlayabiliriz.
Önce unittest modülünü içe aktarıp, TestCase sınıfından, yeni bir sınıf
türetmeliyiz. (alt sınıf oluşturmalıyız.)

    :::python
    import sys
    from random import randint
    ### En güzel unittest'i bulmaya çalış :)
    
    if sys.version_info[0] == 2 and sys.version_info[1] >= 3 and sys.version_info[1] 
    
Ben platforma uygunluk konusunda biraz takıntılı olduğum için çok
uzattım. Size isterseniz basit bir "import unittest" ile unittest
modülünü içe aktarabilirsiniz. Şimdi ilk testimizi yazalım. Bu ilk test
aptal testi olacak. Fonsiyonumuz aptal mı onu test edeceğiz :)

	:::python 
	# unittest içe aktarma burada olacak
	# sonra da hayali modülü dahil etmeliyim. Bunu daha yazmadım :)
	import Hesaplayici
	class HesaplaTestler(UnitTest.TestCase):
		def testAptal(self):
			"Aptal testi"
			self.assertEqual(Hesaplayici.hesapla("2+2"),4)
    
Burada dikkat edilmesi gerek tek şey, metod ismine test ile başlamış
olmam. Metodun çalışması için, isminin test ile başlaması gerekiyor.
Metod başlangıcının hemen ardından yazılan bir satır açıklama da önemli.
Eğer testler başarısız olursa, açıklamalar içerisinde size o bir
satırlık açıklamayı da gösteriyor. Örneğin, "2+2" ile 5 eşit mi diye
sorsak (unittest.main() çağrısı, mevcut bütün testlerin çalışmasına
neden olacaktır.), şuna benzer bir çıktı verecekti.

<pre>   
F
======================================================================
FAIL: testAptal (__main__.HesaplaTestler)
Aptal Testi
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test2.py", line 19, in testAptal
    self.assertEqual(Hesaplayici.hesapla("2+2"),5)
AssertionError: 4 != 5

----------------------------------------------------------------------
Ran 1 test in 0.002s

FAILED (failures=1)
</pre>
    
Tek tek açıklamalara girmeden, bendeki testlerin son halini buraya
yapıştırıyorum. Satır aralarındaki açıklamaların yeterli olacağını
düşünüyorum.

	:::python   
	# -*- coding: utf-8 -*-
	import sys
	from random import randint
	### En güzel unittest'i bulmaya çalış :)

	if sys.version_info[0] == 2 and sys.version_info[1] >= 3 and sys.version_info[1] 

Yukarıdaki basit örnekler, kendi testlerinizi yazmaya başlamak için
yeterli olacaktır. Artık elinizde testler olduğuna göre, fonksiyonunuzu
yazmaya başlayabilirsiniz. Yapmanız gereken, kodları yazdıkça teste tabi
tutmak, ve tüm testler başarılı oluncaya kadar kodları yenilemek.
İleride bu fonksiyona yeni özellikler eklemeye çalıştığınızda bu testler
çok işe yarayacak. Eğer yeni eklediğiniz özellikler, eski özelliklere
zarar veriyorsa, testler hata vererek size bunu bildirecek. Siz de
hatayı düzeltebileceksiniz.

Bu da benim bu testlere göre yazmış olduğum fonksiyon. Bende tüm
testlerden geçti.

    :::python
    # -*- coding: utf-8 -*-
    import re
    
    class kotuGirdi(Exception):
        def __unicode__(self):
            return "Yanlış girdi kullandınız!"
            
        def __str__(self):
            return self.__unicode__()
        
        
    def hesapla(string):
        # Önce boşlukları temizle
        string = string.replace(" ","")
        
        # girdi doğru mu?
        # basta "-" veya "+" opsiyonel
        # sonra bir sayı
        # sonra, sayılar ve islemler devam ediyor
        # son olarak da bir sayı var
        
        if not re.match("^[-+]?\d[-+*/\d]+\d$",string):
            raise kotuGirdi
            
        # İşlem operatöründen sonra, * veya / olamaz -> 5 +* 2
        if re.search("[-+*/][*/]+",string):
            raise kotuGirdi
            
        # Yanyana ikiden fazla işlem operatörü olamaz
        # İki tane olması mümkün -> 10 / -3, 
        
        if re.search("[-+*/]{3,}",string):
            raise kotuGirdi
        
        # Sayılarla islecleri ayıralım:
        sayilar = []
        islecler = []
        son_tip = "islec"
        gecici = ""
        
        for i in range(0,len(string)):
            
            # son karşılaştığımız bir sayıysa
            if son_tip == "sayi":
                
                if re.match("\d",string[i]):
                    gecici += string[i]
                else:
                    sayilar.append(int(gecici))
                    islecler.append(string[i])
                    son_tip = "islec"
            elif son_tip == "islec":
                
                # en son bir işleç gördüysek, yeni bir sayı oluşturmaya başlayabiliriz.
                gecici = string[i]
                son_tip = "sayi"
        
        # En son gecicide kalan sayıyı da ekleyelim
        
        sayilar.append(int(gecici))
        
        # İşlem tanımları
        islemler = {
        "+" : lambda x,y : x + y,
        "-" : lambda x,y : x - y,
        "*" : lambda x,y : x * y,
        "/" : lambda x,y : float(x) / y
        }
        
        # çarpma ve bölme işlemi önceliği
        
        while "*" in islecler or "/" in islecler:
            for i in range(0,len(islecler)):
                if islecler[i] in ["*","/"]:
                    islem = islemler[islecler[i]]
                    
                    sonuc = islem(sayilar[i],sayilar[i+1])
                    sayilar[i:i+2] = [sonuc]
                    islecler = islecler[:i] + islecler[i+1:]
                    break
                    
        # Kalan toplama çıkarmalar:
        
        sonuc = sayilar[0]
        
        for i in range(1,len(sayilar)):
            islem = islemler[islecler[i-1]]
            sonuc = islem(sonuc,sayilar[i])
        return sonuc

  [dive into python]: http://www.diveintopython.net/unit_testing/diving_in.html
  [Python Belgelerinin unittest ile ilgili bölümü]: http://docs.python.org/library/unittest.html