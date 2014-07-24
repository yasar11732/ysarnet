<!--
.. date: 2011-12-29 10:57:00
.. title: Toplu halde http durum kodu alma
.. slug: toplu-halde-http-durum-kodu-alma
.. description: threading, Queue, httplib gibi modüllerin kullanımına dair bir örnek görmek için okuyun. Bir yığın url'in HTTP durum kodunu alacağız.
-->

Bu yazıda, kullanımı hakkında sıkça soru sorulan threading, Queue, httplib gibi
modülleri kullanılarak çalışan bir uygulama örneği var. Bu modülü kendi kullanımım
için yazmıştım, burada paylaşıyorum. <!-- TEASER_END -->

    :::python
    #! /usr/bin/env python2
    # -*- coding: utf-8 -*-
    import os, time
    import threading, Queue
    import httplib
    from urlparse import urlparse
    import sys
    
    class WorkerThread(threading.Thread):
    
        def __init__(self, dir_q, result_q):
            super(WorkerThread, self).__init__()
            self.dir_q = dir_q
            self.result_q = result_q
            self.stoprequest = threading.Event()
    
        def run(self):
            while not self.stoprequest.isSet():
                try:
                    url = self.dir_q.get(True, 0.05)
                    parsed_url = urlparse(url)
                    if parsed_url.scheme == "http":
                        conn = httplib.HTTPConnection(parsed_url.netloc, timeout=2)
                    elif parsed_url.scheme == "https":
                        try:
                            conn = HTTPConnection(parsed_url.netloc, timeout=2)
                        except AttributeError:
                            self.result_q.put(("","",""))
                            continue
                    else:
                        sys.stderr.write("%s için hatalı url şeması: '%s'\n" % (url,parsed_url.scheme))
                        self.result_q.put(("","",""))
                        continue
                    conn.request("HEAD", parsed_url.path)
                    response = conn.getresponse()
                    self.result_q.put((url, response.status, response.reason))
                except Queue.Empty:
                    continue
                except Exception as e:
                    sys.stderr.write("%s => %s\n" % (url,e))
                    self.result_q.put(("","",""))
                    continue
    
        def join(self, timeout=None):
            self.stoprequest.set()
            super(WorkerThread, self).join(timeout)
    
    def main(args,workers = 5):
        dir_q = Queue.Queue()
        result_q = Queue.Queue()
    
        pool = [WorkerThread(dir_q=dir_q, result_q=result_q) for i in range(workers)]
    
        for thread in pool:
            thread.start()
    
        work_count = 0
        for dir in args:
            work_count += 1
            dir_q.put(dir)
    
        print '%s işçiye %s url atandı.' % (workers,work_count)
    
        while work_count > 0:
            url, status, reason = result_q.get()
            if url:
                print("{url} => {code} ({reason})".format(url=url, code = status, reason = reason))
            work_count -= 1
            
        for thread in pool:
            thread.join()
    
    if __name__ == '__main__':
        try:
            main([i.strip() for i in open(sys.argv[1],"r").readlines()],workers=40)
        except IndexError:
            main([i.strip() for i in sys.stdin.readlines()],workers=40)
    