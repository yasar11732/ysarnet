<!-- 
.. description: Parsing ve Parser kavramlarının tanımları, yöntemler, araçları ve kullanım alanları basitçe anlatıldı.
.. date: 2013/10/16 03:15
.. title: Parsing Kavramı ve Yöntemleri
.. slug: parsing-parser-topdown-operator-precedence
-->


Aslında, geçen gün yazdığım Lexer için yazdığım Parser'ı tanıtacaktım. Parse kavramı üzerine internetten
kolayca kaynak bulunabileceğini düşündüm. Ancak, biraz google araması yaptığımda karşıma gelen Türkçe
sonuçlar pek tatmin edici olmadı. Bu sebeple, önce tanıtıcı bir yazıyla başlamak istedim. Bu yazının
konuları şunlar olacak. <!-- TEASER_END -->

 * Parsing nedir, Parser nedir.
 * Parser ne işe yarar
 * Parser ve Lexer arasında nasıl bir ilişki vardır
 * Parser nasıl yapılır
 * Parser'ın kullanım alanları nelerdir
 
Muhtemelen okulda, bir cümleyi öznesine, yüklemine ayırma işlemi yapmışsınızdır. İşte parsing budur.

Parsing yapan şeye parser denir.

Parsing işlemi, genelde dil bilimi ve bilgisayar bilimi alanlarında kullanılır. Daha başka kullanım
alanları da illaki vardır. Örneğin, bence biyoistatistikçiler kesin kullanıyorlardır bu işlemi. Adamlar
o kadar DNA dizisi ile uğraşıyor sonuçta. Neyse, konumuza dönelim.

Parsing işleminin gerçekleşmesi için, iki şey gerekir, gramer kuralları ve sembol dizisi. Örneğin, Türkçe'nin
gramer kuralları var, bu sayfa da kelimeler, bağlaçlar ve noktalama işaretlerinden oluşan bir sembol dizisi. Demek
ki, bu yazı üstünde parsing işlemi uygulanabilir.

Bilgisayar biliminde parser'lar, genelde compiler veya interpreter yapmaya yönelik kullanılırlar. Bir sembol
dizisi, bu işlem sonunda yapıtaşları ve bunların birbiriyle ilişkini gösteren bir yapıya çevrilir. Eğer
bunu bir compiler (derleyici) okuyacaksa, bunlar bir kod üretmek için kullanılır. Eğer bir interpreter (yorumlayıcı)
bunu okuyacaksa, bunlar bir sonuç üretmek için kullanılır. Ya da, bunlar opcode'da çevirilip bir sanal
makinede de çalıştırılabilir. Bunlar dışında başka şekillerde de kullanılması mümkün.

Parsing yapmak için kullanılan sembol dizisi, çoğu zaman Lexer yardımı ile elde edilir. Lexer'lar, bir karakter
dizisini tokenlere bölmek için kullanılır. Bunu [Lexical analiz](/python/lexical-analiz.html) yazısında anlatmıştım.
Lexer ve Parser arasındaki en temel fark, Lexer'ın tokenler arasında sıralama ve gruplama gibi ilişkilere dikkat etmemesidir.
Bu sıralama ve gruplama mevzuları hep Parser'ın problemleridir.

Parser oluşturmak için kullanılan yöntemler, iki temel başlık altında toplanabilir.

 * Yukarıdan Aşağıya: Semboller sağa doğru tüketilir. Örneğin, bir `if` kelimesi görülür, onun sağında bir ifade olması
 beklenir, eğer varsa bu ikisi gruplanıp bir `if ifadesi` oluşturulur. Her zaman en soldaki çıkarımlar yapılır.
 * Aşağıdan Yukarıya: En basit elementler bulunur, sonra bunlardan oluşan elementler bulunur, en geniş element türü
 neyse, ona ulaşmaya çalışılır. Her zaman önce en sağdaki çıkarımlar yapılır. Eğer, shift-reduce olayını duşmuşsanız, o buna giriyor işte.
 
Yukarıdaki açıklamalarda, yukarı ve sol, sembol dizisinde önce gelenleri, aşağı ve sağ ise sonra gelenleri ifade ediyor.

Her parser net bir şekilde yukarıdaki yöntemlerden birini kullanacak diye bir şart yok. Her iki çıkarım türünden de kullanan
parser'lar da yapılabilir. Bu parser'lar üzerinde çalışan çok zeki adamlar var, bunlar sürekli farklı yöntemler üzerine
çalışıyorlar.

Parser oluşturmak için kullanılan çeşitli yazılımlara örnek olarak, yacc, bison ve ANTLR verilebilir.
