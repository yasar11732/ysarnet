<!-- 
.. description: Daha önceki yazılarda yazmaya başladığımız Parser'ı bitiriyoruz.
.. date: 2013/10/16 22:16
.. title: Parser - Statement
.. slug: parser-statement
-->

Evet, son bıraktığımızda, Parser'ımız expression'ları parse edebiliyordu. Ancak, henüz tek bir expression parse edebiliyoruz. Bu yazıda,
statement'ları nasıl parse edeceğimize değineceğiz.

Önce statement (beyan) nedir, ona biraz değinelim. Statement, expression'dan bir üst kategori diyebiliriz. Her expression, aynı
zamanda bir statement olabilir. Ancak, her statement bir expression olamaz. Mesela, programlama dillerindeki `if` sözcüğü bir statement
tanımlar, ama `if` statement'ı bir expression diyemeyiz.

Statement'ları parse edebilmek için, statement başlatan sembollerimize özel bir `std` metodu tanımlayacağız. Örneğin, if statement
yapmak için gerekli olan sembolü, sembol tablosuna ekleyelim: <!-- TEASER_END -->
	
	:::python
	def statement(id, std):
		self._symbol(id).beginStatement = True
		self._symbol(id).std = std
		

	def ifStatement(self):
		self.first = self.parent.Expression()
		self.parent._advance([":"])
		self.parent._advance(["NEWLINE"])
		self.second = self.parent.Block()
		if self.parent.token.id == "else":
			self.parent._advance(["else"])
			self.parent._advance([":"])
			self.parent._advance(["NEWLINE"])
			self.third = self.parent.Block()
		return self
		
	statement("if", ifStatement)
	
Tahmin edeceğiniz gibi, bunlar `_prepareSymTable` metodunun içine gidiyor.

`ifStatement`, önce, bir expression alıp bunu ilk ögesi olarak ayarlıyor. Daha sonra, bir ":" ve bir "NEWLINE" sembolü ilerledikten
sonra, ikinci elemanını bulmak için Parser metodunun `Block` metodunu çağırıyor.
	
	:::python
    def Block(self):
        self._advance(["INDENT"])
        stmts = self.Statements()
        self._advance(["DEDENT"])
        return stmts
		
Bu, `Parser` sınıfının bir metodu olacak. Önce bir indent ilerliyor, sonra bir statement listesi alıyor, sonra bir dedent daha
ilerleyip, statement listesini döndürüyor. Ben, Python gibi, indentation tabanlı block'lar yapmak istedim. Siz isterseniz block'larınızı
"{" ile başlatıp, "}" ile bitirebilirsiniz.

	:::python
    def Statements(self):
        statements = []
        while True:
            if self.token.id in ["END","DEDENT"]:
                break
            s = self.Statement()
            if s:
                statements.append(s)
        return statements
		
Çok açıklayacak birşey yok, END veya DEDENT görene kadar, bir statement parse edip, bunları listeye koyup gönderiyoruz.

	:::python
    def Statement(self):
        t = self.token
        if t.beginStatement:
            self._advance()
            return t.std() 
        ex = self.Expression(0)
        self._advance(["NEWLINE","END","DEDENT"])
        return ex
		
Eğer, geçerli token bir statement başlangıcıysa, onun std metodunun sonucunu döndürüyoruz, eğer değilse, bir expression parse edip, sonra
bir "NEWLINE", "END" veya "DEDENT" ilerleyip, sonucu döndürüyoruz. Eğer expression parse edildiğinde geçerli token bunlardan bir tanesi
değilse, bu okuduğumuz girdi, bizim yazım kurallarımıza uygun değil demek. Bir diğer deyişle, SyntaxError.

Şimdi, şunu parse etmeyi deneyelim:

<pre>
if yasar:
    a = a + 12
else:
    a = 12
    b = 25
</pre>

Test etmek için kullandığımız kodlar:

	:::python
	if __name__ == "__main__":
		tokenq = Queue()
		
		with open("test.txt") as dosya:
			myinput = dosya.read()
		
		mylexer = Lexer(myinput, tokenq)
		mylexer.start()

		myparser = Parser(tokenq)

		print "parse result:",myparser.Statements()
		
Ve sonuç:

<pre>
parse result: [(if (NAME yasar) [(= (NAME a) (+ (NAME a) (NUMBER 12)))] [(= (NAME a) (NUMBER 12)), (= (NAME b) (NUMBER 25))])]
</pre>

## Bundan sonra?

Bundan sonrası size kalmış. Yeni dil kuralları ekleyin, yeni operatörler tanımlayın, artık canınız ne çekerse.

### Peki ya ondan sonra?

Son olarak, elde ettiğiniz parse tree'i kullanılabilecek bir veri türüne çevirebilir veya bir yorumlayıcı yazarak çalıştırabilirsiniz.

İsterseniz makine koduna derleyin, ister başka bir programlama diline derleyin, isterseniz JSON yapın, ister html'e dönüştürün, isterseniz
grafiğini çizin, böyle oklar falan olsun, artık keyfinize göre takılın.

Ben bunları aslında kafamda bir proje var, onun için yazdım. Eğer vakit bulup o aşamaya gelirsem, onu da blog'dan yazarım.