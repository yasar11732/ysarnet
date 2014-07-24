<!--
.. date: 2012-08-23 00:01:00
.. title: Python soketler için faydalı 2 fonksiyon
.. slug: soket-socket-yardimci-fonksiyon
.. description: Python soket programcılığı sırasında işinizi çok kolaylaştıracak create_connection ve sendall fonksiyonlarının amacını ve kullanımını anlatan bu yazıyı, soketlerle uğraşanların okumasında fayda var.
-->


Python ile soketler serisinin 3. yazısında, iki yeni fonksiyondan
bahsedeceğim. Şu örnek üzerinden gideceğiz; <!-- TEASER_END -->

    :::python
    import socket
    
    def recv_all(sock):
        "Karşı taraf bağlantıyı kapatıncaya soketten okur. Okuduğunu döndürür."
        chunks = []
        while True:
            msg = ""
            msg = sock.recv(4096)
            if not msg:
                break
            chunks.append(msg)
        return "".join(chunks)
    
    http_request = """GET / HTTP/1.1
    Host: {}
    Connection: Close
    
    """
    site = "www.google.com.tr"
    
    conn = socket.create_connection((site,80))
       
    conn.sendall(http_request.format(site))
    
    response = recv_all(conn)
    
    conn.close()
    
    print response

Bu örnek, site değişkeninde verdiğimiz siteye bağlanıp, okuduğu cevabı
ekrana yazıyor. Burada `socket.create_connection` ve
`socket.socket.sendall` olmak üzere iki yeni fonksiyon kullandık.

`socket.create_connection` fonksiyonu, ilk yazı'da örnek verdiğim şu
kullanım için bir kısayol sağlıyor.

    :::python
    s = socket.socket(
      socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect(("www.google.com.tr", 80))

Bu fonksiyon verilen internet adresini dinleyen TCP servisine bağlanır.
Eğer adres olarak numerik olmayan bir sunucu adı verirseniz, bu adı hem
`AF_INET` hem de `AF_INET6` için çözümlemeye çalışır. Başarılı bir
bağlantı sağlayıncaya kadar bu adreslere sırasıyla bağlanmaya çalışır.
Bu fonksiyon, hem IPv4 hem de IPv6 uyumlu programlar yazmamız için çok
faydalıdır.

sendall fonksiyonu ise, send fonksiyonu gibi sokete veri gönderir.
Ancak, send fonksiyonunda verinin tamamının gönderildiğinin bir
garantisi yoktur. send fonksiyonu, kaç byte gönderdiğini döndürür.
Verinin hepsinin gittiğini kontrol etmek ve eksikleri tamamlamak
programcıya düşer. sendall ise, tüm veri gönderilinceye veya bir hata
alıncaya kadar çalışır. Böylece, programcı bu zahmete kendisi katlanmak
zorunda kalmaktan kurtulur.

Bu iki fonksiyonu, soketler konusunda çalışırken kolaylık olması
açısından anlatmak istedim. Kritik fonksiyonlar değiller, ancak,
bilmekte fayda var.

Kolay Gelsin.