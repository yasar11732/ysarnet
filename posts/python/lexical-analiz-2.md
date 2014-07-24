<!-- 
.. description:  Bir önceki yazıda başladığımız lexer'ı, bu yazıda bitiriyoruz.
.. date: 2013/10/14 19:46:19
.. title: Lexical Analiz 2
.. slug: lexical-analiz-2
-->


[Lexical Analiz](/python/lexical-analiz.html) yazısında, Python ile basit bir lexer yazmaya başlamıştık. Bıraktığımızda,
lexer'ımız bu şekildeydi: <!-- TEASER_END -->

	:::python
	class Consumed(Exception):
		pass

	class Lexer(Thread):
		def __init__(self,inp, que, name="unnamed lexer"):
			super(Lexer, self).__init__()
			self._inp = inp
			self._que = que
			self._start = 0
			self._pos = 0
			self.name = name
		
		def _emit(self, token_type):
			self._que.put((token_type, self._inp[self._start:self._pos]))
			self._start = self._pos

		def run(self):
			state = self._lexInitial
			while True:
				try:
					state = state()
				except Consumed:
					self._emit("END")
					break
					
Bu yazıda state metotlarını tanımlamaya başlayacağız. İlk çalıştırılan state metodu `_lexInitial`, bu sebeple onunla başlayalım.

    :::python
	from string import ascii_letters, digits
	
	class Lexer(Thread):
		def _lexInitial(self):
			"Starting State"
			while True:
				current = self._currentChar()

				if current in ascii_letters:
					return self._lexName
				elif current in digits:
					return self._lexNumber
				elif current == '"':
					self._pos += 1
					return self._lexString
				elif current in " \t\n": # ignore whitespace
					self._pos += 1
					self._start = self._pos
				else:
					raise LexException("Unrecognized chracter at position %i" % self._pos)
    
		def _currentChar(self):
			try:
				return self._inp[self._pos]
			except IndexError:
				raise Consumed("Input stream is consumed")
				
Bu metot, sonsuz bir döngü içinde, birer birer bize verilen girdideki karakterleri inceleyip, ne yapılması gerektiğine karar verecek.
Eğer baktığı karater bir ascii harf karakteriyle, `_lexName` state metodunu döndürüyor. Böylece, bir sonraki adımda lexer bir kelime
bulmaya çalışacak. Aynı şekilde, sayı gördüğü zaman `_lexNumber` ve çift tırnak gördüğü zaman `_lexString` metodu döndürüyor.

Eğer boşluk, tab veya yeni satır karakteri görmüşse, sadece bir adım ileri sarıyor. Eğer satırları saymak istiyorsanız, burayı
biraz düzenlemeniz gerekecek.

Eğer bu saydıklarımızın dışında bir karakter görürse, örneğin bir noktalama işareti, Exception veriyor. Tanınmayan karakterleri
işlemek için bir çok yol olabilir, ben kolaya kaçıp Exception verdim.

Şimdi de `_lexNumber` fonksiyonuna bakalım.
    
	:::python
	class Lexer(Thread):
		def _lexNumber(self):
			while True:
				try:
					current = self._currentChar()
				except Consumed:
					self._emit("NUMBER")
					raise
				if current in digits:
					self._pos += 1
				elif current == ".":
					self._pos +=1
					return self._lexFloat
				else:
					self._emit("NUMBER")
					return self._lexInitial
					
Bu metot, sayı karakteri gördükçe, pozisyonu bir adım ileri sarıyor. Eğer bir nokta karakteri görürse, pozisyonu bir adım ileri
sarıp, kontrolü `_lexFloat` metoduna devrediyor. Böylece, FLOAT tokenleri de gönderebiliyoruz. Eğer sayı veya nokta dışında bir karakter
görürse, bir NUMBER tokeni verip, kontrolü `_lexInitial` fonksiyonuna devrediyor.

Bu noktada kafaların karışabileceğini tahmin ettiğim için, bir örnekle izah edeyim. Diyelim ki bize verilen girdi "123 abc". Adım adım
lexer'ın yapacağı şeyler şunlar:

 1. `_pos` ve `_start` 0'a ayarlı, `_lexInitial` metodu çağırıldı.
 2. `_lexInitial` 0 pozisyonunda bir sayı olduğunu gördü, kontrolü `_lexNumber` fonksiyonuna bıraktı.
 3. `_lexNumber` 0 pozisyonunda bir sayı olduğunu gördü ve pozisyonu bir adım ileri aldı.
 4. `_lexNumber` 1 poziyonunda bir sayı olduğunu gördü ve pozisyonu bir adım ileri aldı.
 5. `_lexNumber` 2 pozisyonunda bir sayı olduğu gördü ve pozisyonu bir adım ileri aldı.
 6. `_lexNumber` 3 pozisyonunda sayı veya nokta dışında bir karakter gördü. Bir token belirtti.
 7. `_emit` metodu, [0,3) arasındaki karakterleri bir sayı olarak queue'ye koydu.
 8. Kontrol `_lexInitial` metoduna döndü.
 
Evet, basitçe lexer'ın işleyişi bu şekilde gerçekleşiyor. Bunda sonra bu lexer'ı istediğiniz gibi geliştirebilirsiniz. Ben şöyle yaptım:

	:::python
	from Queue import Queue
	from threading import Thread
	from string import ascii_letters, digits

	class Consumed(Exception):
		pass

	class LexException(Exception):
		pass

	class Lexer(Thread):
		def __init__(self,inp, que, name="unnamed lexer"):
			super(Lexer, self).__init__()
			self._inp = inp
			self._que = que
			self._start = 0
			self._pos = 0
			self.name = name

		def _lexInitial(self):
			"Starting State"
			while True:
				current = self._currentChar()

				if current in ascii_letters:
					return self._lexName
				elif current in digits:
					return self._lexNumber
				elif current == '"':
					self._pos += 1
					return self._lexString
				elif current in " \t\n": # ignore whitespace
					self._pos += 1
					self._start = self._pos
				else:
					raise LexException("Unrecognized chracter at position %i" % self._pos)

		def _lexString(self):
			escape = False
			while True:
				try:
					current = self._currentChar()
				except Consumed:
					raise LexException("Bizim bi string vardi, o nooldu?")
				self._pos += 1
				if escape:
					escape = False
					continue

				if current == '\\':
					escape = True

				elif current == '"':
						self._emit("STRING")
						return self._lexInitial()
					

		def _lexName(self):
			while True:
				try:
					current = self._currentChar()
				except Consumed:
					self._emit("NAME")
					raise
				if current in ascii_letters:
					self._pos += 1
				else:
					self._emit("NAME")
					return self._lexInitial

		def _lexNumber(self):
			while True:
				try:
					current = self._currentChar()
				except Consumed:
					self._emit("NUMBER")
					raise
				if current in digits:
					self._pos += 1
				elif current == ".":
					self._pos +=1
					return self._lexFloat
				else:
					self._emit("NUMBER")
					return self._lexInitial

		def _lexFloat(self):
			while True:
				try:
					current = self._currentChar()
				except Consumed:
					self._emit("FLOAT")
					raise
				if current in digits:
					self._pos += 1
				else:
					self._emit("FLOAT")
					return self._lexInitial

		def _currentChar(self):
			try:
				return self._inp[self._pos]
			except IndexError:
				raise Consumed("Input stream is consumed")
					

		def _emit(self, token_type):
			self._que.put((token_type, self._inp[self._start:self._pos]))
			self._start = self._pos

		def run(self):
			state = self._lexInitial
			while True:
				try:
					state = state()
				except Consumed:
					self._emit("END")
					break
		
	if __name__ == "__main__":
		tokenq = Queue()
		myinput = 'yasar 12 12.657 "bu bir string" "--> escape \\\"" ""'
		mylexer = Lexer(myinput, tokenq)
		mylexer.start()

		while True:
			ttype, tvalue = tokenq.get()
			if ttype == "END":
				break
			print ttype, tvalue
			
Çıktısı:
<pre>
NAME yasar
NUMBER 12
FLOAT 12.657
STRING "bu bir string"
STRING "--> escape \""
STRING ""
</pre>

## EE, peki ya sonra?

Bundan sonra şu tarz şeyler yapmak isteyebilirsiniz:

 * Satır sayma
 * '+', '-' gibi işleçleri token olarak tanıma
 * Eğer bir programlama diline yönelik lexer yapıyorsanız, `if`, `else`, `for` benzeri keyword'leri tanıma
 * Eğer daha asortik birşeyler istiyorsanız, Python gibi, girintilemeyi bir token olarak belirtebilirsiniz.
 
Buraya kadar güzel ama, Lexer kendi başına pek de kullanışlı birşey değil. Lexer'ın çıktısının bir parser tarafından
kullanılabilir bir veri yapısına döndürülmesi gerekiyor. Adam akıllı bir lexer elde ettikten sonra, o işe de girmeyi
düşünüyorum.
