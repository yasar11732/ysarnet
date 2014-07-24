<!--
.. date: 2013-01-23 00:18:30
.. slug: bitly-php-kutuphane
.. title: Bitly ve php ile url kısaltmak
.. description: Bir php kütüphanesi aracılığıyla, bitly api'ye bağlanıp, url kısaltma, uzatma ve url istatistikleri alma örneklerle anlatılıyor.
-->


Öncelikle, Php ile bitly apisine erişimimizi sağlayacak kütüphaneyi
[bitly-api-php deposu] üzerinden indiriyoruz. Bu kütüphane henüz (21 ocak 2012) fazla
denenmedi. Ancak, çok önemli bir sorunu görünmüyor.

Bunu kullanabilmek için, php 5 çalıştıran bir web sunucuya da
ihtiyacımız olacak. Bunun dışında, bir bitly login ismi ve bir api
anahtarına da ihtiyaç duyacaksınız. Bunlara [Bitly login and api_key] sayfasından ulaşabilirsiniz.
Ya da [Bitly access token] sayfasından bitly servislerine ulaşmak için kullanacağınız access
token'ı alabilirsiniz. Bunları yaptıktan sonra, yeni bir Bitly objesi
oluşturarak başlayalım; <!-- TEASER_END -->

    <?php
    include("bitly_api.php");
    $bitly = new Bitly(array("login" => "----", "api_key" => "----")); # kendi bilgileriniz doldurun.
    # ya da oauth 2 kullanmak için, access token kullanın.
    $bitly = new Bitly(array("access_token" => "----"))

Artık bitly apisini kullanmaya başlayabiliriz, öncelikle nasıl url
kısaltacağımız görelim;

    <?php
    $data = $bitly->shorten("http://betaworks.com/page?parameter=value#anchor");
    print_r($data);

Şuna benzer bir çıktı alacağız;
<pre>
Array
(
    [long_url] => http://betaworks.com/page?parameter=value#anchor
    [url] => http://bit.ly/XkH7mN
    [hash] => XkH7mN
    [global_hash] => aEemC8
    [new_hash] => 0
)
</pre>

shorten metodu bir array döndürüyor. Bizim ilgilendiğimiz kısa url bu
array'in url anahtarında.  Şimdi de kısaltılmış bir linkin uzun halini
nasıl alabiliriz ona bakalım, bunun için kısa linki veya bunun hash
değerini sorgulatabiliriz.

    <?php
    $params = array(
                "hash" => "XkH7mN"
            );
    $data   = $bitly->expand($params);
    print_r($data);

Çıktı:
<pre>
Array
(
    [0] => Array
        (
            [hash] => XkH7mN
            [long_url] => http://betaworks.com/page?parameter=value#anchor
            [user_hash] => XkH7mN
            [global_hash] => aEemC8
        )

) </pre>

Aynı zamanda, birden fazla hash değerini (api 15'e kadar destekliyor)
sorgulatabilirsiniz:

    <?php
    $params = array(
                "hash" => array(
                    "Xky7y9",
                    "VR455I"
                )
            );
    $data   = $bitly->expand($params);
    print_r($data);

Çıktı:
	
<pre>
Array
(
    [0] => Array
        (
            [hash] => Xky7y9
            [long_url] => https://github.com/
            [user_hash] => Xky7y9
            [global_hash] => 3mWN3O
        )

    [1] => Array
        (
            [hash] => VR455I
            [long_url] => http://www.google.com/
            [user_hash] => VR455I
            [global_hash] => 2V6CFi
        )

) </pre>

Linklerle ilgili ulaşabileceğimiz birkaç metrik var. Tıklanma verileri,
ülkeler, paylaşımlar vs. gibi metrikler var. Tıklanma ilgili metriklere
nasıl ulaşacağımıza bakalım;

    <?php
    print_r($bitly->link_clicks("http://bit.ly/XkH7mN"));

Bu bize çıktı olarak bir sayı verecek. Sonuç olarak, bitly api'si derya
deniz, hepsine tek tek giremiyeceğim, gerisini çözmeyi de okuyucuya
bırakıyorum. Kolay gele...

  [bitly-api-php deposu]: https://github.com/yasar11732/bitly-api-php
  [Bitly login and api_key]: https://bitly.com/a/your_api_key "Bitly login and api_key"
  [Bitly access token]: https://bitly.com/a/oauth_apps "Bitly access token"