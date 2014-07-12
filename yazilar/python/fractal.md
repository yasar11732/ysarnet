<!--
.. date: 2014/07/12 03:29
.. slug: fractal
.. title: Python ile Fraktal Çizme
.. description: Bugün Python ile fraktal şekiller çizdim, blog'da paylaşıyorum.
-->
Ne zamandır fraktal geometri meraklısı bir insanım. Python'da turtle kütüphanesini olduğunu farkedince (bunca zamandır nasıl görmediysem...) ilk iş
aklıma fraktal çizmek geldi. Blog'dan da paylaşayım istedim.
<!-- TEASER_END -->

Öncelikle, turtle nedir ondan bahsedeyim biraz. Bu kütüphane ekrandaki bir kaplumbağa'ya (temsili) komutlar vermenizi sağlıyor. Örneğin, ileri git, geri
git, sağa dön sola dön gibi komutlar veriyorsunuz. Kamlumbağanın gittiği yol ekranda çizgi olarak görülüyor.

Örneğin ekrana bir kare çizmek için, 4 kere 100 birim ilerle, 90 derece sola dön komutunu verebilirsiniz. Python'da bunu yapmak için, turtle kütüphanesini
kullanıyoruz.

	:::python
	from turtle import Turtle, screen

	wn = screen() # ekranı kontrol etmemizi sağlıyor

	t = Turtle()  # bir adet kaplumbağa oluşturduk.

	for i in range(4):
		t.forward(100) # kaplumbağa 100 birim ilerlesin
		t.left(90)     # 90 derece sola dönsün
		
	wn.exitonclick() # ekrana tıklanınca ekran kapansın

** Şimdi de siz deneyin **: Ekrana bir üçgen çizin!

Fraktal çizmek için ise, en basit yol, recursive fonksiyon kullanmak. Mesela, bir ağaç çizelim;

	:::python
	from turtle import Turtle, Screen

	wn = Screen()

	def tree(length,t):
		if length > 5:
			t.forward(length) # ileri git
			t.right(40)       # sağa dön
			tree(length-15,t) # daha küçük bir ağaç çiz
			t.left(80)        # sola dön
			tree(length-15,t) # daha küçük bir ağaç çiz
			t.right(40)       # Başladığın açıya geri dön
			t.backward(length)# Başladığın noktaya geri dön


	t = Turtle()
	t.left(90) # Yukarıya doğru çizmek için
	t.speed(0) # en hızlı animasyon

	tree(100,t)

	wn.exitonclick()
	
Şöyle bir resim oluşması gerekiyor;

![fractal tree](http://i.imgur.com/Tk1EIT2.png)

Her ne kadar recursive fonksiyonlar basit olsa da, şekiller karmaşıklaştıkça uygulaması daha zor olabilir. Bunun yerine, fraktal çizmek
için L-Sistemi denilen bir sistem kullanacağız. Eğer fraktal meraklısı bir insansanız, L-sistemini zaten duymuşsunuzdur. Bilmeyenler için kısaca
bahsetmek gerekirse; elimizde belli bir karakter string'i var. Bunu belli kurallar çerçevesinde, giderek kendi içerisinde büyütüyoruz. Örnek verelim;

<pre>
	Başlangıç: A
	Kurallar : A -> AB
			   B -> A
			   
	Adımlar:

	1) A
	2) AB
	3) ABA
	4) ABAAB
	5) ABAABABA
	6) ... Böyle gidiyor
</pre>

Peki, bunun fraktallarla ne alakası var? Bildiğiniz gibi (bildiğinizi varsayıyorum) fraktallar kendi içinde yenilenen segmentlerden oluşuyor. İşte bu kendi
içinde yenilenmenin kuralını, L-Sistemi ile belirleyip, kaplumbağa'ya o şekili çizdiriyoruz. 

Örnek olarak, Koch Snowflake şeklinin ilk 3 adımına bakalım.

![Koch Snowflake](http://i.imgur.com/SkDploA.png)

Evet, önce düz bir çizgi ile başladık, daha sonra bu çizgiyi 3'e bölüp, ortadaki kısmı silip, üstüne bir eşkanar üçgen yerleştirdik. Daha sonra da, her çizgi bölümü
için, bunu tekrarlıyoruz. Eğer aynı işlemi 6. adıma kadar devam edersek, şöyle bir şekil elde ediyoruz.

![Koch Snowflake step 5](http://i.imgur.com/pjJe1XX.png)

Şimdi de bu işlemi, L-Sisteminde nasıl ifade edebileceğimize bakalım;

<pre>
	Başlangıç: f
	Kurallar:  f -> f+f--f+f
</pre>

Burada, `f` aksiyonu ileri git, `+` aksiyonu 60 derece sola dön, `-` ise, 60 derece sağa dön manasına geliyor. Şimdi, bu kurallara göre, istediğimiz derinlikle
L-dizisi oluşturacak bir fonksiyon yazalım.

	:::python
	def make_l_string(start, rules, depth):
					string = start
					for _ in range(depth):
							string = "".join(rules[x] for x in string)
					return string
					
	koch_rules = {
			'f' : 'f+f--f+f',
			'+' : '+',
			'-' : '-'
	}

	print make_l_string("f", koch_rules, 3)
	
<pre>
f+f--f+f+f+f--f+f--f+f--f+f+f+f--f+f+f+f--f+f+f+f--f+f--f+f--f+f+f+f--f+f--f+f--f+f+f+f--f+f--f+f--f+f+f+f--f+f+f+f--f+f+f+f--f+f--f+f--f+f+f+f--f+f
</pre>

Buradaki ana fikirden yola çıkarak, farklı fraktallar çizmek için kullanılabilecek python sınıfları hazırladım, kodlar aşağıda;

	:::python
	import turtle

	class advanced_turtle(turtle.Turtle):

		def push_state(self):

			self._stack.append((self.pos(), self.heading()))

		def pop_state(self):

			isdown = self.isdown()
			
			pos, heading = self._stack.pop()

			if isdown:
				self.penup()

			self.setpos(pos)
			self.setheading(heading)

			if isdown:
				self.pendown()

		def draw(self):
		
			for x in self.string:

				self.actions[x](self)

		def fix_rules(self):
			"Add dummy element"

			parts = set("".join(self.rules.keys() + self.rules.values()))

			for x in parts:
				if not x in self.rules.keys():
					self.rules[x] = x

		def init(self, depth, speed=0):

			self._stack = []
			self.speed(speed)

			self.depth = depth

			string = self.begin

			self.fix_rules()
			
			for _ in xrange(depth):

				string = "".join(self.rules[x] for x in string)

			self.string = string

			self.after_init()

		def after_init(self):

			pass


	class koch(advanced_turtle):

		rules = {'f':'f+f--f+f'}

		begin = "f"

		def gforward(self): self.forward(self.length)

		def tright(self): self.right(60)

		def tleft(self): self.left(60)

		actions = {
			"f": gforward,
			"+": tright,
			"-": tleft }

		def after_init(self): self.length = 400 / 3 ** self.depth
		

	class square_koch(advanced_turtle):

		rules = {'f':'f-f+f+f-f'}
		begin = "f"

		def gforward(self): self.forward(self.length)
		def tright(self):   self.right(90)
		def tleft(self):    self.left(90)
		
		actions = {
			'f': gforward,
			'+': tright,
			'-': tleft
		}

		def after_init(self): self.length = 400 / 3 ** self.depth

	class sierpinsky(advanced_turtle):
		
		rules = {'A':'B-A-B', 'B':'A+B+A'}
		begin = 'A'

		def gforward(self): self.forward(self.length)
		def tright(self):   self.right(60)
		def tleft(self):    self.left(60)

		
		actions = {
			'A': gforward,
			'B': gforward,
			'-': tleft,
			'+': tright,
		}

		def after_init(self): self.length = 300 / 2**self.depth

	class fibonacci_tree(advanced_turtle):

		rules = {'1':'11', '0': '1[0]0'}

		begin = "0"

		def gforward(self): self.forward(self.length)
		def branch_left(self): self.push_state(); self.left(45)
		def branch_right(self): self.pop_state(); self.right(45)

		actions = {
			"0": gforward,
			"1": gforward,
			"[": branch_left,
			"]": branch_right
		}

		def after_init(self): self.length = 300 / 2**self.depth

	class dragon_curve(advanced_turtle):

		rules = {'x':'x+yf', 'y': 'fx-y'}

		begin = "fx"

		def gforward(self): self.forward(self.length)
		def tleft(self): self.left(90)
		def tright(self): self.right(90)

		actions = {
			"f": gforward,
			"-": tleft,
			"+": tright,
			"x": lambda self: None,
			"y": lambda self: None,
		}

		def after_init(self): self.length = 300 / (1.5) ** self.depth

	class fractal_plant(advanced_turtle):

		rules = {'X':'F-[[X]+X]+F[+FX]-X', 'F': 'FF'}

		begin = "X"

		def gforward(self): self.forward(self.length)
		def tleft(self): self.left(25)
		def tright(self): self.right(25)
		def push(self): self.push_state()
		def pop(self):  self.pop_state()

		actions = {
			"F": gforward,
			"-": tleft,
			"+": tright,
			"X": lambda self: None,
			"[": push,
			"]": pop
		}

		def after_init(self): self.length = max(120 / 1.9 ** self.depth, 1) 

		

	if __name__ == "__main__":
		
		wn = turtle.Screen()

		k = koch()
		k.init(4) # level of detail
		k.draw()

		wn.clearscreen()
		
		sk = square_koch()
		sk.init(4)
		sk.draw()

		wn.clearscreen()
		
		s = sierpinsky()
		s.init(6)
		s.draw()

		wn.clearscreen()
		
		ft = fibonacci_tree()
		ft.init(6)
		ft.draw()

		wn.clearscreen()
		
		dc = dragon_curve()
		dc.init(10)
		dc.draw()

		wn.clearscreen()

		fp = fractal_plant()
		fp.init(5)
		fp.draw()
		
		wn.exitonclick()
		

Bunlar da sonuçlarımız;

<a href="http://i.imgur.com/4hyocnt.png"><img src="http://i.imgur.com/4hyocnt.png" style="width:850px"></a>

Peki ya bundan sonra? Daha farklı fraktal şekiller çizmek için yeni L-sistemi kuralları araştırılabilir. Eğer yeni şekiller eklersem, onları da daha sonra paylaşırım.