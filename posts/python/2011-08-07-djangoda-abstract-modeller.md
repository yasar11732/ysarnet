<!--
.. date: 2011/08/07 23:19:00
.. description: Django'da abstract model nasıl oluşturulur? Django modelleri arasında inheritance (kalıtım/miras) nasıl olur? Bu yazıda örnek bir Django abstract modeli oluşturulacak.
.. slug: django-abstract-model
.. title: Django'da Abstract Modeller
-->


Django'da abstract modellerin kullanımını merak edenlere yönelik, kısa
ve öz bir yazı olacak bu.

Django'da birbirine çok benzer modeller oluşturacağınız zaman, bir adet
abstract model oluşturup, daha sonra o abstract modeli kullanarak asıl
modellerinizi oluşturabilirsiniz. abstract (tr: soyut) modellerin
kendileri veritabanında bir tablo oluşturmak için kullanılmazlar, bunun
yerine diğer modeller için temel oluştururlar. Bir örnekle inceleyelim: <!-- TEASER_END -->

	:::python
	class MotorluArac(models.Model):
		model = models.CharField(max_length=100)
		yas = models.PositiveIntegerField()
		plaka = models.IntegerField()
		class Meta:
			abstract = True

	class Araba(MotorluArac):
		abs_var_mi = models.BooleanField()

Bu örneğimizde, MotorluArac abstract modelini kullanarak oluşturduğumuz
Araba modelinin, model, yas, araba ve plaka olarak 4 farklı alanı
olacak. MotorluArac abstract modelini kullanarak istediğimiz kadar yeni
model üretebiliriz.

Deneyimli python programcıları, Araba modelinde Meta sınıfının üstüne
yazmadığımız için, bu modelin de bir abstract sınıf olacağını
düşünebilirler, ancak Django bu problemi bizim için hallediyor.

abstract model kullanarak oluşturduğumuz modellerin kendi Meta
sınıflarını oluştururken, isterseniz abstract modelin Meta sınıfından
kalıtım alabilirsiniz (eng: inherit, extend)

	:::python
	class Araba(MotorluArac):
		abs_var_mi = models.BooleanField()
		class Meta(MotorluArac.Meta):
			db_table = "araba_tablosu"