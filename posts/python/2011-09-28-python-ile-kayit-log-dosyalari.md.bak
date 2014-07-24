<!--
.. date: 2011-09-28 12:03:00
.. slug: kayit-log-dosyalari
.. title: Python ile kayıt (log) dosyaları
.. description: Log dosyaları oluşturmak veya konsola düzgün formatta çıktı vermek için logging modülü'nün nasıl kullanılabileceği örnekleriyle açıklanıyor.
-->

Son uğraştığım ufak programda Python'un logging modülünü kullanarak
kayıt işlemleri yapıyorum. Kısaca nasıl yapıldığını açıklayayım dedim.

Python ile logging modülü kullanmak için gereken ilk iş, logging
modülünü içe aktarıp, `getLogger` ile yeni bir kayıt tutucu
oluşturmak. Bunun nasıl yapıldığını görmek için, aşağıdaki örnek python
kodunu inceleyelim. <!-- TEASER_END -->

    :::python
    import logging
    
    # "benim-program-ana-modul" adında yeni bir kayıtçı al
    ana_modul_kayitci = logging.getLogger("benim-program-ana-modul")
    # bu kayıtçı debug seviyesinde kayıt yapsın.
    ana_modul_kayitci.setLevel(logging.DEBUG)

Daha sonra, bu kayıtçı için en az 1 tane handler (bundan sonra işleyici
olarak bahsedilecek) eklememiz gerekiyor. Bu işleyicilerin çoğu
logging.handlers içersinde bulunurken, aşağıda kullandığım iki tanesi,
doğrudan logging modülü içerisinde tanımlanmış. Daha önce belirttiğim
gibi sadece bir tane işleyici yetecektir, ben örnek oluşturması için,
iki tanesini aşağıdaki python kodundan belirttim.

    :::python
    # logging modulünde tanımlanmış dosyaya kaydedici.
    # argüman olarak kayıt dosyasının yolu.
    dosya = logging.FileHandler("benim-program-ana-modul.log")
    
    # logging modülünde tanımlanmış standart çıktıya kaydedici
    standard_cikti = logging.StreamHandler()

Böylece, elimizde iki adet işleyici var (logging.StreamHandler ve
logging.FileHandler). Bu işleyicilerin görevi, kayıt tutulmasını
istediğiniz bilgileri gerekli şekillerde kullanmak. Örneğin yukarıdaki
örnekte, bir işleyicinin görevi, kayıt altına alınan bilgileri ekrana
basmak (logging.StreamHandler), bir diğerinin görevi ise, kayıt altına
alınan bilgileri dosyaya kaydetmek (logging.FileHandler). Bunlar gibi
daha birkaç çeşit çekirdek python modüllerinde tanımlanmış [kayıt
işleyiciler][] var. Şimdi bunlara çıktı formatı ekleyelim. Bunun için
logging.Formatter kullanacağız. İkisine ayrı ayrı çıktı formatı
eklenebilir, Örnekte tek bir format oluşturup, iki işleyici için de bunu
kullanacağım.

    :::python
    # Örn: 2011-09-28 11:45:58,394 - hebele [CRITICAL]: kayıtçı hazır
    log_format = logging.Formatter('%(asctime)s - %(name)s [%(levelname)s]: %(message)s')
    
    dosya.setFormatter(log_format)
    standart_cikti.setFormatter(log_format)

Böylece kayıt işleyicilerimiz için kayıt formatı belirledik. Bu formatı
kişisel zevklerinize ve ihtiyaçlarınıza göre düzenleyebilirsiniz. Şimdi
tek ihtiyacımız bu işleyicileri kayıt tutucumuza eklemek, böylece kayıt
dosyası oluşturmaya hazır hale geleceğiz.

    :::python
    ana_modul_kayitci.addHandler(dosya)
    ana_modul_kayitci.addHandler(standart_cikti)
    
    # artık kayıt tutmaya hazırız.
    
    ana_modul_kayitci.info("kayıt tutucu hazır") # bilgi mesajı
    ana_modul_kayitci.warning("Kendine mukayyet ol!") # uyarı mesajı
    ana_modul_kayitci.critical("Elektirikler kesildi!") # Kritik bilgi
    ana_modul_kayitci.error("Elim kapıya sıkıştı.") # Hata mesajı
    ana_modul_kayitci.debug("Nefes aldım.") # hata ayıklama mesajı
    ana_modul_kayitci.debug("Nefes verdim.") # hata ayıklama mesajı
    ana_modul_kayitci.debug("Tekrar nefes aldım.") # hata ayıklama mesajı
    

Böylece python'da logging modülünü kullanarak kayıt işlemi yapmış olduk.
Kolay Gelsin.

  [kayıt işleyiciler]: http://docs.python.org/library/logging.handlers.html