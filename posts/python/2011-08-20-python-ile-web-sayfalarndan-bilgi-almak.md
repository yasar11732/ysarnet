<!--
.. date: 2011-08-20 15:27:00
.. title: HTMLParser ve urllib ile Web Sayfalarından Bilgi Almak
.. slug: web-sayfalarindan-veri-okumak
.. description: Python ile internetten sayfa okumak için urllib, bu sayfalardan veri okumak için HTMLParse modülleri kullanılabilir. Bu yazıda örneklerle bunun açıklaması yapılacak.
-->


Bu yazıda, python kullanarak, internet sayfalarını okumak ve bu
sayfalardan ilgilendiğimiz bilgileri toplamakla alakalı küçük bir örnek
yapacağım. Örneğimizde, internetten bir html belgesi alacak ve bu html
belgesindeki javascript'leri bir listeye toplayacağız.

Eğer daha önce bu konuda bir uğraşınız olmuşsa, neden SGMLLib değil de,
HTMLParser kullandığımı merak edebilirsiniz. Bunun nedeni, python 3 ile
birlikte, SGMLLib'in standard python modülleri içerisinden çıkarılması.
HTMLParser modülü de html.parser modülüne taşındı, ancak o sorunu şu
şekilde halledeceğim: <!-- TEASER_END -->

    :::python
    # -*- utf-8 -*-
    from sys import version_info
    if version_info[0] == 2 and version_info[1] >= 2:
        from HTMLParser import HTMLParser
    elif version_info[0] == 3:
        from html.parser import HTMLParser
    else:
        from sys import exit
        print("Python yorumlayıcınız bu programı kullanamaz!")
        exit(1)

HTMLParser sınıfının bir alt sınıfını oluşturmadan önce, bu sınıfın
nasıl çalıştığını bir örnekle açıklamak istiyorum. Aşağıdaki basit html
belgesine bir göz atalım:

~~~~{.html}
<html>
     <head>
          <title>Başlık</title>
     </head>
      
     <body>
          <span id="benimspan" class="7b"></span>
     </body>
</html>
~~~~  

HTMLParser sınıfı bu belgeyi ayrıştırmak için, sırasıyla aşağıdaki
metotları parantez içerisinde gördüğünüz argümanlarla çağıracak:

-   HTMLParser.handle\_starttag("html",[])
-   HTMLParser.handle\_starttag("head",[])
-   HTMLParser.handle\_starttag("title",[])
-   HTMLParser.handle\_data("Başlık")
-   HTMLParser.handle\_endtag("title")
-   HTMLParser.handle\_endtag("head")
-   HTMLParser.handle\_starttag("body",[])
-   HTMLParser.handle\_starttag("span",[("id","benimspan"),("class","7b")])
-   HTMLParser.handle\_endtag("span")
-   HTMLParser.handle\_endtag("body")
-   HTMLParser.handle\_endtag("html")

Ancak, bahsedilen metotların hiçbiri, birşey yapmıyor. HTMLParser
sınıfının bir işe yaraması için, bu sınıfın bir alt sınıfını
oluşturarak, programlama mantığınızı bu alt sınıfta uygulamanız
gerekiyor. Aşağıda benim yaptığım örnek var:

    :::python
    # -*- coding: utf-8 -*-
    from sys import version_info
    if version_info[0] == 2 and version_info[1] >= 2:
        from HTMLParser import HTMLParser
    elif version_info[0] == 3:
        from html.parser import HTMLParser
    else:
        from sys import exit
        print("Python yorumlayıcınız bu programı kullanamaz!")
        exit(1)
        
    
    class ScriptAl(HTMLParser):
        
        def reset(self):
            self.scriptler = []
            self.script_ici = False
            HTMLParser.reset(self)
            
        def handle_starttag(self,tag,ozellikler):
            
            if tag == "script":
                for anahtar,deger in ozellikler:
                    if anahtar == "type" and deger == "text/javascript":
                        self.script_ici = True
                        
        def handle_endtag(self,tag):
            if tag == "script" and self.script_ici:
                self.script_ici = False
                
        def handle_data(self,data):
            if self.script_ici:
                self.scriptler.append(data)

İlk 10 satırda önemli birşey yok, farklı python yorumlayıcılarını
desteklemek için import çağrısını biraz uzattım o kadar. 13. satırda,
asıl işi yapacak sınıfımı oluşturdum. Bu sınıf, HTMLParser sınıfının bir
alt sınıfı. Burada, HTMLParser sınıfının istediğim metotlarını
uygulayarak, kendi sınıfımın yapısını oluşturacağım. *reset* metodu
HTMLParser tarafından, yeni bir belge ayrıştırılmaya başlamadan önce
çağırılıyor. Burada, kullanmak istediğiniz değişkenleri sıfırlamanızı
tavsiye ederim. Daha sonra da HTMLParser.reset(self) ile bu metodun
HTMLParser sınıfındaki davranışını tekrar etmesini sağlayabilirsiniz.

Örnekde programlama mantığım çok basit. Bir *script* etiketi
açıldığında, script\_ici değişkenini True'ya çeviriyorum. Etiket
kapandığı zaman da bu değişkeni False'a geri çeviriyorum. *handle\_data*
metodunda ise, eğer bir script içerisindeysek, verileri listeye
ekliyorum. Aşağıdaki örnekde, bir sayfadaki javascriptlerin hepsini
alıp, bunları bir dosyaya yazacağız. Yukarıdaki kodların scriptal.py
isminde bir dosyada olduğunu, ve bu dosyaların import edebileceğimiz bir
yerde olduğunu varsayın.

    :::python
    from scriptal import ScriptAl
    import urllib
    
    parser = ScriptAl()
    soket = urllib.urlopen("http://tr.myspace.com")
    parser.feed(soket.read())
    soket.close()
    
    dosya = open("scriptler.txt","w")
    for script in parser.scriptler:
        dosya.write("\n")
        dosya.write(script)
        dosya.write("\n\n")
    dosya.close()

Örneğim, bu kadar.İyi geliştirmeler.