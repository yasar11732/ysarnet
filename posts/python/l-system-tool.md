<!--
.. date: 2014/07/14 08:33
.. slug: l-system-tool
.. title: Python L-Sistemi Aracı
.. description: Python Tk ile yazdığım L Sistemi çizme aracının beta sürümü github'da
-->

Merhabalar,

Birkaç gün önce blog'dan [Python kullanarak Fraktal şekiller](fractal.html) çizmek ile ilgili bir
yazı yazmıştım. O yazıyı yazdıktan sonra, turtle'ın bu tarz grafikleri çizmek için fazla yavaş
bir kütüphane olduğunun farkına vardım. Ayrıca, çok pratik de değildi.

İnternette gördüğüm [l-sistem çizen](http://www.kevs3d.co.uk/dev/lsystems/) websayfası çok hoşuma gitti,
bir benzerini Python ile yazmaya karar verdim. <!-- TEASER_END -->

Kodların ilk sürümü, [tklsystem](https://github.com/yasar11732/tklsystem) github deposunda. Bu sürüme
beta demeye karar verdim, çünkü henüz pek denemedi bu program.

Kodları windows üzerinde, Python 3.4.1 ile yazdım. Python 2.x sürümleriyle ne kadar uyumlu çalışır emin değilim.
Programın Py2 versiyonuyla ilgilenmek isteyeniniz varsa, github'dan fork etmeyi unutmayın.

Programı kullanmak için PIL kütüphanesine ihtiyacınız olacak. Windows için gerekli kurulum dosyalarını [Gayri-resmi Python kurumları](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
sayfasından ulaşabilirsiniz. Linux için hangi paketleri yüklemek gerekir henüz tam emin değilim, kendi dağıtımınızın paketlerini biraz kurcalayın.

<a href="http://i.imgur.com/KHkV5Uq.png" target="_blank"><img src="http://i.imgur.com/KHkV5Uq.png"/ style="width:850px"></a>

Program yukarıdaki resimde gördüğünüz gibi bir arayüze sahip. Sol üstteki yazı kutucuklarına istediğiniz parametleri girdikten sonra, Enter'a veya
alttaki render tuşuna basarak, ortadaki görüntüyü güncelleyebilirsiniz. Kutucuklar şu işlere yarıyor;

 - **Iterations**: Axiom kaç kez büyütülecek. Bu sayı arttıkça oluşacak resim giderek komplex olacağı için, özellikle karmaşık sistemlerde
 fazla büyük rakamlar kullanmayın. Önce 4-5 gibi bir rakam deneyin. Daha fazla detay istiyorsanız, detayları artırabilirsiniz.
 - **angle**: Dönüş Açısı
 - **Axiom**: Başlangıç Durumu
 - **rule1, rule2, rule3, rule4**: Büyüme kuralları. Değişen ve yerine gelecek kısımları iki nokta (:) ile ayırın.
 - **constants**: Sabitler. Bunlar çizgiye dönüşmez, büyümeyi kontrol etmek için kullandığınız fazladan değişkenler.
 
Program'da bazı sabitler öntanımlı geliyor. Onların kullanımı da şu şekilde;

 - **+, -**: Sağa dön, sola dön
 - **[, ]**: Pozisyon ve açıyı kaydet, veya son kayıtlı pozisyon ve açıya geri dön.
 - **1,2,3,4**: Aktif rengi değiştir.
 
Programın ön tanımlı renklerini sol tarafta görebilirsiniz. Bunları üstüne tıklayarak, renkleri değiştirebilirsiniz.

Eğer denediğiniz bir şekli beğendiyseniz, bunun denklemini `save` tuşuyla bir metin belgesine kaydedebilir, daha sonra bunu tekrar yükleyebilirsiniz.

Ayrıca, o anki görüntüyü resim olarak da kaydedebilirsiniz.

En sağda, programlar birlikte gelen, veya sizin kaydettiğiniz dosyaları görecekseniz, bunları da seçerek yükleyebilirsiniz.

Böyle şeylere meraklı olanlarınız bir denesin, istek & şikayet doğrultusunda, vaktim olursa, gerekli düzenlemeleri de yapabilirim. Hiç olmadı siz
yapar github'dan pull request gönderirsiniz, o şekilde yaparız.

Sağlıcakla.