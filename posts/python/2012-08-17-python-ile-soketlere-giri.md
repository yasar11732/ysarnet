<!--
.. date: 2012-08-17 15:55:00
.. title: Python ile soketlere giriş
.. slug: soket-socket
.. description: Python socket modülünün kullanımını hiç bilmeyenlere uygun şekilde, örneklerle anlatan bu yazıyı, soket programcılığı yapmak isteyenler okusunlar.
-->


Merhabalar,

Bu yazıda, Python programlama diliyle soketlerin kullanılışı konusuna
kısaca giriş yapmaya çalışacağım. Okuyucuda soketler hakkında temel
bilgilerin olduğunu varsayıyorum. Bunların ne olduğu veya ne için
kullanıldığı konusunda hiçbir bilgisi olmayanlar için şöyle
özetleyebiliriz; **soketler** iletişim kanallarıdır. Bunlar aynı
bilgisayarda iki işlem arası iletişim sağlayabilse de (örn: unix
soketleri) bunları en çok ağ üzerinde iletişim için kullanırız.
İnternetten bilgisayarınıza gelip giden tüm veriler için, mutlaka birer
soket kullanılır.

Anlatıma geçmeden önce şunu da söylemek istiyorum ki, Python'daki
*socket* modülünü lazım olmadıkça kullanmayınız. Demek istediğim şu ki,
bir internet sayfası indirmek için socket açmak, HTTP başlıklarını
göndermek, gerekirse yönlendirilen sayfaya yeniden soket açmak gibi bir
uğraşa girmeyin. Python bu tip yaygın kullanımlar için zaten daha üst
seviye modüllere sahip bir dil. Amerika'yı yeniden keşfetmeye gerek yok. <!-- TEASER_END -->

Öyleyse, Python'daki socket modülünü alternatif bulamadığımız durumlarda
kullanalım. Ağ bakımı/programcılığı konusunda bu modülün kullanım alanı
kendisini belli edecektir.

Bir örnekle başlayalım;

    :::python
    s = socket.socket(
      socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect(("www.google.com.tr", 80))

Bu örnekte bir client (ingilizcede müşteri demek) soket oluşturduk.
Bunun anlamı, bu soket kendisi veri sunmayacak, bir sunucuya bağlanacak
demek. Sunucu programlara ileriki yazılarda göz atmaya çalışacağım.

Soket oluşturma fonksiyonuna ilk verdiğimiz argüman, bu soketin
adresleme şeklini gösteriyor diyebiliriz. Bunun `socket.AF_INET` olması,
bunun bildiğimiz IP adresi soketi olduğunu gösteriyor. Bunun yerine,
`socket.AF_INET6` ile IPv6 kullanabiliriz. Bir de `socket.AF_UNIX` var
ki, bu UNIX soketleri için kullanılıyor. Dolayısıyla her sistemde bu
sabit tanımlı olmayabilir.

İkinci argüman ise bu soketin iletişim tipini gösteriyor.
`socket.SOCK_STREAM`, en yaygın kullanılan [TCP][] iletişim tipidir.
Bundan sonra en yaygın kullanılan iletişim tipi [UDP][] için
`socket.SOCK_DGRAM` sabiti kullanılır.

Daha sonra, elimizdeki `s` isimli soket objesinin `connect` isimli
metoduyla, soketimizi internetteki bir diğer sokete (yani sunucuya)
bağlayabiliriz. Bu metot adres türüne göre farklı argümanlar alabilir.
`socket.AF_INET` için, adres ve porttan oluşan bir *tuple* veri tipi
alır.

Eğer internetle veya işletim sistemiyle ilgili bir hata oluşmadı ise, şu
andan sonra soketimiz yazmak ve okumak için hazır. Bu işlemler için
sırasıyla `send` ve `recv` metotları kullanılır. Aynı örnekten devam
ederek, şunu deneyebiliriz;

    :::python
    s.send("GET / HTTP/1.1\r\nHost: www.google.com.tr\r\nConnection: Close\r\n")
    while True:
        msg = s.recv(512) # 512 byte veri okumaya çalış
        if not msg: # Eğer boş döndüyse,
            break
        print msg

**Not:** Kodlar içerisindeki adres html tagları içinde görünüyorsa,
onları kaldırın. Galiba Tumblr otomatik olarak onu linke çevirmeye
çalışıyor :/

Burada, muhtemelen yapılabilecek en kısa HTTP isteğini gerçekleştirdik.
Daha sonra da, 512 byte'lar halinde okuyabildiğimiz kadar veri okuduk.
İnternetten gelecek verinin tümünün ne kadar olduğunu bilmediğimiz için,
boş veri okuyana kadar okumaya devam etmemiz gerekiyor. Bir yandan
okudukça, bir yandan da ekrana yazmaya devam ettik.

**Ekleme:** `Connection: Close` header'ını eklemek önemli. Bu header
olmazsa, server yeni bir istek almak için bağlantıyı açık tutabilir. Bu
durumda, program bağlantının kapanacağını varsaydığından, bağlantının
iki ucu da diğerinden veri beklerken program donabilir. (bkz: [HTTP
persistent connection][])

<del>Artık `s` isimli soketimizle işimiz bitti. HTTP protokolünde, bir kez
veri okuduktan sonra bağlantı kapanır. Yeni bir sayfa okumak istersek,
sıfırdan bir soket bağlantısı gerçekleştirmemiz gerekir.</del>

Bu yazıda konuya genel bir giriş yaptım. Bir sonraki yazıda sunucu
programlarda soketlerin nasıl kullanılacağına değinmeyi planlıyorum.

  [TCP]: http://tr.wikipedia.org/wiki/TCP
    "Transmission Control Protocol"
  [UDP]: http://tr.wikipedia.org/wiki/UDP "User Datagram Protocol"
  [HTTP persistent connection]: http://en.wikipedia.org/wiki/HTTP_persistent_connection