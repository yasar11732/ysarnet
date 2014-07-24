<!--
.. date: 2011-08-14 23:35:00
.. description: Bazen If-Else yapısı yerine Try-Except kullanmak daha yerinde olabilir. Önce herşey yolunda varsayın, sonra hata varsa düzeltin.
.. slug: if-else-mi-try-except-mi
.. title: If..Else yada Try..Except, hangisi ne zaman kullanılmalı?
-->

Python öğrenen geliştiriciler, birkaç basit ders ardından try...except
yapısıyla hata yakalama ve kurtarma yapmayı öğrenir. Bunu gerekli
yerlerde kullanabilecek bilgi ve deneyim seviyesine kısa sürede
erişebilir. Ancak, try..except yapısının daha egzotik kullanımları da
mümkün. Try..except yapısıyla daha okunaklı ve temiz kod yazılabilir mi,
yada ne zaman bu yapıyı kullanmaktan kaçınmalıdır sorusuna değinmek
istedim. Birazdan okuyacaklarınız, benim bu konudaki kişisel
görüşlerimdir. Kanıtlanmış veya toplumca kabul görmüş gerçekler olabilir
veya olmayabilir. <!-- TEASER_END -->

Bu yazıyı yazmamın arkasındaki sebep [Wikibooks Python Programlama
 makalesi](http://en.wikibooks.org/wiki/Python_Programming/Exceptions#Exotic_uses_of_exceptions)
içinde okuduğum şu cümledir:


> If you have a complicated piece of code to choose which of several
> courses of action to take, it can be useful to use exceptions to jump
> out of the code as soon as the decision can be made.

Kabaca bir çeviriyle diyor ki, eğer birçok seçimin yapılması gereken
karmaşık bir kodunuz varsa, kararın verilebileceği bir aşamada,
exception (tr: istisna, kuraldışılık) kullanarak koddan dışarı sıçramak
yararlı olabilir. Basit bir örnekle açıklamak gerekirse:

	:::python
	def ifelseile(a=None):
		if a is not None:
			return a + 1
		else:
			return 0

	def tryexceptile(a=None)
		try:
			return a+1
		except:
			return 0
Her ne kadar bu iki örnek çok basit örnekler olsa da, ikinci kodun çok
daha okunaklı ve anlaşılır olduğunu farketmişsinizdir. Ayrıca, biraz
önce bahsettiğim wikibooks sayfasında da benzer bir örneğini yaptığı
gibi, `getattr`, `hasattr` gibi fonksiyonlar ve
`__getitem__`, `__setitem__`, gibi metodlar, try..except blokları
ile birlikte daha okunaklı ve programlama mantığını daha düzgün ifade
eden kodlar olabilirler.

	:::python
	# If .. Else
	if hasattr(a,b):
		k = getattr(a,b)
	else:
		k = "öntanımlı_değer"

	# Try .. Except
	try:
		k = getattr(a,b)
	except:
		k="öntanımli_deger"

	# __getitem__ örneği

	my_dictionary = dict()

	if "deneme" in my_dictionary:
		a = my_dictionary["deneme"]
	else:
		a = None

	try:
		a = my_dictionary["deneme"]
	except:
		a = None
Yani, bence, eğer karar verilmesi gereken konu bir exception
oluşturuyorsa, çoğu zaman try .. except yapısı tercih edilmeli, ancak,
bu bazen verimliliği etkileyebilir.

	:::python
	#####
	# Bu örnekde,  if .. else bloğu tercih edilmeli!
	#####

	### IF-ELSE ###

	if isinstance(a,dict):
		zorHesaplananSayi = cokKarmasikHesapYap()
		a["hebele"] = zorHesaplananSayi
	else:
	   oksuz_sayilar += 1

	### TRY-EXCEPT ###

	try:
		zorHesaplananSayi = cokKarmasikHesapYap()
		a["hebele"] = zorHesaplananSayi
	except:
		oksuz_sayilar += 1
Bu örnekde, exception oluşturacak noktaya kadar çok uzun bir işlem
yapılması gerektiği için, if .. else yapısıyla doğrudan bu kısmı atlamak
daha mantıklı. Bu yüzden, try..except yapısını doğru şekilde kullanmak
biraz da programcının maharetine kalıyor.

İyi geliştirmeler.