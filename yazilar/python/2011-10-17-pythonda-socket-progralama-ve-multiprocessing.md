<!--
.. date: 2011-10-17 19:42:00
.. title: Python ile soket programlama ve multiprocessing modülü
.. slug: soket-programlama-ve-multiprocessing
.. description: Multiprocessing ve socket modüllerini öğrenmek için bu yazıdaki örnekleri inceleyebilirsiniz. Basitçe anlattım.
-->

Bu yazıda, Python'daki multiprocessing ve socket modüllerini kullanarak
basit bir HTTP sunucusu yapacağız. Bu modülleri kullanmak isteyenler
ancak nereden başlayacağını bilemeyenler bu basit örnekle konuya giriş
yapabilirler.

Yaptığım şey özetle şu; 5 tane işlem port 9090'ı
dinliyor. Gelen isteklere sırasıyla cevap veriyorlar. Python içindeki
Threading modülünden farkı ne derseniz, Python'daki GIL (Global
Intrepreter Lock) yüzünden, threading modülü ile birden fazla işlemciyi
aynı anda kullanamıyorsunuz. Ancak multiprocessing ile birden fazla
işlem çalıştığı için, işlemcinizin tüm olanaklarından
yararlanabilirsiniz :) <!-- TEASER_END -->

    :::python
    import multiprocessing as mp
    import logging
    import socket
    import time
    
    logger = mp.log_to_stderr(logging.DEBUG)
    
    def worker(socket):
        while True:
            client, address = socket.accept()
            logger.debug("{u} connected".format(u=address))
            client.send("HTTP/1.1 200 OK\r\n")
            client.send("Content-Type: text/html\r\n\r\n")
            client.send("OK")
            client.close()
    if __name__ == '__main__':
        num_workers = 5
    
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('',9090))
        serversocket.listen(5)
    
        workers = [mp.Process(target=worker, args=(serversocket,)) for i in
                range(num_workers)]
    
        for p in workers:
            p.daemon = True
            p.start()
    
        while True:
            try:
                time.sleep(10)
            except:
                break
    

#### Ekleme:

Ayrıca, Python'daki SocketServer modülün kullanarak şöyle birşeyler
yapmak da mümkün:

    :::python
    import SocketServer
    class MyTCPHandler(SocketServer.BaseRequestHandler):
        def handle(self):
            self.data = self.request.recv(1024)
            self.request.send(self.data)
    
    if __name__ == "__main__":
        HOST, PORT = "localhost", 9090
        server = SocketServer.ForkingTCPServer((HOST,PORT), MyTCPHandler)
        server.serve_forever()
    

Burada normal TCP server yerine, Forking TCP server kullanmayı tercih
ettiğime dikkat edin. SocketServer.TCPServer sınıfı, her seferinde tek
bir istemciye cevap verecek şekilde çalışıyor. ForkingTCPServer ise, her
yeni bağlantı için yeni bir işlem oluşturuyor (fork ediyor.). Böylece
birden fazla bağlantıya aynı anda cevap verebiliyor. Çalışma şekli benim
yukarıda yaptığımdan biraz daha farklı ama, alınan sonuçlar birbirine
yakın.