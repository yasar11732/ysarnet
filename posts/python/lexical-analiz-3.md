<!-- 
.. description: Daha önceki iki yazıda yazmış olduğumuz Lexer'a ufak dokunuşlar yapacağız.
.. date: 2013/10/14 23:20
.. title: Lexical Analiz 3
.. slug: lexical-analiz-3
-->


Bugünkü yazılar biraz spam gibi oldu kusura bakmayın, ama [lexical analiz 2](/python/lexical-analiz-2.html)'deki lexer'a
yapılabileceğinden bahsettiğim birkaç eklemeyi de göstereyim dedim.

## Satır Sayma

Satır sayma konusu çok kolay, `_lexInitial` ve `_lexString` yeni satırla karşılaştıklarında, bir değişkeni artıracak.
Ayrıca, gönderdiğimiz tokenlere satır bilgisi de ekleyeceğiz. <!-- TEASER_END -->
	
	:::python
	def __init__(self,inp, que, name="unnamed lexer"):
		# Yukarıla aynı
		self.line = 1
	def _lexInitial(self):
		while True:
		# Yukarılar aynı
		elif current in " \t\n": # ignore whitespace
			self._pos += 1
			self._start = self._pos
			if current == "\n":
				self.line+=1
				return self._lexIndentation
		# Aşağılar aynı
	def _lexString(self):
        escape = False
        while True:
			# Yukarılar aynı
			elif current == "\n":
				self.line += 1
			# bunu sona ekledim, aşağıda birşey yok
			
	def _emit(self, token_type):
        self._que.put((token_type, self.line, self._inp[self._start:self._pos]))
        self._start = self._pos
		
`_lexIndentation` biraz spoiler oldu, ama onun dışında açıklayacak birşey yok.

## İşleçler

İşleçlerle karşılaşacak tek state, `_lexInitial`. Bunda yapacağımız bir değişiklik işimizi görecek.

	:::python
	class Lexer(Thread):
		operators = "+-*/^=~:"
		def _lexInitial(self):
			"Starting State"
			while True:
				# Yukarılar aynı
				elif current in self.operators:
					self._pos += 1
					self._emit(current)
				
## Keywordler

Keyword dediğimiz şey, aslında önceden bizim belirlediğimiz bir *name*. `_lexName` düzenlenerek keyword'lerimizi
token olarak belirtebiliriz.

	:::python
	class Lexer(Thread):
		keywords = ("if","else","or","and","while","for","switch","case")
		
		def _lexName(self):
			def keywordOrName():
				token = self._inp[self._start:self._pos]
				return token in self.keywords and token or "NAME"
			
			while True:
				try:
					current = self._currentChar()
				except Consumed:
					self._emit(keywordOrName())
					raise
				if current in ascii_letters:
					self._pos += 1
				else:
					self._emit(keywordOrName())
					return self._lexInitial
					
## Indentation

Geldik zurnanın zırt dediği yere! Önce kodları görelim:

	:::python
	class Lexer(Thread):
		def __init__(self,inp, que, name="unnamed lexer"):
			# Aynısı
			self.indentlevels = [0]
		
		def _lexIndentation(self):
			current_indent = 0
			while True:
				current = self._currentChar()
				if current == " ":
					self._pos += 1
					current_indent+=1
				elif current == "\t":
					self._pos += 1
					current_indent+=4
				elif current == "\n":
					self._pos += 1
					current_indent = 0
				else:
					if current_indent < self.indentlevels[-1]:
						if current_indent in self.indentlevels:
							while True:
								if current_indent < self.indentlevels[-1]:
									self._emit("DEDENT")
									self.indentlevels.pop()
								else:
									return self._lexInitial
						else:
							raise LexException("Congratz! Your indentation is all messed up!")
					elif current_indent > self.indentlevels[-1]:
						self._emit("INDENT")
						self.indentlevels.append(current_indent)
						return self._lexInitial
					else:
						return self._lexInitial
					
İlk bakışta göze korkunç geliyor ama çok birşeyi yok aslında. Öncelikle, `__init__` içerisinde `indentlevels` adında bir liste
tanımladık. Bunu yapmamızın nedeni, önceki girintileme seviyelerini akılda tutmak. Bunu yapmazsak, doğru sayıya çıkıntılama (girintilemenin tersi :) )
yapamayız. Bir örnekle inceleyelim:

<pre>
yasar
  arabacı
      osman
	         hebele
  yine yasar
</pre>

Eğer lexer'ımız yukarıdaki yazıyı okuyorsa, son satıra geldiği zaman iki kere "DEDENT" tokeni vermeli. Aksi halde parser sıkıntıya
girer. Evet, henüz bir parser yok ortada, ama olunca bu işimize yarayacak.

`_lexIndentation`'a gelen tek state `_lexInitial`. `_lexInitial` yeni bir satır gördüğünde işi indentation state'ine paslayacak.

Bu state'in ilk işi o satırdaki girinti seviyesini hesaplamak. Bunu yapmak için, boşluk, tab veya yeni satır haricinde ilk
karakteri görene kadar sayıyor. Her boşluk 1, tab 4 girintileme değerine sahip. Yeni satır ise, girintileme değerini sıfırlıyor.
Böylece, bir girintileme seviyesi içindeki boş satırları da hesaba katmış oluyoruz.

Bu state o satırdaki girintileme seviyesini belirlediği zaman, bir önceki girintileme seviyesi ile karşılaştırma yapıyor. Eğer
şu anki girintileme seviyesi, öncekinden büyükse, bir INDENT tokeni verip, kontrolü `_lexInitial` state'ine veriyor.

Eğer o anki girintileme, öncekinden daha küçükse, yani bir çıkıntılama (:)) tespit edilmişse, bunu daha önceki seviyelerle
karşılaştırıyor. Eğer daha önceki seviyelerden biriyle eşleşiyorsa, o seviyeye dönene kadar DEDENT tokeni veriyor. Eğer bir eşleşme
yoksa, Exception veriyor. Tıpkı Python dilinin yaptığı gibi.

Eğer o anki girintileme, önceki ile aynıysa, kontrolü `_lexInitial` devralıyor, ve işlem devam ediyor.

Düzeltilmesi gereken bir şey daha var aslında. Okunacak girdi bittiği zaman, girintilemeyi sıfırlamak gerek.
	
	:::python
    def _cleanup(self):
        current_indentation = self.indentlevels.pop()
        while current_indentation != 0:
            self._emit("DEDENT")
            current_indentation = self.indentlevels.pop()
        self._emit("END")

    def run(self):
        state = self._lexInitial
        while True:
            try:
                state = state()
            except Consumed:
                self._cleanup()
                break
            except LexException as e:
                print e.message
                self._emit("END")
                break
				
Burada olup biten de oldukça açık. Son olarak, lexer'ımızın son halini bir test edelim.

	:::python
	if __name__ == "__main__":
		tokenq = Queue()
		myinput = """if myname == "yasar":
		12 + 12 = 28
			"Another indent babe!"
	"Lets dedent by two!"
		What happens when we finish in indented block"""
		mylexer = Lexer(myinput, tokenq)
		mylexer.start()

		while True:
			ttype, line, tvalue = tokenq.get()
			if ttype == "END":
				break
			print "%s(line %i) %s" % (ttype, line, tvalue)
			
Çıktısı:

<pre>
if(line 1) if
NAME(line 1) myname
=(line 1) =
=(line 1) =
STRING(line 1) "yasar"
:(line 1) :
INDENT(line 2)     
NUMBER(line 2) 12
+(line 2) +
NUMBER(line 2) 12
=(line 2) =
NUMBER(line 2) 28
INDENT(line 3)         
STRING(line 3) "Another indent babe!"
DEDENT(line 4) 
DEDENT(line 4) 
STRING(line 4) "Lets dedent by two!"
INDENT(line 5)     
NAME(line 5) What
NAME(line 5) happens
NAME(line 5) when
NAME(line 5) we
NAME(line 5) finish
NAME(line 5) in
NAME(line 5) indented
NAME(line 5) block
DEDENT(line 5) 
</pre>

Artık bir parser'a girişmenin vakti geldi gibi. Parser işine girip girmeyeceğimden emin değilim. Ama buraya kadar okuduysanız
bile, lexer konusunda sizin için eğitsel bir deneyim olmuştur diye ümit ediyorum.