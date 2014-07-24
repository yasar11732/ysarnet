<!--
.. date: 2011/08/04 11:41:00
.. description: Django'da debugging yapmanın doğru yolu nedir? Django uygulamalarınızı hata ayıklamasını (debugging) Python debugger, kısa adıyla pdb kullanarak yapabilirsiniz.
.. slug: pdb-ile-debug
.. title: Django'da pdb ile debug
-->


Django’da geliştirdiğimiz web uygulamasının hata temizlemesini
isterseniz pdb (python debugger) ile de yapabilirsiniz. Bu yazıda kısaca
bunun nasıl yapıldığından bahsedeceğiz. 

Django’nun kendine ait bir debug aracı var, ama *django* ile python
debugger kullanmak isteyenler için, *django-pdb* var. *django-pdb*
sayesinde *django* uygulamalarımızı *pdb* ile debug edebiliriz.
*django-pdb*’nin kurulumu *pip* ile kolayca yapılabilir.
`pip install django-pdb` komutu *django-pdb*’nin kurulumunu sizin için
yapacaktır. \*Nix kullananların kendi dağıtımlarına ait depoları kontrol
etmelerinde de fayda var. Eğer depolarda bulabiliyorsanız, kendi paket
yöneticinizle de kurabilirsiniz. <!-- TEASER_END -->

	:::terminal
	pip install django-pdb

Kurulumu tamamladıktan sonra *django* ayar dosyanızdaki, yüklü
uygulamalara (`INSTALLED_APPS`) *django\_pdb*’yi ekleyerek *django’da*
geliştirdiğimiz siteye dahil ediyoruz.

	:::python
	INSTALLED_APPS = (
	  'django_pdb',
	)

Python Debugger’ın çalışması için birkaç farklı yöntem var, ama hepsi için
settings modülündeki `DEBUG` değişkeninin, `True`’ya eşitlenmesi
gerekiyor. Aksi halde çalışmayacaktır. `settings.DEBUG`’ın `True`
olduğundan emin olduktan sonra, ek bir işlem yapmadan *django’nun* kendi
geliştirme sunucusunu başlatabilirsiniz. GET metodunda *pdb* olan
herhangi bir sayfa’yı açmaya çalıştığınızda *pdb* devreye girecektir.
(ÖRN: www.ornek.com/?pdb)

	:::python
	DEBUG = True

Eğer geliştirme sunucunuzu `--pdb` anahtarı ile başlatırsanız,
yüklediğiniz her view sayfasıyla birlikte pdb devreye girecektir.

	:::terminal
	manage.py runserver --pdb

django-pdb'yi [PYPI](http://pypi.python.org/pypi/django-pdb) sayfasından indirebilirsiniz.

*[PYPI]: Python Package Index