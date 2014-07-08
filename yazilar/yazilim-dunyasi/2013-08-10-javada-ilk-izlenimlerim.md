<!--
.. date: 2013-08-10 12:27:22
.. slug: javada-ilk-izlenimlerim
.. title: Java'da ilk izlenimlerim
.. description: Java nesne yönelimli, hata yapması zor, biraz da kasıntı bir dil. Bir süre denedikten sonra söyleyebilirim ki, Java beni pek sarmadı.
-->

Uzun zamandır java'yı denemek istiyordum ama nedense içten içe
ayak diretiyordum. Şu günlerde biraz java öğrenmek için
fırsatım oldu. Java diliyle ilgili ilk izlenimlerimi buradan
paylaşayım dedim. Daha önce Python ve C gibi dillerle ufak
tefek programlar yazan bana, Java bir hayli farklı geldi.
Şimdilik alışamadığımı söylemem gerek.

Java dilinin en belirgin özelliklerinden birisi, Türkçe'ye nesne
yönelimli programlama diye çevrilen "Object-oriented
programming" paradigmasına sahip bir dil olması. Python'da da sınıflar
ve objeler var ancak Java tam anlamıyla bir NYP dili. Beni
billenler bilir, C++ ve genel anlamda NYP konusuna karşı
biraz antipatim var. <!-- TEASER_END -->

Bakın [git mail grubundaki bir e-posta](http://thread.gmane.org/gmane.comp.version-control.git/57643/focus=57918)
gösteriyor ki [Linus Torvalds](https://plus.google.com/+LinusTorvalds)
da bu konuda bana katılıyor, ya da ben de ona katılıyorum da denilebilir.
[NYP'nin iğrenç olduğunu savunanlar](http://harmful.cat-v.org/software/OO_programming/why_oo_sucks) da mevcut.
Nedendir tam bilmiyorum, NYP bir türlü içime sinmiyor.
Java'nın NYP'yi destekleyen ama zorlamayan versiyonu olsa tam benlik
olurdu diye düşünüyorum.

Java'nın bir nevi sevdiğim yanı, programlama hatalarına karşı
baştan önlem alması olabilir. Bir kere C'den alışık olduğum
(Python'un aksine) statik veri tipi kontrolü var. Bu static tip olayı
yerine göre güzel yerine göre rahatsız edici olabiliyor
bence. Örneğin, hızlıca birşey yazıp sonuç almak
istediğimde hemen Python'la birşey yazabiliyorum.
Duck-typing olayı sayesinde Python bunu pek dert etmiyor. Ancak biraz
daha büyük birşey yazacaksam, statik veri tipi herşeyin
kontrol altına alınmasında yardımcı olması açısından
güzel bence.

Java *Exception handling* konusunda bir hayli sıkı. Her method,
hangi Exception'ları fırlatabileceği (throw'un en güzel
çevirisi budur, her türlü tartışırım!) belirtmek zorunda. Ve eğer bir
exception fırlatabilecek bir metod çağırırsanız, bu
exception'ı yakalamak zorundasınız. İşte bu çok güzel birşey bence.
Beklenmedik bir şekilde programın patlamasına engel olur
diye düşünüyorum.

Java'nın kıl olduğum bir yanına gelirsek, basitçe halledilebilmesi
gerektiğini düşündüğüm bazı şeylerin bana biraz fazla
komplike gelmesi. Örnekler verecek olursam, bir [dış komut
çağırmak] ve [dosya okumak] buna örnek olarak
gösterilebilir. Açıkcası java'nın kendi
kütüphalerinin bu tarz şeyler için neden basit fonksiyonlar
tanımlamadığına hayret ediyorum şu anda.

Bu arada, Java ile ufak bir program yazmaya çalıştım,[yas github deposu]
üzerinden ulaşabilirsiniz. Mutlaka bir sürü
acemi hatalarıyla dolu olacaktır. Bir hışımla yazdım. Bana
çalışıyor gibi görünüyor ama, bir sürü hatası olabilir.

  [dış komut çağırmak]: http://www.javaworld.com/javaworld/jw-12-2000/jw-1229-traps.html?page=1
  [dosya okumak]: http://www.mkyong.com/java/how-to-read-file-from-java-bufferedreader-example/