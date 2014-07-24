<!--
.. date: 2011-08-14 16:23:00
.. description: Bir spell-correct (Yazım Düzeltme) algoritması kullanarak, django uygulamamızda, kullanıcıyı doğru url'e gönderecek kodları yazacağız.
.. slug: url-duzeltme-algoritmasi
.. title: Django ve Url Düzeltme
-->


Internet tarayıcısına elle url girenler, url'leri yanlış yazmalarından
dolayı gördükleri 404 sayfalarını hatırlayacaktır. Bu 404 sayfaları
sinir bozucudur. Özellikle de ziyaretçiye kolaylık sağlayan bir
özellikleri yoksa. 404 sayfaları, ziyaretçiye site haritası sunarak, ya
da ziyaretçiye bazı önerilerde bulunarak ziyaretçiye kolaylık
sağlayabilir. Ancak, 404 sayfasını atlayıp, ziyaretçiyi gerçekten gitmek
istediği sayfaya yönlendirmek en doğrusu olacaktır. <!-- TEASER_END -->

Ziyaretçileriniz gerçekten nereye gitmek istediklerini anlamak için, bir
[yazım düzeltme algoritması][]'na ihtiyaç duyacaksınız. Ben, verdiğim
bağlantıdaki algoritmanın, biraz basitleştirilmiş bir halini
kullanacağım.

	:::python
	alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789-'
	# http://norvig.com/spell-correct.html adresindeki algoritma değiştirilmiştir.
	def suggest(word,Nwords):
	   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
	   deletes    = [a + b[1:] for a, b in splits if b]
	   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
	   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
	   inserts    = [a + c + b     for a, b in splits for c in alphabet]
	   all_suggestions = set(deletes + transposes + replaces + inserts)
	   return [suggestion for suggestion in all_suggestions if suggestion in Nwords]

ilk satırda tanımladığımız, *alphabet* karakter dizisindeki her
karakter, yanlış kelimedeki eksik karakteri doldurmak için veya yanlış
karakterleri değiştirmek için kullanılacak. 3. satırda, tanımladığım
fonksiyon, 2 argüman alıyor. İlk argümanı, düzeltilmek istenen karakter
dizisi, diğeri ise, tüm düzgün kabul edilen karakter dizilerini içinde
barındıran bir liste. 4. satırda, splits listesi tanımlanarak, verilen
kelimenin tüm ikiye bölünme ihtimalleri bu listede toplanıyor. Örneğin:

	:::python
	a = "yasar"
	def splits(word):
	   return [(word[:i], word[i:]) for i in range(len(word) + 1)]
	print(splits(a))
	# [("","yasar"),("y","asar")...,("yasar","")] gibi bir liste döndürür.

Daha sonra tanımlanan deletes listesi, verilen kelimenin bir harfi eksik
tüm farklı şekillerini içinde barındırıyor. Bunu yapmak için, bir önceki
satırda tanımladığımız splits listesinin içindeki her ikiliden
ikincisinin ilk karakterini siliyor. Daha sonra tanımladığımız
transposes listesi ise, yanyana harf değişimlerinin tüm çeşitlerini
içinde barındırıyor. Son olarak da, inserts isminde bir liste oluşturup,
bu listeye verilen kelimenin mümkün olan her yerine, *alphabet*
içerisinden her harfin bir kez eklendiği bütün versiyonlarını tutuyor.
Örneğin, "yasar" kelimesi verildiğin, kelimenin başı ve sonu ilk y ile a
arası, gibi toplamda 6 tane harf eklenebilecek yer var. *alphabet*
karakter dizisinde 37 karakter olduğu için, insert listesi 6x37 = 222
kelimeden oluşacak. Daha sonra, tüm bu hesaplanan doğru kelime
adaylarını, tek bir listede birleştiriyoruz. Son olarak, hesapladığımız
önerilerden, kabul edilebilir kelimeler listesinde olanları bir liste
olarak döndürüyoruz.

Url düzeltmeyi gerçekleştirebilmek için, url içerisinde veya
dekoratörleri içerisinde *get\_object\_or\_404* gibi standart 404
sayfası gösterilmesine neden olacak fonskiyonların etkisini dikkate
almak gerekiyor. Eğer, url düzeltme mekanizmanız çalışmadan, başka bir
yerde Http404 hatası verilirse, url düzeltme algoritmanız işe
yaramayacaktır. Örnek bir görünüm fonksiyonu şöyle olabilir.

	:::python
	from django.http import Http404, HttpResponsePermanentRedirect, HttpResponseNotFound
	from django.views.decorators.http import condition
	from portal.blog.models import Post
	from django.template import Context, loader

	def last_modified(request,slug):
		"""
		Burada, get_object_or_404 kullanmaktansa, try except kullandım.
		Burada oluşacak bir Http404 hatası, url düzetmenin çalışmasına engel olacaktır.
		"""
		try:
			post = Post.objects.get(slug=slug)
			return post.last_mod
		except Post.DoesNotExist:
			return None

	def handlenotfound(request,suggestions = None):
		"""
		Burada, şablonumuzun içerisine önerileri göndererek, önerileri ziyaretçiye
		sunabiliriz. HttpResponseNotFound döndürdüğümüze dikkat edin. Böylece, 
		arama motorları buranın geçerli bir sayfa olmadığını anlayıp, indekslerine almayacaktır.
		"""
		datas = { 'suggestions' : suggestions}
		template = loader.get_template("404.html")
		icerik = Context(datas)
		return HttpResponseNotFound(template.render(icerik))

	# Her ne kadar bu dekoratörün konumuzla bir alakası olmasa da
	# bir dekoratör örneği göstererek, dekoratör içerinde get_object_or_404
	# kullanmamak gerektiğine dikkat çekmek istedim.

	@condition(last_modified_func=last_modified)
	def post(request,slug):
		"""
		get_object_or_404 olmadığına dikkat edin. Bunu yerine, exception yakalayarak
		önerileri yüklemeye çalışacağız.
		"""
		try:
			p = Post.objects.get(slug=slug)
		except Post.DoesNotExist:
			suggestions = suggest(slug, [p.slug for p in Post.objects.filter(yayinlandi=True)])
			if len(suggestions) == 0:
				raise Http404 # Eğer öneri yoksa, standart 404 sayfası göstermekten başka çare yok.
			elif len(suggestions) == 1:
				p = Post.objects.get(slug = suggestions[0]) # Eğer sadece 1 öneri varsa, doğrudan oraya yönlendirebiliriz.
				return HttpResponsePermanentRedirect(p.get_absolute_url())
			else:
				posts = [Post.objects.get(slug=suggestion) for suggestion in suggestions]
				suggestions = [p.get_absolute_url() for p in posts]
				# Eğer elimizde 1den fazla öneri varsa, standart 404 sayfası yerine, önerileri gösterecek
				# bir 404 sayfası göndermek daha iyidir.
				return handlenotfound(request,suggestions)
		# Eğer except'in içerisine girmediyse, zaten herşey yolundadır.
		datas = {
			"post" : p,
		}
		return render_to_response('blog/post.html',datas)

Yukarıdaki örnek için gerekli açıklamaları, yorumlarla birlikte yaptım.
Her ne kadar, burada bahsedilen algoritma çok profesyonel, yada hız
canavarı bir algoritma olmasa da, çoğu durumda işinizi görecektir. Eğer
hala başlamadıysanız, tarayıcınızın url çubuğuyla oynamaya
başlayabilirsiniz. Son olarak bir tane de **öldülsüz** zeka sorusu, bu
sayfaya ulaşmak için yukarı örneği verilen algoritma kullanıldığına
göre, kaç farklı adres bu sayfaya yönlendirilir?

  [yazım düzeltme algoritması]: http://norvig.com/spell-correct.html