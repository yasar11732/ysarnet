<!--
.. title: Neden nikola'yı tercih ettim?
.. date: 2013-10-07 20:26
.. slug: python-nikola-static-site-generator
.. description: Günümüzün blogları statik. Python ile yazılmış statik site oluşturucu nikola'yı inceledim ve gözlemlerimi paylaşıyorum. Nikola'nın avantajlarını merak ediyorsanız okuyun.
-->


Eğer statik blog oluşturucuların size göre olmadığını düşünüyorsanız, bu yazı fikrinizi değiştirebilir. Aslına bakarsanız, artık devir statik blog devri.
Veritabanları'nın yerini markdown dosyaları ve html şablonları aldı. Statik siteler oluşturulduğu anda kullanılmaya hazır!

Statik bloglar, birtakım programlar tarafından oluşturulmuş html dosyalarından oluşturulan sitelerdir. Bu programlar, örneğin markdown gibi, bir markup dilinde
yazılmış olan dosyaları okurlar ve bunları siteyi hazırlamak için kullanırlar. Böylece ortaya, index sayfası, RSS'i, site haritası dahil her şeyiyle tam bir
site meydana gelir. Bu şekilde hazırlanmış sitelerin, alışılagelmiş blog sistemlerine göre birtakım avantajları vardır.

 - **Güvenlik:** Statik siteler, güvenlik açığı bulundurmaz. Çünkü, dinamik olarak sunulan kısımları yoktur.
 - **Verimli Kaynak Kullanımı:** Statik siteler çok az server kaynağı kullanırlar.
 - **Platform bağımsızlığı:** Statik siteler, herhangi bir sunucuda rahatlıkla barındırılabilir. Belli bir php, python sürümü veya belli bir işletim sistemi ihtiyacı yoktur.
 - **Ücretsiz Server İmkanı:** [GitHub Pages](http://pages.github.com/) statik siteler için ücretsiz hosting sağlıyor. Üstelik, bununla birlikte kendi domain adınızı kullanabilirsiniz. <!-- TEASER_END -->

Tüm bunlar göz önünde bulundurulduğunda, statik siteler bir hayli avantajlı görünüyor. Zaten, son yıllarda statik site oluşturucu programların sayısı bir hayli arttı. Birkaçını saymak gerekirse:

 - **Jekyll/Octopress:** Jekyll, yanlış hatırlamıyorsam ilk gördüğüm statik blog oluşturucu. Ruby tabanlı ve Github Page ile entegre. Github bir jekyll sitesini otomatik olarak derleyip kullanıma açıyor.
 - **Pelican:** Kullanmayı denediğim ilk Python tabanlı statik blog oluşturucu.
 - [**Nikola:**](http://getnikola.com) Şu anda kullanmayı tercih ettiğim statik blog sistemi. Yazının geri kalanından bundan bahsedeceğim.
 
Nikolayı tercih etmemde, en önemli etken Python tabanlı olması oldu. Böylece, istediğim zaman istediğim yerlerine müdahale edebiliyorum. Nikolayı denemeden önce, Pelican'ı denemiştim.
Ancak, pelican'ın bana göre bazı eksik kısımları var. Bunların başında ise, post'larınızı iç içe klasörlerde saklama imkanı vermemesi. Bu sıkıntıdan sonra bulduğum nikola ise, beni memnum
etti. Başlıca nedenlerinden bahsedeyim.

### Nikola Geliştiricisi

Nikola'nın geliştiricisi [Roberto Alsina](http://ralsina.me/weblog/) aktif olarak Nikolayı geliştirmeye devam ediyor. Github üzerinden bir issue açtığınızda, kısa bir süre
içinde geri dönüşte bulunuyor. [Nikola mail grubu](https://groups.google.com/forum/#!forum/nikola-discuss) pek az kişi tarafından kullanılsa da, Roberto Alsina orada da aktif
bir şekilde katılım gösteriyor. İstediğiniz gibi fikir alışverişinde bulunabilir, soru sorabilir veya istekte bulunabilirsiniz.

### Hızlı oluşturuyor

[Doit](http://pydoit.org/) kullandığından dolayı, yaptığı işleri keşliyor (bkz. [keşleme](http://www.idefix.com/kitap/django-mustafa-baser/tanim.asp?sid=OQFCL6MHX32LQUJYWSSU)) ve
sadece sitenizin değişen kısımlarını yeniden oluşturuyor, ki böylece [agile development](http://en.wikipedia.org/wiki/Agile_software_development) tadında bir süreçten geçiyorsunuz.
Ayrıca, otomatik değişikleri izleme modu sayesinde, siz değişiklik yaptığınız anda sitenizi derleme özelliği sayesinde, sizi bir hayli rahat ettiriyor. Ancak şunu belirtmem gerek ki,
bu özelliği Windows üzerinde çalıştırma konusunda sıkıntı yaşadım.

### Plugin sistemi

[Nikola plugin sistemi](http://getnikola.com/extending.html) temel özelliklere ekleme yapma imkanı sağlıyor. Eğer istediğiniz bir özellik nikola içerisinde yoksa, siz ekleyin olsun! Böylece nikolayı istediğiniz gibi genişletebilir,
ihtiyaçlarınız doğrultusunda yön verebilirsiniz. Başkalarının yazdığı [nikola pluginleri](http://plugins.getnikola.com/) de indirilip kullanılabilir.

3 çeşit plugin var, komut, şablon ve görev pluginleri. Komut pluginleri, aslında herhangi bir Python programı olabilir. Bunları `nikola komut_ismi` şeklinde kullanabiliyoruz.
Kullanılabilecek komutları görmek için `nikola help` komutunu kullanabilirsiniz. Görev plug'inleri ise, sitedeki verilere ihtiyaç duyulan durumlarda kullanılıyor. Bunların listesine
de `nikola list` komutuyla ulaşabilirsiniz. Eklediğiniz görev pluginleri `nikola build` komutu sırasında çalıştırılacak. Şablon pluginleri ise, Jinja ve Mako dışında bir şablon
sistemine ihtiyaç duyulduğunda kullanılıyor.

### Temaları

Nikola ile birlikte Jinja ve Mako temaları kullanabilirsiniz. Nikola ile birlite gelen temalar mako ile hazırlanmış. Şu anda 3 farklı tema ile geliyor. Bunlardan bir tanesi
base isminde, ve bu diğer temaları oluşturmak için başlangış noktası olarak kullanılıyor. Base dışında iki adet bootstrap ile hazırlanmış temalar var.

Bunları dışında hazır [nikola temaları](http://themes.getnikola.com/) indirilip kullanılabilir. Eğer `requests` kütüphanesi yüklü ise, `nikola install_theme -l` kullanılabilir temaların
bir listesini sunuyor. Bunları `install_theme` komutunu kullanarak yükleyebilirsiniz.

[Nikola temalarının](http://themes.getnikola.com/) bazıları [bootswatch](http://bootswatch.com/) desteği sağlıyor. Eğer bir bootswatch teması kullanmak istiyorsanız, `nikola bootswatch_theme -n bir_isim -s bootswatch_temasinin_ismi -p bootstrap3`
komutu ile, `bir_isim` isminde yeni bir tema oluşturup, bu temayı bootstrap3 üzerinde, istediğiniz bootswatch teması kurulmuş haliyle kullanmaya başlayabilirsiniz.

Tabi ki, hazır gelen temaları kullanmak zorunda değilsiniz. [Nikola belgeleri](http://getnikola.com/documentation.html) tema oluşturmak konusunda bazı makaleleri listelemiş, eğer baştan temalar
oluşturmak istiyorsanız, oradan başlayabilirsiniz.

### Dil Desteği

An itibariyle 10'dan fazla dil desteği var. Türkçe dil desteği de bunlara dahil. Ayrıca, henüz kendim denemedim ancak, çoklu dil desteği de var. Örneğin, bir makaleyi iki farklı dilde yazdığınızda, bir dildeki
makaleden, onun çevirisine bir dil koyuyor.

### Bir sürü ufak tefek hoşlukları

 - local_search plugin'i ile site içi arama.
 - webassets kullanarak css ve js dosyalarını tek dosya'da birleştirme
 - Dosyaları gzip ile sıkıştırarak, server taraflı bir optimizasyona gidebilme
 - Daha denemeye fırsat bulamadığım bir takım diğer özellikleri
 
### Sonuç olarak

Eğer siz de statik bir blog oluşturmak istiyorsanız nikola'ya bir şans vermenizi öneririm. An itibariyle birkaç ufak tefek sıkıntsı olsa da, kullanıma hazır bir program. Üstelik sürekli gelişmeye
devam ediyor. [Nikola El Kitabı](http://getnikola.com/handbook.html) başlangıç yapmak için gerekenleri anlatmış. Eğer github üzerinden destek vermek ve issue açmak isterseniz, [Nikola'nın github depoları](https://github.com/getnikola)
işinizi görecektir.