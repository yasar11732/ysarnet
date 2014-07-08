<!--
.. date: 2011-08-24 19:54:00
.. title: Django'da Tembel Reverse
.. slug: djangoda-tembel-reverse
.. description: Django'nun bir sonraki sürümünde gelecek olan reverse_lazy fonksiyonunun yerine geçici bir fonksiyon kullanıyorum. Bu yazıda bu fonksiyonun kullanımını bulabilirsiniz.
-->

Django'da `reverse()`, argüman olarak verdiğiniz görünüm fonksiyonuna
giden url'i bulur, ve bu url'i bir karakter dizisi olarak döndürür.
Ancak bazı durumlarda, bu fonksiyonu kullanamazsınız. Örneğin, url
bilgilerini tutan modüle dahil ettiğiniz modüllerde bunu kullandığınızda
sıkıntı çıkaracaktır. Çünkü bu fonksiyonu kullandığınızda, url
bilgilerinin zaten yüklenmiş olması gerekir. <!-- TEASER_END -->

Bu tip sorunların önüne geçmek için, [`reverse_lazy()`](https://docs.djangoproject.com/en/dev/topics/http/urls/#reverse-lazy) fonksiyonu
geliştiriliyor. Yanlış bilmiyorsam, şu anda sadece [django dev versiyonu]nda bulunuyor bu fonksiyon. Bu fonksiyonun özelliği, url'i
aramaya fonksiyon çağırıldığında değil, url kullanılmaya çalışıldığında
başlaması.

Bu fonksiyonun davranışını django'nun kararlı sürümünde şu şekilde
kullanmayı başardım:

    :::python
    from django.utils.functional import lazy
    from django.core.urlresolvers import reverse
    
        
    reverse_lazy = lazy(reverse, str)
    
    # reverse kullanmanız gerektiğinde:
    aradigim_url = reverse_lazy("app.views.view",args=[arguman])
    
    ## reverse fonksiyonu henüz çalışmadı. url'i kullanmaya çalışmanızı bekliyor.
    
    print(aradigim_url)
    
    ## reverse fonksiyonu şimdi çalışıyor, ve url'i ekrana basıyoruz.

  [django dev versiyonu]: https://code.djangoproject.com/browser/django/trunk/django/core/urlresolvers.py