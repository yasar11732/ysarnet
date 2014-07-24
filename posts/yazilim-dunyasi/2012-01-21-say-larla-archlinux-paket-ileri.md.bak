<!--
.. date: 2012-01-21 11:07:57
.. slug: sayilarla-archlinux-paketcileri
.. title: Sayılarla ArchLinux Paketçileri
.. description: Çeşitli linux komutlarıyla toplanan verilerden, matplotlib kullanarak çizilmiş bir bar grafiği.
-->

Ben doğuştan manyak olduğum için, arada istatistik toplayıp grafik
çiziyorum. Bu seferki grafikte, ArchLinux geliştiricilerinin ne kadar
paket yapımına katkıda bulunduğunu görebilirsiniz. <!-- TEASER_END -->

![Arch Linux packagers by number of packages graph](/images/arch-linux-packagers.png)

Kaynak:

    :::bash
    cd /var/abs
    find -name 'PKGBUILD' -exec cat '{}' \; | egrep '(Maintainer|Contributor)' | cut -d: -f 2 | sed 's///' | sort | uniq -c | sort -nr