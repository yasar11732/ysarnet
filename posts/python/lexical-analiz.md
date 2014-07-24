<!-- 
.. description: lexical analiz nedir, lexical analiz ne için kullanılır? Python ile lexer yapıyoruz!
.. date: 2013/10/14 16:35:21
.. title: Lexical Analiz
.. slug: lexical-analiz
-->


[lexical analiz](http://en.wikipedia.org/wiki/Lexical_analysis)  karakter dizisini,  token dizisine çevirme işlemine deniyor. Token
dediğimiz şey ise, bir veya daha fazla karakterden oluşan ve grup olarak önem taşıyan karakter dizisi demek. Bu analizi yapan kodlara lexer deniyor.
Çoğu zaman, lexer'ların oluşturduğu token dizisi, parser tarafından işlenir. Bunlar bir dil oluşturmak ve bu dili analiz etmek için kullanılır. <!-- TEASER_END -->

	:::python
	cevre = 2 * pi * r
	
Yukarıdaki koddaki tokenler şu şekilde düşünülebilir:

<style>
td {
	border-bottom: 1px solid #ccc;
	padding: 9px 8px 0;
}
th {
	border-bottom: 2px solid #aaa;
	padding: 9px 8px 0;
}

table {
	font-style: normal;
	font-weight: 400;
}
</style>
<table style="margin: 20px">
 <thead>
  <tr> <th>Tip</th>      <th>Deger</th> </tr>
 </thead>
 <tbody>
  <tr> <td>degisken</td> <td>cevre</td> </tr>
  <tr> <td>esittir</td>  <td>=</td>     </tr>
  <tr> <td>sayı</td>     <td>2</td>     </tr>
  <tr> <td>islec</td>    <td>*</td>     </tr>
  <tr> <td>degisken</td> <td>pi</td>    </tr>
  <tr> <td>islec</td>    <td>*</td>     </tr>
  <tr> <td>degisken</td> <td>r</td>     </tr>
 </tbody>
</table>

Lexical analiz için, çeşitli yöntemler kullanılabilir.

 * Düzenli İfadeler: Düzenli ifadeler, bu tip işler için kullanılabilir. Düzenli ifadeler çok gelişmiş araçlardır. Ancak,
 bunlar lexer için biraz fazla kaçabilir. Ayrıca, yazılan kurallara bağlı olarak, çok yavaş çalışabilirler.
 * Lexer ve Parser oluşturucu araçlar: Örneğin, lex/yacc, flex/bison, ply gibi araçlar, lexer ve parser oluşturmak için kullanılabilir.
 Ancak duyduğuma göre, bunlar çok genel amaçlı araçlar olduğu için, en ufak  iş için bile, gereğinden fazla kod oluşturuyorlarmış. Ayrıca,
 yavaş çalıştıklarını da duymuştum.
 * lexer yazmak: lexer yazmak çok zor  iş değil. Kendi kullanım alanınızla tam entegre olur, ve gereğinden fazla kod üretmez. Ayrıca,
 lexer'ın çalışma yapısı üzerinde tam hakimiyet sahibi olursunuz.

Python'la basitçe  lexer'ın nasıl yapılabileceğini, birkaç yazılık bir seri halinde anlatmak istedim. Eğer vakit bulursam, bundan sonra da
basit bir parser yapmaya değinebilirim. Lexer sınıfımız şu şekilde başlıyor: 

	:::python
	class Lexer(Thread):
		def __init__(self,inp, que, name="unnamed lexer"):
			super(Lexer, self).__init__()
			self._inp = inp
			self._que = que
			self._start = 0
			self._pos = 0
			self.name = name

Bu sınıf bir thread olarak çalışacak. Böylece, ileride  parser ilave edersek, parser ve lexer
aynı anda paralel olarak çalışabilir. Argüman olarak, okuyacağı girdiyi ve  `Queue` objesini alıyor. `_start` geçerli
tokenin başladığı index'i gösteriyor. `_pos` ise, lexer'in o anda hangi pozisyonda işlem yaptığını gösteriyor. `_start` ve
`_pos` state fonksiyonları tarafından o anki token'i belirlemek için kullanılacak. Detaylarına daha sonra değineceğiz.

Lexer sınıfımız  state machine gibi çalışacak. Her state  sonraki state'i döndürecek, ve lexer'ımız bu şekilde çalışmaya devam edecek.
    
	:::python
	class Lexer(Thread):
		def run(self):
			state = self._lexInitial
			while True:
				try:
					state = state()
				except Consumed:
					self._emit("END")
					break
					
Başlangıçta `_lexInitial` state'i çalışıyor. Daha sonra, sonsuz  döngü şeklinde, state'ler ardarda çalışıyor. Analiz işleminin
bittiğini belirtmek için exception kullandım. Bu durumda, "END" tokeni verip, döngüden çıkıyoruz.

    :::python
	class Consumed(Exception):
		pass
	
	class Lexer(Thread):
		def _emit(self, token_type):
			self._que.put((token_type, self._inp[self._start:self._pos]))
			self._start = self._pos

state fonksiyonları bir token vermek istediklerinde `_emit` fonksiyonunu çağırıyorlar. Bu fonksiyon, Lexer sınıfına verilmiş olan
`Queue`'ye tokenin tipi ve değerinden oluşan bir `tuple` koyuyor. Daha sonra, `_start` değerini ileri sarıyor. Böylece, bir sonraki
token, bu tokenin bittiği yerden başlayacak.
 			
Bir sonraki yazıda state fonksiyonlarını gösterdiğimde, `_start` ve `_pos` değişkenlerinin nasıl kullanıldığı ve state'ler arasındaki
geçişin nasıl sağlandığı biraz daha netleşecek. Ama bu yazılık bu kadar.