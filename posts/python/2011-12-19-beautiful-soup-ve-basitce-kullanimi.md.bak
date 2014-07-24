<!--
.. date: 2011-12-19 07:13:00
.. title: Python Beautiful Soup Kütüphanesi ve Basitçe Kullanımı
.. slug: beautiful-soup-ve-basitce-kullanimi
.. description: HTML ve XML dosyalarını işlemek için kullanabileceğiniz BeautifulSoup kütüphanesinin özelliklerini ve kullanımını öğrenmek için okuyun.
-->

Python'da HTML ve XML dosyalarını işlemek için, genelde acemi kullanıcılar,
düzenli ifadeleri kullanır. Ancak düzenli ifadeler hem hata yapması kolay bir
alandır, hem de bu iş için verimli değildir. Diğer yandan, BeautifulSoup gibi
bu iş için tasarlanmış, performanslı ve kullanımı kolay bir kütüphanedir.

Beautiful Soup Python için bir HTML ve XML ayrıştırıcısıdır (parser).
Beautiful Soup kütüphanesi kullanışlı olmasını şu özelliklerine
borçludur: <!-- TEASER_END -->

1.  Beautiful Soup kötü girdi verseniz bile bozulmaz. Neredeyse orjinal
    belgenizle aynı anlama gelen bir ayrıştırma ağacı (parse tree)
    döndürür. Bu özellik çoğu zaman gereken bilgiyi almanız için
    yeterlidir.
2.  Beautiful Soup bir ayrıştırma ağacında kolayca gezinme (traversing),
    arama ve düzenleme yapmanıza olanak sağlayan birçok metot ve Python
    vari deyimler sağlar: her uygulama için baştan HTML veya XML
    ayrıştırıcı yazmanıza gerek kalmaz.
3.  Beautiful Soup gelen belgeleri Unicode'a, giden belgeleri de UTF-8'e
    kendiliğinden çevirir. Kodlamalarla uğraşmanıza gerek kalmaz.

[Beautiful Soup resmi web sitesi][]

### Beautiful Soup Örnekleri

    :::python
    # -*- coding : utf-8 -*-
    from BeautifulSoup import BeautifulSoup
    basit_html = """
    Başlık buraya>/title>
    Paragraf 1Paragraf 2
    """
    soup = BeautifulSoup(basit_html)
    
    print soup.html.head.title
    # ekrana "Başlık buraya" yazar.
    
    print len(soup('p'))
    # 2 yazar. Belgedeki p tagı sayısı
    
    print soup('p', {"class": "hebele"})
    # [Paragraf 2] -> class="hebele" olan tagların listesi.
    
    head = soup.html.head
    print head
    #Başlık buraya
    
    head.next
    #Başlık buraya
    head.next.string
    # u'Başlık buraya'
    
    # tag'ın özelliklerine, tag sanki sözlükmüş gibi erişebiliyoruz.
    soup.find('p',{"class" : "hebele"})["class"]
    # u'hebele'
    
    for i in soup.body:
        print i    
    
    # Paragraf 1
    # Paragraf 2

[BeautifulSoup belgeleri] ve [lxml - Python ile XML ve HTML ayrıştırma] de ilginizi çekebilir.

  [Beautiful Soup resmi web sitesi]: http://www.crummy.com/software/BeautifulSoup/
  [BeautifulSoup belgeleri]: http://www.crummy.com/software/BeautifulSoup/documentation.html
    "Beautiful Soup Belgeleri"
  [lxml - Python ile XML ve HTML ayrıştırma]: http://lxml.de/ "lxml - Python ile XML ve HTML ayrıştırma"