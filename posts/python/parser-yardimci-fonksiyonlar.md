<!-- 
.. description: Yazdığımız parser yardımcı fonksiyonlara değineceğiz, temel sembol sınıfı yazacağız ve bir sembol tablosu oluşturacağız.
.. date: 2013/10/16 20:50
.. title: Parser - Yardımcı Fonksiyonlar
.. slug: parser-yardimci-fonksiyonlar
-->


[Python ile parser yapımı](python-ile-parser-yapimi.html) yazısı, kullanacağımız algoritmayı tanıtmak üzerineydi. Bu yazıda
ise, Parser yapmakta kullanacağımız yardımcı fonksiyon ve sınıflara değineceğiz. <!-- TEASER_END -->

## Parser Sınıfı

	:::python
	class Parser(object):
		def __init__(self, queue):
			self._q = queue
			self._sym = {}
			self._prepareSymTable()
			self.token = self._nextToken()
			
Parser sınıfı, bir Queue objesi alıyor. Token'lerimizi bu Queue üzerinden okuyacağız. Bu Queue'e, daha önceki yazılarda
yazmış olduğumuz Lexer sınıfı tokenleri koyacak.

Parser sınıfının `_sym` adında bir sembol tablosu var. `_prepareSymTable` Parser'ın tanıdığı sembolleri bu tabloya ekleyecek.
Bu metodu daha sonra inceleyeceğiz.

`_nextToken` ise, daha sonraki token'i almak için kullanılıyor. Ancak, bir sonraki token'e ilerlemek için, bu metot
yerine, aşağıdaki `_advance` metodunu kullanacağız.

    :::python
	def _nextToken(self):
        ttype, lineno, tvalue = self._q.get(True, 5) # if we can't get a new token in next 5 secs, raise an exception
        self.lineno = lineno      
        s = self._sym[ttype]()

        if ttype in ["NUMBER","FLOAT","STRING","NAME"]:
            s.value = tvalue
        return s
		
	def _advance(self, idlist=None):

        if self.token.id == "END":
            return

        if idlist and self.token.id in idlist:
            self.token = self._nextToken()
        elif not idlist:
            self.token = self._nextToken()
        else:
            raise ParseError("""Expected one of %s
	found %r instead. (line: %i)""" % (" ".join(idlist), self.token.id, self.lineno))

`_nextToken`, Queue'den bir token alıyor. Parser'ın bulunduğu satırı, Lexer'dan gelen bilgiye göre güncelliyor. Daha sonra,
sembol tablosundan o token'e karşılık gelen sınıfı bulup, yeni bir örneğini oluşturuyor. Eğer, o anki token bir literal ise,
literal'in değerini ayarlayıp, sembolü gönderiyor.

`_advance` ise, opsiyonel olarak bir `idlist` argümanı alıyor. Eğer bu argüman verildiyse, ve şu anki token idlist içerisinde
değilse, ParseError veriyor. Bunun kullanımını daha sonra göreceğiz. Bunun dışında, eğer token sırası bitmişse, hiçbirşey yapmıyor.

Sıra geldi, sembol tablomuzun oluşturulmasına. Sembol tablomuza koyacağımız her sembol için, tek tek yeni sınıf oluşturmak yerine,
temel sembol sınıfı oluşturacağız. Diğer semboller bunun uzantısı olacak.

	:::python
	class BaseSymbol(object):
		id = None
		value = None
		parent = None
		first = second = third = None
		beginStatement = False

		def nud(self):
			raise ParseError("Parse error (%r)" % self.id)

		def led(self, left):
			raise ParseError("Unknown operator (%r)" % self.id)

		def __repr__(self):
			if self.id in ["NAME","NUMBER","FLOAT","STRING"]:
				return "(%s %s)" % (self.id, self.value)
			out = [self.id, self.first, self.second, self.third]
			return "(" + " ".join(map(str,filter(None,out))) + ")"
			
`id`, "NUMBER", "FLOAT" gibi, o tokenin tipini gösteren bir string. `value` literaller tarafından kullanılacak, o tokenin değerini
gösteriyor. `first`, `second`, `third` değikenleri, birkaç kısımdan oluşan sembollerin kısımlarını göstermek için kullanılacak. Örneğin,
"+" sembolünün sol ve sağ tarafları, `first` ve `second` değişkenlerine atanacak. `parent`, bu sembolün ait olduğu Parser objesini gösteriyor.
`beginStatement` ise, bu sembolün bir statement başlatıp başlatmadığını gösteriyor. Henüz bir statement parse etmeye başlamadık, ama
başladığımız zaman kullanacağız bu değişkeni.

Şimdi de, factory rolünü üstlenecek metoda bir bakalım:

	:::python
    def _symbol(self, id, bp=0):
        try:
            s = self._sym[id]
        except KeyError:
            class s(BaseSymbol):
                pass
            s.__name__ = "symbol-" + id
            s.id = id
            s.lbp = bp
            s.parent = self
            self._sym[id] = s
        else:
            s.lbp = max(bp, s.lbp)
        return s
		
Bu metodun yaptığı az çok belli, çok üstünde durmayacağım. Özetle, eğer sembol önceden oluşturulmuşsa, sembol tablosundan
döndürüyor, aksi halde yeni bir sembol oluşturup, tabloya ekleyip onu döndürüyor.

Artık, `_prepareSymTable` ne yapıyor bakabiliriz. Bu metodun işi, Parser'ın tanıdığı tüm sembolleri, sembol tablosuna
eklemek. Önce, 4 işlem sembollerini ekleyelim:

	:::python
	def _prepareSymTable(self):
		def plusled(self, left):
			self.first = left
			self.second = self.parent.Expression(10)
			return self
		
		self._symbol("+", 10).led = plusled
		
		def minusled(self, left):
			self.first = left
			self.second = self.parent.Expression(bp)
			return self
		
		self._symbol("-", 10).led = minusled
				
		def multiled(self, left):
			self.first = left
			self.second = self.parent.Expression(20)
			return self
			
		self._symbol("*", 20).led = multiled
				
		def divideled(self, left):
			self.first = left
			self.second = self.parent.Expression(20)
			return self
		
		self._symbol("/", 20).led = divideled
		
Şaka, şaka... Böyle ekliycez:

	:::python
     def _prepareSymTable(self):
         def infix(id, bp):
            def led(self, left):
                self.first = left
                self.second = self.parent.Expression(bp)
                return self
            self._symbol(id, bp).led = led
            
        infix("+",10); infix("-",10); infix("*",20); infix("/",20)
		
Evet, literallerimizi de ekleyelim:
	
	:::python
	def literal(id):
		self._symbol(id).nud = lambda self: self
		
	for l in ["NUMBER","FLOAT","NAME","STRING"]:
		literal(l)
		
Evet, böylece, şimdiye kadar kullandığımız sembolleri sembol tablosuna eklemiş olduk. Daha statement'lara girmediğimiz için,
henüz onların sembollerini tabloya eklemedim. Onu da bir sonraki yazıda yapacağız.