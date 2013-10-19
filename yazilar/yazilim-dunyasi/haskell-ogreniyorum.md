<!-- 
.. date: 2013/10/13 12:51:18
.. description: Haskell, tamamen fonksiyonel, zarif ve ifade gücü yüksek bir dil. Örnek kodlar ve kullanım alanlarını anlattım.
.. title: Haskell Öğreniyorum
.. slug: haskell-tanitim
-->

Hazır tatil, boş vaktim varken Haskell öğrenmeye bir şans daha vereyim dedim. Bir yandan
öğrenirken, bir yandan da ufak bir [Haskell tanıtımı](http://learnyouahaskell.com/introduction) yapayım (bkz: araklamak).

Haskell **tamamen fonksiyonel** bir dil. İmperatif dillerde, programa hangi adımları izleyeceğini
adım adım anlatıp, neyin nasıl yapılacağını anlatıyoruz. Fonksiyonel dillerde ise, neyin ne olduğunu
belirtiyoruz, nasıl yapılacağına program kendi karar veriyor.

Haskell **tembel** bir dil. Haskell size bir sonuç göstermek zorunda kalmadıkça, fonksiyon çalıştırmaz.
Örneğin, bir liste döndüren bir fonksiyonu çalıştırıp, ilk iki elemanını ekrana basmak istediğinizde,
Haskell ilk iki elemanı bulacak kadar fonksiyonu çalıştırıp, orada bırakıyor.

Haskell, **statik tipleme** kullanıyor. Yani, derleme sırasında bir takım hataları yakalayabiliyorsunuz. Ayrıca,
C'nin aksine, çıkarım yapma yoluyla veri tiplerini bulabiliyor. Örneğin, `a = 5` derseniz, `a`'nın bir int
olduğunu belirtmenize gerek yok, Haskell kendi anlıyor.

Haskell **zarif ve ifade gücü yüksek** bir dil. Python'dan hatırlayacağınız, *list comprehension* yapısı Haskell
kaynaklı. Ne kadar az kod, o kadar kolay bakım gereksinimi ve o kadar az bug demek. <!-- TEASER_END -->

## Haskell Örnek Kodlar

	:::haskell
	primesTo m = eratos [2..m]  where
	   eratos []     = []
	   eratos (p:xs) = p : eratos (xs `minus` [p, p+p..m])
	   
Yukarıda, *sieve of eratosthenes* yöntemiyle asal sayıları bulan bir fonksiyon görüyoruz. `primesTo` fonksiyonu tek bir
argüman alıyor, ve `eratos` isminde bir başka fonksiyonu 2'den başlayıp o sayıya kadar olan sayılaradan oluşan bir liste
ile çağırıyor.

`eratos` fonksiyonu iki farklı şekilde çağırılabilecek şekilde yazılmış. Eğer boş listeyle çağırılırsa, boş liste döndürüyor.
Eğer, bir liste ile çağırılırsa, p bu listenin ilk elemanı, ve xs geriye kalan elemanlarından oluşan bir liste değerini alıyor.

Çıktı olarak da, ilk elemanı p, geriye kalan elemanları ise başka bir eratos fonksiyonundan gelen liste olan bir liste döndürüyoruz.
İkinci fonksiyona verdiğimiz argüman, xs listesinden p ve katları çıkarılmış hali. `minus` fonksiyonu'nun ayrıca tanımlanması gerekiyor.

## Kullanım alanları

Haskell ile geçirdiğim süre içerisinde, Haskell kullanıcılarının genelde matematikçi olduğun gördüm. Haskell ile
yazılmış uygulamalara baktığımda ise, denklemlerin doğruluğunu kanıtlayan programlar, parser ve derleyiciler, ayrıca
tam olarak ne işe yaradığını bilemediğim ama çok zeki birşeymiş gibi duran bazı programlar var.

Ayrıca, wiki klonu, çeşitli oyunlar, web server vs. de yazılmış. Yani, normal insanlara göre şeyler de
yazılabiliyor demek ki Haskell ile.

