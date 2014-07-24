<!--
.. date: 2012-08-30 22:47:00
.. title: socket objelerinden dosya yapmak
.. slug: soket-socket-makefile
.. description: Soket objelerinin makefile metodu sayesinde, soketler üzerinde buffer'lı okuma ve yazma işlemleri yapabilir, bunlarda dosyalardaki gibi readlines() ve benzeri metotlar kullanabiliriz.
-->


Bu kısacık yazıda, Python'daki socket objelerinden dosya objesi elde
etmeye çalışan socket.makefile fonksiyonundan bahsedeceğim; <!-- TEASER_END -->

    :::python
    #coding:utf-8
    import socket
    
    conn = socket.create_connection(("www.google.com",80))
    
    http_request = """GET / HTTP/1.1
    Host: {}
    Connection: Close
    
    """
    conn.sendall(http_request.format("www.google.com"))
    headerlar = {}
    dosya = conn.makefile("r")
    
    for satir in dosya.readlines():
        if not satir.strip():
            break
        if ":" not in satir:
            continue
        header, _, deger = satir.partition(":")
        headerlar[header.strip()] = deger.strip()
    
    dosya.close()
    conn.close()
    
    for k,v in headerlar.items():
        print k, "=>", v

Daha önceki socket yazılarını okuduysanız, burada size yeni olan tek şey
`dosya = conn.makefile("r")` satırı olmalı. Bu satır sayesinde, socket
objesinden bir dosya objesi elde ediyoruz. Bu dosyaya yazdığımızda soket
yazılacak, bundan okuduğumuz da da soketten okunacak. Peki, neden bunu
yapmak isteyelim? Bunu iki nedeni var; birincisi bu dosya objesi
buffer'lı, bu sebeple doğrudan soketten okumaktan daha verimli. İkincisi
ise, dosya objelerindeki readline() ve benzeri fonksiyonlardan
faydalanabiliyoruz. Yukarıdaki örnekte gördüğünüz gibi, soketten
oluşturulmuş bu dosyayı satır satır okuyabiliyoruz.