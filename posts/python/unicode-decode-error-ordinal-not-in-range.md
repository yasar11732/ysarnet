<!--
.. date: 2013/10/21 21:44
.. slug: unicode-decode-error-ordinal-not-in-range
.. title: UnicodeDecodeError - ordinal not in range(128)
.. description: UnicodeDecodeError neden olur, nasıl düzeltilir?
-->




UnicodeError, Python 2.x sürümlerinde s&#305;kça kar&#351;&#305;la&#351;&#305;lan ve Python diline
veya programlamaya yeni ba&#351;layanlar&#305;n kafas&#305;na kar&#305;&#351;t&#305;rabilecek bir hata.
Ço&#287;u zaman, python dosyas&#305;n&#305;n kulland&#305;&#287;&#305; encoding'i do&#287;ru belirtmemekten
veya internetten al&#305;nan dosyay&#305; do&#287;ru encoding'i kullanarak decode etmemekten
kaynaklanan bu hata, hatan&#305;n do&#287;as&#305;n&#305; bilmiyorsan&#305;z, sizi biraz u&#287;ra&#351;t&#305;rabilir.
Bu yaz&#305; size bu hatan&#305;n neden kaynakland&#305;&#287;&#305;n&#305;, bundan kaç&#305;nmak için neler
yapmak gerekti&#287;ini ve kar&#351;&#305;la&#351;&#305;ld&#305;&#287;&#305; zaman nas&#305;l çözülece&#287;i gösterecek. Bu yaz&#305;,
biraz Python bilen ba&#351;lang&#305;ç seviyesindeki programc&#305;lara yönelik olacak.

Yaz&#305;n&#305;n içeri&#287;i:

 * Temel encoding/decoding konseptleri
 * Python str ve unicode objeleri
 * Do&#287;ru encoding'i tespit etmek <!-- TEASER_END -->
 
Öncelikle, kafan&#305;za yerle&#351;tirmeniz gereken en önemli &#351;ey, **Bilgisayarda
yaz&#305; olmad&#305;&#287;&#305; gerçe&#287;idir.**

Peki o zaman, bizim yazı dosyalarının içinde ne var? Tabi ki sayılar var. Bilgisayarda sadece sayılar vardır! Bir
yazı dosyası oluşturduğunuzda, o yazı, çeşitli şekillerde bir sayı dizisine dönüştürülür. Bunu bir nevi şifreleme
gibi düşünebilirsiniz. Bu şifrelemeye, encoding diyoruz. En eski encodingler'den birisi, ascii olup, şu şekildedir:

![Ascii Tablosu](/images/ascii.gif)

Vakti zamanında bu ascii encoding'i yapan adamlar, ingilizce dışında bir yazının da bilgisayarda kullanılabileceğini
pek akıllarına getirmediğinden olacak, bu encoding sadece İngilizce karakterleri kodlayabiliyor. Ancak, ascii kodlaması
karakter başına 8-bit kullandığından, 128'den 256'ya kadar olan karakterler ascii tablosunda boş kalmış. Daha sonra, bu
eksik kısım çeşitli şekillerde doldurulmuş. Bunlar da code page adını almış. 857 numaralı code page'de bizim Türkçe
karakterler var. Şimdi diyelim ki, ascii kodlaması 857 code page kullanarak bir mail yazdınız ve mailinizin içinde
"Işık ılık süt iç" yazıyor. Sonra da bunu Yunanistandaki bir arkadaşınıza mail attınız. Yunanistandaki arkadaşınız,
bunu kendi ascii code page'i olan 737 ile açtı. Arkadaşınız mailde "IθΞk ΞlΞk sΒt iΘ" okuyacak. Hiç hoş bir durum değil!

Bunun nedeni, 159 sayısı cp857'de ş karakterini kodlamaya yararken, cp737'de θ karakterini kodlamaya yarıyor. Dolayısıyla,
**eğer bir dosyanın hangi encodingle yazıldığını bilmiyorsanız, o yazı hiçbir işinize yaramaz!**

Şimdi biraz da yazıların Python içinde nasıl bulundurulduğuna bakalım. Python 2 sürümünde, iki tür yazı objesi var. Bunlardan
bir tanesi `str`, diğeri `unicode` objesi. Str objesi, bir byte dizisi tutuyor. Yani, encode edilmiş veri tutuyor. Bu str'nin
içinde hangi karakterler olduğunu öğrenebilmemiz ve bunlar üzerinde işlem yapabilmemiz için, bunu doğru kodlama kullanarak
decode edip, Unicode objesine dönüştürmemiz gerekiyor. Siz `str` objeleri üzerinde işlem yaparken, Python gerekli yerlerde
sizin için öntanımlı encoding olan ascii ile bu yazıyı decode ediyor. Peki ya yazı ascii ile kodlanmamışsa?

<pre>
UnicodeDecodeError: 'ascii' codec can't decode byte falance in position filanca: ordinal not in range(128)
</pre>

Peki ne diyor bu hata? Ben bunu ascii kodlaması kullanarak decode etmeye çalıştım ama kodlaması 128'den büyük
olan karakter var, decode edemedim. Hatırlarsanız, ascii kodlamasında sadece 128'e kadar olan karakterler var.

Bu hatadan kurtulmak için, Unicode kullanmamız gereken durumlarda, elimizdeki `str` objesini doğru kodlamayla
decode etmemiz gerekiyor. İşimiz bittikten sonra da, tekrar encode edip, o şekilde kaydetmeliyiz. Örneğin, elimizde
utf-8 ile kodlanmış bir dosya var, ve bu dosya üzerinde işlem yapmak istiyoruz:

	:::python
	with open("dosya.txt") as dosya:
		icerik = dosya.read().decode("utf8")
		
	# icerikle bisiler yap

	with open("dosya.txt","w") as dosya:
		dosya.write(icerik.encode("utf8"))
	
Böylece, doğru kodlamayı kullandığımız sürece, hiçbir problemle karşılaşmayız.

Bu encoding/decoding hatalarının en kolay oluşabileceği durumlar, internet üzerinden veri okunan durumlar. Bazen
aldığımız belgenin hangi kodlamayla yazıldığını bilmemizin hiçbir yolu yok. Böyle durumlarda, şansımıza küselim, çünkü
o belge ile çalışamayız.

Ama bazı durumlarda, aldığımız belgenin hangi kodlamayla kodlandığını bulabileceğimiz yollar var. Örneğin, internetten
bir html dosyası aldığımızda, karşı server bize HTTP header'ları içerisinde `Content-type: text/html; charset=utf8` gibi
bir header gönderebilir. Eğer, bu header'ı aldıysak, işimiz çok kolay, utf8 ile decode edip, dosya üzerinde çalışabiliriz.
Ancak, her zaman karşıdaki sunucu bize kodlama bilgisini sağlamayabilir. Bu gibi durumlarda, html belgesi içindeki, meta
taglarının içinde doğru kodlamayı aramalıyız. Şunlar gibi birşey aramamız gerekiyor:

	:::html
	<meta charset="utf-8">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

Burada ana fikir, herhangi bir html belgesinin üst kısmının ascii kullanarak decode edilebileceği. Eğer
bu yöntemle de doğru kodlamayı bulamazsanız, yapmanız gereken şey o siteyi tasarlayan arkadaşlara negatif enerji göndermek.

Bunlara ek olarak, [chardet](https://pypi.python.org/pypi/chardet) modülü ile, bir belgenin hangi kodlama ile
kodlandığını tahmin etmeye çalışabilirsiniz. Bu modülün teorik olarak kesin doğru sonuç vermesi mümkün değil,
ama bir iki kere denedim, belgelerin doğru kodlamalarını bulabildi.