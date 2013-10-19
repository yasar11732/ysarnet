<!-- 
.. description: Python ile parser yapıyoruz. Bu yazıda, Operatör önceliği konusu var. Bitmiş kodlar  github'da.
.. date: 2013/10/16 15:06
.. title: Python ile parser yapımı
.. slug: python-ile-parser-yapimi
-->

Bu yazıda, [Lexical Analiz](lexical-analiz.html) yazısında anlattığım Lexer'ın üstüne, bir de Parser yapmaya başlayacağız.
Parser konusunda genel bilgi almak için, [Parsing Kavramı ve Yöntemleri](parsing-parser-topdown-operator-precedence.html) yazısını
okuyabilirsiniz.

Öncelikle, izleyeceğimiz yöntemden biraz bahsedeyim. Burada kullanacağımız yöntem, çok orjinal bir yöntem değil aslında.
[Vaughan Pratt](http://boole.stanford.edu/pratt.html) tarafından Recursive Descent ve Operator Precedence yöntemlerinin güzel yanlarını birleştiren
bir parse yöntemi, 1973 yılında bir sempozyumda sunuldu. 2007 yılında, [Douglas Crockford](http://www.crockford.com/) bu yöntemi
kullanarak, [Top Down Operator Precedence](http://javascript.crockford.com/tdop/tdop.html) adında bir yazı yazdı. Bu yazıda,
bir javascript parser'ı örnek gösteriliyordu. Bundan esinlenen [Fredrik Lundh](http://effbot.org/zone/about.htm)
[Simple Top-Down Parsing in Python](http://effbot.org/zone/simple-top-down-parsing.htm) yazısında, bu yöntemi kullanarak Python'un
bir kısmını parse edebilen bir program örneği ve benchmarkları yayınladı. Ben burada, bu yöntemi anlaşılır bir şekilde sunmaya
çalışacağım. Bahsi geçen Parser ve Lexer'ın kısmen bitmiş hallerine [Lexer-Parser github deposu](https://github.com/yasar11732/Lexer-Parser)
üzerinden ulaşabilirsiniz. <!-- TEASER_END -->

İlerlemeden önce, şunu da belirteyim; yazdığım parser'ı `parse tree` oluşturmaya yönelik yazdım. Ancak, isteyenler, yöntemi anladıktan
sonra bunu interpreter yapmaya yönelik de kullanabilirler.

## Operatör Önceliği

Kullanacağımız yöntem, yukarıda da bahsettiğim gibi hem Yukarıdan Aşağıya parse yöntemini hem de Operator Precedence yöntemini kullanıyor.
Bunu yapmak için, her token için 3 şey belirtiyoruz: `nud`, `led` ve `lbp`.

 * `nud`: Crockford'un terminolojisinde, null denotation'ın kısaltması. `nud` metodu, soldaki tokenlerle ilgilenmez. `nud` metodu,
 literal dediğimiz, kendi değeri kendine eşit semboller tarafından kullanılacak, örneğin, NAME, STRING, NUMBER, FLOAT vs. Ayrıca, prefix
 dediğimiz, kendinden sonra gelen ifade üzerinde işlem yapan işleçler de nud metodunu kullacak. Örneğin, `-5` parse edilirken, - tokeni
 `nud` metodunu çağıracak.
 * `led`: left denotation'ın kısaltması. Soldaki sembollerle ilişki kuran semboller tarafından kullanılacak. infix dediğimiz, '+'
 sembolü gibi, iki ifadeyi birbirine bağlayan ve suffix dediğimiz, "++" gibi kendinden önce gelen ifadeye bağlanan işleçler tarafından
 kullanılacak.
 * `lbp`: left binding power'ın kısaltması. Bir operatör, solundaki ifadeye ne kadar güçlü bağlanıyorsa, o kadar yüksek bir değer alacak.
 Örneğin, standart matematik kuralları gereği, `*` ve `/` sembolü, `+` ve `-` sembollerinden yüksek öncelik almalı
 
Şimdilik, "1 + 2 * 3" ifadesini parse edecek kadar bir parser yapmaya başlayalım. Bu parser'ın, `2 * 3` ifadesini gruplamasını ve
baştaki `1` i bu grupla bağlamasını istiyoruz. Algoritamanın kalbi, işte bu fonksiyon;
	
	:::python
    def Expression(self, rbp=0):
        t = self.token
        self._advance()
        left = t.nud()
        while rbp < self.token.lbp:
            t = self.token
            self._advance()
            left = t.led(left)
        return left
		
Bu fonksiyon, bir `expression` parse etmek için kullanılıyor. Değişkenler, literal'ler ve işleçlerden
oluşan ve bir değere indirgenebilen kısımlara expression diyoruz. Örneğin, "1 + 1" ifadesi, 2 değerine indirgenebilen bir ifade.

`Expression`, Parser sınıfının bir metodu olacak. `token` geçerli tokeni belirtiyor. `_advance()` bir sonraki tokene geçiyor.
Bu metot, önce baştaki token'in `nud` metodunu çağırıyor. Yukarıda da bahsettiğimiz gibi, değişken, literal ve prefix gibi bir ifade
başlatabilen semboller `nud` metodu tanımlamalı. Daha sonra, bir sonraki sembolün soldan bağlama gücü, bu ifadenin sağdan bağlama
gücünden yüksek olduğu sürece, müteakip sembollerin `led` metodu çağırılıyor. Bu işlem, recursive olabilir, çünkü, `led` ve `nud`
metotları tekrar `Expression` metodunu çağırabilirler.

Yukarıda, örnek olarak verdiğimiz ifade üzerinden gidecek olursak, önce değeri 1 olan NUMBER tokeninin `nud` metodu çağırılacak.

	:::python
	class number_token:
		def __init__(self, value):
			self.value = value
		
		def nud(self):
			return self
			
		def __repr__(self):
			return "(NUMBER %i)" % self.value
			
Fredrik Lundh'un makalesinde, bu sınıf, `literal_token` isminde ve `nud` metodu token'in kendisinin yerine değerini döndürüyor.
Ben farklı literallere farklı sınıflar oluşturuyorum, çünkü, hepsine ayrı `__repr__` metotları atayabilirim. `nud` metodu da 
kendisini döndürüyor çünkü direk *parse tree* oluşturmak istiyorum. Eğer yorumlayıcı yapacak olsaydım, direk değeri döndürmek
daha mantıklı olabilirdi.

Daha sonra Expression, sıradaki token'in bağlama gücünün, en az bu ifade'nin bağlama gücü kadar olup olmadığını kontrol ediyor.
Eğer öyleyse, sıradaki token'in `led` metodu çağırılacak. En başta, Expression'a verilen bağlama gücü 0 ve sıradaki token `+`
tokeni. Onu da bu şekilde yazabiliriz.

	:::python
	class operator_add_token:
		lbp = 10
		def __init__(self, parser):
			self.parser = parser
			self.first = self.second = None
		
		def led(self, left):
			self.left = left
			self.right = parser.Expression(10)
			return self
			
		def __repr__(self):
			return "(+ %r %r)" % (self.first, self.second)
			
Yine yukarıda bahsettiğim nedenlerden dolayı, bu metot Lundh'un makalesindeki versiyondan biraz farklı. Farkettiyseniz, tek
tek her token için bir class oluşturmak giderek yorucu bir hal alacak, daha sonra bunun için bir factory yazacağız, ama şimdilik
konuyu dağıtmamak için oraya girmiyorum.

Burada dikkat edilecebilecek 2 şey var; `lbp` değeri ve `Expression` çağrısı. `lbp` için verdiğimiz 10 değerini kafadan atadık. Bunu
atarken, operatör önceliğine dikkat etmemiz gerek. Buna verdiğimiz değer `=` gibi operatörlerden büyük, `*` gibi operatörlerden
küçük olmalı ki, tokenler doğru şekilde gruplanabilsin.

Bu token, sağ taraftaki ifadeyi bulmak için, tekrar parser'ın Expression metodunu çağırıyor. Ancak, bu sefer `Expression` metodunu 10 değeriyle çağırdık. Böylece, bundan sonraki tokenlerin
`lbp` değerleri 10'dan yüksek olduğu sürece, yeni ifade oluşturulmaya devam edecek.

Şimdilik, 1 ve + tokenlerini bir kenara bırakalım, şu anda + operatörünün sağ tarafındaki ifadeyi bulmaya çalışıyoruz. Acaba +
operatörü `2`'yi mi kendine bağlayacak, yoksa `2 * 3`'ü mi kendine bağlayacak... Tüm bu soruların cevabı, reklamlardan sonra...

> https://www.coursera.org/course/ml adresinde, ücretsiz machine learning dersleri bulabilirsiniz. Hem de Andrew Ng veriyor dersi!

Evet, tekrar birlikteyiz. Son bıraktığımızda, `Expression` metodu, bağlayıcılık gücü 10 olacak şekilde çağırılmıştı. Sırada ne var peki?
Önce 2'nin nud metodu çağırılacak, sonra * ifadesinin bağlayıcılık gücüne bakılacak. Peki * operatörü ne kadar bağlıyor?

	:::python
	class operator_multiply_token:
		lbp = 20
		def __init__(self, parser):
			self.parser = parser
			self.first = self.second = None
		
		def led(self, left):
			self.left = left
			self.right = parser.Expression(20)
			return self
			
		def __repr__(self):
			return "(* %r %r)" % (self.first, self.second)
			
Evet, gördüğümüz gibi, `*` tokeninin bağlayıcılık gücü, 10'dan fazla, demek ki, bu sefer de `*` tokeninin sağında ne var diye bakmak
için, tekrar `Expression` metodu çağırılacak.

Döndük başa, 3'ün nud metodu çağırıldı, şimdi de bir sağdaki token'in bağlayıcılık gücüne bakılacak. İyi de, sağda bir ifade yok?
Token dizisinin bittiğini belirtmek için, end tokeni kullanacağız.

	:::python
	class end_token:
		lbp = 0

Evet, end token'in bağlayıcılık gücü 20'den az. Dolayısıyla, `*` sembolünün sağ tarafında bir tek 3 varmış. Ve demek ki neymiş, `+`
ifadesinin sağ tarafında `2 * 3` varmış. Böylece, bir tam ifadeyi parse etmiş olduk. Şimdi işlemi tekrar özetleyelim;

 1. `Parser.Expression(0)`
 1. `number_token(1).nud()`
 2. `operator_add_token().led((NUMBER 1))`
 3. `Parser.Expression(10)`
 4. `number_token(2).nud()`
 5. `operator_multiply_token().led((NUMBER 2))`
 6. `Parser.Expression(20)`
 7. `number_token(3).nud()`
 8. Bütün fonksiyon çağrıları bitiyor.
 
Oluşturduğumuz parse tree de şu şekilde oldu;
<pre>
(+ (NUMBER 1) (* (NUMBER 2) (NUMBER 3)))
</pre>

Evet, beklediğimiz gibi, en dışta, `+` sembolü var. Bunun ilk elemanı (NUMBER 1), ikinci elemanı ise (\* (NUMBER 2) (NUMBER 3)). Bu
ikinci eleman ise, yine iki elemandan oluşan bir \* sembolü.

Bu yazı çok uzadığı için, burada bırakıyorum. Daha sonra, bu Parser'ı yapmaya devam edeceğiz.