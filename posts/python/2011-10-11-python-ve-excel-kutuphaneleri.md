<!--
.. date: 2011-10-11 04:12:00
.. title: Python ve Excel Kütüphaneleri
.. slug: excel-kutuphaneleri
.. description: Python ile Excel dosyalarını okumak veya excel dosyası yazmak için bu yazıyı okuyun. Kısa ve öz yazı size gereken temelleri verecek.
-->


Eğer Python ile excel dosyaları okumak veya yazmak istiyorsanız doğru
yerdesiniz. Çeşitli Python kütüphaneleri ile excel dosyaları üzerinde
işlem yapmak çocuk oyuncağı.

Python ile Excel dosyaları okumak ve yazmak, anladığım kadarıyla merak
edilen bir konu ve günlük Python kullanımında ihtiyaç duyulabilecek bir
bilgi. Bu yüzden, üstünkörü de olsa, konuya giriş için küçük bir belge
yazmak istedim. Python kullanarak Excel dosyalarıyla çalışmak için
geliştirilmiş, benim bildiğim, birkaç tane kütüphane var. Bunlardan xlwt
Excel'e yazmak, xlrd ise Excel'den okumak için hazırlanmış. Diğer bir
kütüphane olan xlutils ise, bunlar arasında bir nevi tutkal görevi
görerek, yardımcı fonksiyonlarla bu ikisini birbirine bağlıyor. Bu
yazıda, xlrd kütüphanesinden kısaca bahsedip, diğer kütüphanelere de
ileriki zamanlarda değinmek istiyorum. <!-- TEASER_END -->

**Feragat:**Aşağıda yazdıklarım çoğunlukla [burada][] bulabileceğiniz
belgenin tembel çevirisidir. Birebir çevirmedim, ama orada olanları
aktarıyorum. Bu yazıyı eğer bir şekilde başka bir platformda aynen veya
değiştirerek yeniden yayınlayacaksanız, ki yayınlayabilirsiniz, orjinal
metine atıfta bulunmanız gerekir. 

### Kurulum

Yukarıda adı geçen paketlerin hepsine pypi üzerinden ulaşılabilir. Yani
eğer sisteminizde setuptools kuruluysa, ki değilse kurmalısınız,
`easy_install paket_adi` komutuyla bunlardan herhangi
birini yükleyebilirsiniz. pip ile de aynı şekilde
`pip install paket_adi` komutuyla yükleyebilirsiniz. Kök
dizinine yazma hakkı olmayanlar, --user anahtarıyla kurulumu ev
dizinlerine yapabilirler (pip veya easy\_install farketmez.).
Zannediyorum çoğu gnu/linux dağıtımının resmi veya kullanıcı
depolarından da bu kütüphanelere ulaşılabilir. İsterseniz bu paketleri
teker teker kurabilirsiniz, ama benim tavsiyem xlutils paketinin
kurulması, xlutils ile birlikte gerekli xlrd ve xlwt paketleri, ayrıca
bazı diğer paketler de kurulmuş oluyor. Böylece, Python ile excel
dosyalarıyla çalışmak için gereken tüm kütüphaneleri tek bir komutla
yüklemiş oluyorsunuz.

### Python ile Excel Dosyaları Okumak

#### Çalışma Kitabı Açmak

Çalışma kitabı açmak için, xlrd paketi ile gelen open\_workbook
fonksiyonu kullanılıyor. Bu fonksiyona ilk argüman olarak dosya yolunu
verirseniz, o dosyayı okuyup, ilişkili bir `xlrd.Book`
sınıfı döndürüyor. Dolayısıyla bu dosyayla çalışmak için dönüş değerini
bir değişkene atamalısınız.

    :::python
    from xlrd import open_workbook
    a = open_workbook("birexceldosyasi.xls")
    
    # alternatif olarak:
    
    with open("birexceldosyasi.xls","rb") as dosya:
        # dosyayı binary olarak açtığımıza dikkat ediniz.
        a = open_workbook(file_contents=dosya.read())
    
    # Ayrıca, file_contents olarak mmap objesi de verebilirsiniz.
    # bkz: http://docs.python.org/library/mmap.html

#### Çalışma Kitabında Gezinme

Bir çalışma kitabı açtıktan sonra, muhtemelen bu dosyanın içerisinde
gezinip bazı satır ve sütünlardan bilgi almak isteyeceksiniz. Bunun için
`xlrd.Book` objesinin bazı metotlarından yararlanacağız,
aşağıdaki örneği inceleyelim.

    :::python
    from xlrd import open_workbook
    
    a = open_workbook("dosyaadi.xls")
    
    # Bir çalışma kitabı, birkaç farklı çalışma sayfadan oluşur. Her sayfada farklı bir tablo vardır.
    # bunlara erişmek için xlrd.Book.sheets() metodunu kullanabiliriz.
    
    for sayfa in a.sheets():
        # Bu satırda sayfa değişkenine bir xlrd.sheet objesi atandı.
        
        print "Çalışma sayfası: " + sayfa.name
        
        # sayfadaki satır sayısına nrows ile ulaşıyoruz.
        for satir in range(sayfa.nrows):
            degerler = []
            
            # Sütün sayısına ncols üzerinden ulaşıyoruz
            for sutun in range(sayfa.ncols):
                # cell metodu bize bir hücre döndürüyor, value ile değer okuyoruz.
                values.append(sayfa.cell(satir, sutun).value)
            print "\t".join(degerler)
        print

#### Çalışma Kitabını İncelemek

`open_book()` ile dönen xlrd.Book sınıfı bir çalışma
kitabıyla ilgili tüm bilgileri tutar. Bu sınıfın nsheets özelliği,
çalışma sayfalarının sayısını tutar. Bu sayıyı sheet\_by\_index
metoduyla birlikte kullanmak, çalışma sayfalarını almak için en sık
kullanılan yoldur.

`sheet_names` metodu, çalışma sayfalarının adını döndürür.
Nasıl sheet\_by\_index metoduyla belli bir sıradaki çalışma sayfasını
alabiliyorsak, sheet\_by\_name metodunu kullanarak, belli bir isimdeki
çalışma sayfasını alabiliriz. Ayrıca, `sheets` metodu da
tüm çalışma sayfalarının bir listesini döndürür.

    :::python
    a = open_book("birexceldosyasi.xls")
    
    # Index'e göre sayfaları alma
    for i in range(a.nsheets):
        print a.sheet_by_index(i)
    
    # Isime göre sayfaları alma
    for name in a.sheets_names():
        print a.sheet_by_name(name)
    
    for sayfa in a.sheets():
        print sheet
    

#### Çalışma Sayfasını İncelemek

Yukarıda bahsedilen herhangi bir metot ile elde edeceğiniz
`xlrd.sheet.Sheet` objesi, bir çalışma sayfasıyla ilgili
tüm bilgileri tutar. Bu objenin `name` özelliği bu sayfanın
adını tutar. `ncols` ve `nrows` ise sırasıyla
bu sayfadaki sütun ve satır sayısına karşılık gelir.

    :::python
    sayfa = a.sheet_by_index(0)
    for satir_no in range(sayfa.nrows):
        for sutun_no in range(sayfa.ncols):
            print sayfa.cell(satir_no, sutun_no).value

#### Sayfa İçeriğinin Topluca Alınması

Yukarıda üstünkörü bahsettiğim hücre hücre erişim dışında, bir gurup
hücredeki bilgileri toplu halde de alabilirsiniz.

    :::python
    # import'lar burada ...
    a = open_workbook("bir dosya")
    sayfa0 = a.sheet_by_index(0)
    
    # col ve row sırasıyla bir sütun ve satır döndürür. (cell objeleri listesi olarak)
    
    satir0 = sayfa0.row(0)
    sutun0 = sayfa0.col(0)
    
    # row_slice ve col_slice ise, belli bir satır ve sütunun bir dilimini döndürür.
    
    # 1. satirin 5. sütundan itibaren olan kısmı
    k = sayfa.row_slice(1,5)
    
    # 1. (sayfaya 0'dan başlayarak..) satirin 5 ile 10 sütünları arası
    g = sayfa0.row_slice(1,5,10)
    
    # col_slice'de aynı şekilde çalışıyor.
    
    # row_values ve col_values, yukardaki row_slice ve col_slice gibidir.
    # ancak, xlrd.sheet.Cell objesi yerine, direk hücrenin değerlerinin
    # bir listesini döndürür.
    
    # İlk satirdaki tüm hücrelerin değerleri
    birinci_satir_degerleri = sayfa0.row_values(0,0)

### Sonuç Olarak

xlrd kütüphanesinin burada bahsetmediğim birkaç özelliği daha var, ama
ben detaylara girmeden konuya giriş yapmış olmak istediğimden, sadece
temel özelliklere değindim. İleriki zamanlarda,xlwt ve xlutils ile
ilgili açıklamaları da blog'uma eklemek istiyorum, ama zaman ne
getirecek bilemeyiz.

  [burada]: http://www.simplistix.co.uk/presentations/python-excel.pdf
    "Working with Excel files
    in Python"