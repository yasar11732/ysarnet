<!--
.. date: 2011-08-25 19:35:00
.. title: Git Deposundan Alt Dizin Ayrıştırma 
.. slug: git-deposunu-bolme
.. description: git submodülleri aracılığıyla, bir git deposu içerisinde başka bir git deposu barındırabilirsiniz. Bu yöntemle, mevcut git deposunu iki ayrı depoya dönüştüreceğiz.
-->

Eğer kodlarınızı bir git deposunda tutuyorsanız ve bu depoyu iki ayrı
depo haline getirmek istiyorsanız, bu yazı işinize yarayabilir. Benim
böyle bir ihtiyacım vardı, ve bulduğum [Stackoverflow sorusu][]
sayesinde, geçmişi kaybetmeden, git depomu iki ayrı git deposu haline
getirdim. <!-- TEASER_END -->

Önce, ne yapacağımıza biraz daha dikkatli bakalım, şu haldeki git
deposunu:

<pre>
DIZIN1/
		.git/
		DIZIN2/
		DIZIN3/
</pre>

Şu hale getireceğiz:

<pre>
DIZIN1/
		.git/
		DIZIN2/
DIZIN3/
		.git/
</pre>

İşlemlere başlamadan önce, **tüm deponuzu yedekleyin.** Herhangi bir
hata olması durumunda, verilerinizi kaybedebilirsiniz. İlk yapacağımız
şey, depoyu klonlamak:

    :::terminal
    git clone --no-hardlinks /DIZIN1 /DIZIN3

Şu anda, DIZIN3 içerisinde, tüm git geçmişiniz bulunuyor. Şimdi geçmişi
filtreden geçirip, sadece alt klasöre ait geçmişin kalmasını
sağlamalıyız. Bu komutu, klonladığınız git deposu içerisinde verin.

    :::terminal
    git filter-branch --subdirectory-filter DIZIN3 HEAD

Şu anda, bütün git geçmişiniz, sanki deponun kök dizini DIZIN3'müş gibi
yeniden yazılmış olmalı. Daha sonra, depoyu resetlememiz lazım.

    :::terminal
    git reset --hard

git gc komutuyla, gereksiz dosyaları silelim.

    :::terminal
    git gc --aggressive

Son olarak da, git prune komutuyla işlemimizi bitiriyoruz. Bu komut,
dosyalarımızla, geçmişimizin birbirine uyumlu olduğundan emin olmamızı
sağlıyor.

    :::terminal
    git prune

Artık yeni git deponuz hazır olmalı, büyük deponuzu içerisinden de bu
alt dizini silip, yeni bir commit ile bu dizini çıkarabilirsiniz.
İsterseniz yeni deponuzu alt modül olarak tekrar ilk deponuza
ekleyebilirsiniz. Böylece, eğer bu iki depo birbirine bağımlıysa,
kodlarınız doğru çalışmaya devam eder.Yalnız, **git push komutunun alt
modülleri göndermediğini aklınızda çıkarmayın.**Yeni dizin kendi başına
bir depo olduğundan, git pull ve git push komutlarını bu dizin
içerisinden ayrıca vermelisiniz.

  [Stackoverflow sorusu]: http://stackoverflow.com/questions/359424/detach-subdirectory-into-separate-git-repository