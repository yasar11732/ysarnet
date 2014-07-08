<!--
.. date: 2012-08-18 13:03:00
.. title: Python ile soketler - 2
.. slug: soket-socket-2
.. description: Python ile soket programcılığı yapmak konusundaki bu yazıda, bir portu dinleme ve bu port ile veri alışverişi yapma konusu anlatılıyor.
-->

Bir önceki yazıda, Python ile soketlerin kullanımı konusuna genel bir
giriş yapmıştım. O yazıda sadece istemci (client) soketlere yüzeysel
olarak değinmiştim. Bu yazıda ise, sunucu özelliği olan programlarda
soketlerin nasıl kullanılacağına değineceğim.

Bu yazıları tek bir seferde okuyup anlamaya daha müsait olması için,
kısa ve öz tutmaya gayret ediyorum. Bu sebeple, bu yazıda sunucu
programlarda kullanıldığını görebileceğimiz [select][] ve
[threading][] gibi modüllerine değinmeyeceğim. Bunun yerine, bunların
kendilerine ait kısa yazılar ile anlatılması bana daha verimli geliyor. <!-- TEASER_END -->

Yine bir örnekle başlayalım;

    :::python
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    
    serversocket.bind((socket.gethostname(), 80))
    serversocket.listen(5)

İlk satırda yeni bir şey yok. Bir önceki yazıda anlatıldığı gibi bir
soket objesi oluşturuluyor. 

İkinci satırda ise, `bind` metodunun kullanıldığını görüyoruz. Sunucu
görevi görecek bir soketin bağlantı kabul etmeden önce, bir adresle
ilişkilendirilmesi gerekir. Aldığı argüman, soketi oluştururken
kullandığımız adresleme türüne (bu örnekte `AF_INET`) göre farklılık
gösterir. Bizim örneğimizde, adres ve porttan oluşan bir *tuple* veri
tipi kullandık.

Burada, `socket.gethostname()` bize bilgisayarımızın ağda kendini hangi
isimle tanıttığını gösteren bir fonksiyon. Bunun yerine, `localhost`
veya `""` da kullanılabilirdi. Ancak bu durumda, bu soket sadece o
bilgisayardan gelen isteklere açık olur. Ağdaki diğer bilgisayarlar, bu
soketimize bağlanamazlar.

İkinci argüman olarak da port numarası belirledik. Soketimizin bu portla
ilişkilendirilebilmesi için, bu portun kullanımda olmaması gerekir. Eğer
başka bir program bilgisayarınızdaki 80 numaralı portu işgal ediyorsa,
işletim sistemi sizin soketinize bu portu vermeyecektir. Bu gibi
durumlarda, ya o portu kullanan işlemin o portu salıvermesini beklemeli
(soketi kapatmasıyla olur) ya da kendinize başka bir port seçmelisiniz.

Bu örnekte kullanılan 80 portu, internet sunucuları tarafından
kullanıldığından, eğer bilgisayarınızda bir internet sunucusu
çalışıyorsa, size verilmeyecektir. Ayrıca, Windowsda bu tip özel
portları kullanabilmek için yönetici hakları gerekebilir. Soketler
konusunda denemelerinizi yaparken, port numarası olarak 4 haneli rasgele
(max: 65536) rakamlar kullanmanızı tavsiye ederim. Ya da, port numarası
olarak 0 vererek, işletimi sisteminin sizin için uygun bir port
seçmesini isteyebilirsiniz.

    :::python
    >>> serversocket.bind((socket.gethostname(),0))
    >>> serversocket.getsockname()
    ('192.168.1.100', 56956)

Örneğimizde, işletim sisteminin bize 56965 numaralı portu tayin ettiğini
görüyoruz.

Soketimizi bir adresle ilişkilendirdikten sonra, artık o adresi
dinlemeye başlayabiliriz. Bunu ilk örneğimizdeki
`serversocket.listen(5)` satırı ile yapıyoruz. Argüman olarak verdiğimiz
5 sayısı, işletim sisteminin bizim için ne kadar bağlantı isteğini
sırada bekleteceğini gösteriyor. Bu durumda, 5 kişi sırada beklerken
eğer altıncı bir kişi bu sokete bağlanmak isterse, o kişi için bağlantı
reddedilecek.

Artık, bağlantı istekleri işletim sistemi tarafından kabul edilip sıraya
konmaya başlandı. Sırada bekleyen ilk isteğimizi kabul edelim;

    :::python
    (clientsocket, address) = serversocket.accept()

`accept()` metodu bize bir *tuple* döndürür. İlk elemanı, bir client
sokettir. Kabul ettiğimiz bağlantıyla iletişim kurmak için, bunun `send`
ve `recv` metotlarını kullanacağız. Bunun ikinci elemanı da, iki
elemandan oluşan başka bir *tuple* olup, ilk elemanı karşı soketin IP
adresi, ikinci elemanı da portudur. Diğer durumlarda olduğu gibi,
soketin adreslendirme türüne göre (`AF_INET`), bu değer de farklılık
gösterebilir.

Yaptığımız şeyi bir bütün olarak görmek için, aşağıdaki kodu
kullanabiliriz;

    :::python
    import socket
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind((socket.gethostname(), 0))
    
    server.listen(5)
    
    print "{}:{} dinleniyor...".format(*server.getsockname())
    
    while True:
        try:
            client, address = server.accept()
            print "{}:{} bağlandı".format(*address)
            print client.recv(4096)
            client.send("Merhaba dünya!")
            client.close()
        except KeyboardInterrupt:
            break
    
    server.close()

Bu programı çalıştırdığınızda, hangi adresi dinlediğini size bildirecek.
O adresi internet tarayıcınızla ziyaret ederseniz (doğru portu
kullandığınızdan emin olun), tarayıcıda "merhaba dünya", program
çıktısında da tarayıcının size gönderdiği HTTP başlıklarını
göreceksiniz.

Bu yazılık da bu kadar olsun. Bir sonraki yazıda birkaç kısayola
değinmeyi planlıyorum. Kolay gelsin.

  [select]: http://docs.python.org/library/select.html
    "Python select modülü"
  [threading]: http://docs.python.org/library/threading.html
    "Python threading modülü"