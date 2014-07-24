<!--
.. date: 2011-08-06 00:44:00
.. description: Django şablonlarında php kodu nasıl kullanılır? django_php paketi, django şablon dili için PHP desteği sağlıyor. 
.. slug: django-sablonlarinda-php
.. title: Django şablonlarında php
-->


django\_php paketiyle django uygulamalarınızın web şablonlarında php
kullanmanız mümkün. Bunu neden yapmak isteyeceğiniz ise tamamen bir
muamma... <!-- TEASER_END -->

Kurulum
-------

Komut satırından

	:::terminal
	easy_install django_php

veya

	:::terminal
	pip install django_php

komutlarıyla kurabilirsiniz. Tabi ki bu komutları vermek için gerekli
python paketlerinin yüklü olmasını gerektiğini unutmamak gerek.

Daha sonra django\_php'yi settings modülü içerisindeki INSTALLED\_APPS
listesine ekleyerek kullanmaya başlayabilirsiniz.

	:::python
	INSTALLED_APPS = (
	   'django_php',
	)
django\_php'yi kullanmadan önce php\_cgi'in sisteminizde yüklü
olduğundan emin olun. Eğer php\_cgi'in yerini belirtmeniz gerekiyorsa,
settings modülü içerisinde

	:::python
	PHP_CGI = '/usr/local/bin/php-cgi'

şeklinde belirtebilirsiniz. Çoğu zaman bu ayarı yapmanıza gerek yoktur.


Şablonlarınızın içine php'yi dahil etmek için de, şablon dosyalarınızın
içinde:

	{% load php %}
	{% php echo 9; %}
şeklinde kullanabilirsiniz. Daha fazla örnek kaynak kodlarının içinde
mevcut.

##### İlgili Linkler:

 - [Proje anasayfası](http://animuchan.net/django_php/)
 - [PYPI Sayfası](http://pypi.python.org/pypi/django_php)
 - [Kaynak Kodları](https://github.com/mvasilkov/django-php)