<!--
.. date: 2011-09-03 10:34:00
.. title: Python ve Google Api ile Url Kısaltma
.. slug: google-api-ile-url-kisaltma
.. description: Uzun url'leri kısaltma servisini sağlayan birkaç firma var. Bu yazıda, google api'sini kullanarak nasıl link kısaltılabileceğine değineceğiz.
-->


Url kısaltmak için google kullanmak bana kolay geliyor. Çünkü, temel
işlemler için, api anahtarına ihtiyaç yok. Tek yapmanız gereken,
kısaltmak istediğiniz url'i json formatında, post metoduyla
https://www.googleapis.com/urlshortener/v1/url adresine göndermeniz.
Python ile bunu nasıl yapılacağına ait aşağıda bir örnek var. İhtiyaca
göre düzenlenip, kullanılabilir.

İlk iş, urllib2 ve json modüllerini içe aktarmak. Bu araçlar olmazsa,
http isteği göndermek ve aldığımız cevabı kullanabileceğimiz bir python
değişkenine dönüştürmek, oldukça güç olur. <!-- TEASER_END -->

    :::python
    from urllib2 import urlopen, Request
    from json import loads, dumps

Request ile, bir http isteği hazırlanır. Bu hazırlanan istek, urlopen
ile gerçekleştirilir. loads, bir yazıdan, python sözlüğü oluşturur.
dumps ise bunun tam tersidir. Öylese, dumps'ın kullanacağı bir sözlük
hazırlamak gerekir.

    :::python
    json_sozluk = {"longUrl" : "http://yasar.serveblog.net/post/python-ve-google-api-ile-url-kisaltma/"}

Bu hazırlanan sözlükte, longUrl olmalıdır. Google bizden, bunu ister.
Artık http isteği oluşturmak için, gerekli şeyler hazır.

    :::python
    istek = Request(
        "https://www.googleapis.com/urlshortener/v1/url",
        data=dumps(json_sozluk),
        headers={"Content-Type" : "application/json"}
    )

Content-type http başlığını "application/json" yapmak şarttır, aksi
halde google, isteğinizi reddeder. Artık geriye kalan, Google'dan gelen
cevabı okumaktır, ve bundan bir sözlük yapmaktır.

    :::python
    soket = urlopen(istek)
    
    cevap = loads(soket.read())
    
    soket.close()

Son olarak elimizde kalan, şöyle bir python sözlüğü olur.
`cevap = { "kind": "urlshortener#url", "id": "http://goo.gl/n1G9N", "longUrl": "http://yasar.serveblog.net/post/python-ve-google-api-ile-url-kisaltma/" }`.
Bu sözlükteki id anahtarıyla belirtilen url, sizin google'a
verdiğiniz url'e yönlendirilir. Ancak, google bu url'in zararlı olduğunu
düşünüyorsa başka. O zaman, bu siteye yönlendirme yapılmayabilir. Google
kullanıcılarını korumaya çalışır.

Url kısaltınca, bunun hakkında bilgi de edinilebilir. Bu basit http
isteğiyle olur. [İsterseniz yüzeysel][] yada [detaylı][] bilgiye
erişebilirsiniz.

  [İsterseniz yüzeysel]: https://www.googleapis.com/urlshortener/v1/url?shortUrl=http://goo.gl/n1G9N
  [detaylı]: https://www.googleapis.com/urlshortener/v1/url?shortUrl=http://goo.gl/n1G9N&projection=FULL