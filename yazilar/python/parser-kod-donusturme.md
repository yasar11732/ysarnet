<!-- 
.. description: Python benzeri syntax'dan C benzeri syntax'a kod dönüştüren Parser'ı bitiriyoruz.
.. date: 2013/10/18 19:45:33
.. title: Parser - Kod Dönüştürme
.. slug: parser-kod-donusturme
-->

Parser yazılarını takip ettiyseniz, kaynak kodları parse tree'e çevirebilen bir parser yazmıştık. Bu yazıda, onu biraz daha
geliştirip, parse tree'den kod üretmesini sağlayacağız. [Kodlar](https://github.com/yasar11732/Lexer-Parser/) yine aynı yerde.

Daha önce bahsettiğim gibi, parser tree'i birçok farklı şekilde kullanabilirsiniz. Ben kendi parse tree'min kodları C benzeri bir
dile çevirmesini istiyorum. <!-- TEASER_END -->

Bunu yapmak için, parse tree'deki her eleman için, onun nasıl yazdırılacağını gösteren bir fonksiyon atayacağım. Örneğin,
bir if statement'ı için:
		
	:::python
	def ifWriter(self):
		
		begin = "if (%s)%s" % (self.first.write(), self.second.write())
		
		if not self.third:
			return begin
		
		return "%s%selse %s" % (begin, self.parent.outputindentlevel * "    ",self.third.write())
		
gibi bir fonksiyon aracılığıyla, bir if statement'ı yazdırabileceğiz. Bunu, if sembolüne metot olarak ekliyorum.

	:::python
	statement("if", ifStatement, ifWriter)
	
`statement` yardımcı fonksiyonunu şu şekilde düzenledim:

	:::python
	def statement(id, std, writer=None):
		self._symbol(id).beginStatement = True
		self._symbol(id).std = std
		if writer:
			self._symbol(id).write = writer
			
Böylece, gerekli `write()` metodunu, if sembolüne eklemiş oluyoruz. Bunu, parse tree'de olabilecek her sembol için yapmalıyım.
Birçok sembol için, sadece yardımcı fonksiyonu düzenlemem yeterli olacak.

	:::python
	def infix(id, bp):
		def led(self, left):
			self.first = left
			self.second = self.parent.Expression(bp)
			return self
		self._symbol(id, bp).led = led
		self._symbol(id).write = lambda self: self.first.write() + id + self.second.write()
		
	def infixr(id, bp):
		def led(self, left):
			self.first = left
			self.second = self.parent.Expression(bp-1)
			return self
		self._symbol(id,bp).led = led
		self._symbol(id).write = lambda self: self.first.write() + id + self.second.write()
		
	def literal(id):
		self._symbol(id).nud = lambda self: self
		self._symbol(id).write = lambda self: str(self.value)
		
`while`, `print` gibi statement'lar için özel fonksiyonlar yazılması gerekiyor. Github deposundaki kodlarda bunlar var, oradan
bakabilirsiniz.

Halletmem gereken birşey daha var. Bir statement listesi, expression statement ve bir kod bloğu, parse tree'de sembol olarak
bulunmuyor. Bu sebeple, onlar için wrapper sınıflar yazıp, onları parse tree'e ekleyeceğim:


	:::python
	class BlockWrapper(object):
		def __init__(self, stmts, parent):
			self.stmts = stmts
			self.parent = parent
		def write(self):
			self.parent.outputindentlevel += 1
			inner = self.stmts.write()
			self.parent.outputindentlevel -= 1
			return "{\n%s}\n" % inner
			
	class ExpressionStatementWrapper(object):
		
		def __init__(self, expr):
			self.expr = expr
			
		def write(self):
			return self.expr.write() + ";"
			
			
	class StatementsWrapper(object):
		def __init__(self, stmts, parent):
			self.stmts = stmts
			self.parent = parent
			
		def write(self):
			lvl = self.parent.outputindentlevel
			return "\n".join(["    " * lvl + x.write() for x in self.stmts])
			
Son olarak, gerekli yerlerde, bu wrapper sınıfların objelerini parse tree'e eklemem gerekiyor. `Statements` ve `Block` metotlarını
düzenleyeceğim.

	:::python
    def Statement(self):
        t = self.token
        if t.beginStatement:
            self._advance()
            return t.std()
        ex = self.Expression(0)
        self._advance(["NEWLINE","END","DEDENT"])
        return ExpressionStatementWrapper(ex)
        
    def Statements(self):
        statements = []
        while True:
            if self.token.id in ["END","DEDENT"]:
                break
            s = self.Statement()
            if s:
                statements.append(s)
        return StatementsWrapper(statements, self)
		
	def Block(self):
        self._advance(["INDENT"])
        stmts = self.Statements()
        self._advance(["DEDENT"])
        return BlockWrapper(stmts, self)

`Parser` sınıfına da `parse` ve `output` isminde iki yeni metot ekledim:

	:::python
    def parse(self):
        self.stmts = self.Statements()
        
    def output(self):
        return self.stmts.write()
		
Artık kodları deneyebiliriz:

	:::python
	if __name__ == "__main__":
		tokenq = Queue()
		
		with open("test.txt") as dosya:
			myinput = dosya.read()
		
		mylexer = Lexer(myinput, tokenq)
		mylexer.start()

		myparser = Parser(tokenq)
		
		myparser.parse()
		print myparser.output()
		
Örnek *test.txt*

	:::python
	while True:
		if a > 12:
			break
		if a < 3:
			continue
		else:
			print a

	osman = 12
	veli = 29 * 12

Çıktı:
	
	:::c
	while (True) {
		if (a>12){
			break;}

		if (a<3){
			continue;}
		else {
			print(a);}
	}

	osman=12;
	veli=29*12;

Evet, gördüğünüz gibi, temelden girip, Python benzeri bir dili, C benzeri bir dile dönüştürebilen bir parser yapmış olduk. Artık burdan
sonrası da size kalmış.