<!--
.. date: 2012-08-22 16:49:00
.. title: Windows'da Python eklentisi nasıl derlenir?
.. slug: eklenti-windows-derleme
.. description: C ile yazılmış bir eklenti modülünü Windows platformu üzerinde derlemeyi örneklerle anlatan bu yazıyı, Python için C eklentisi geliştirmek isteyenler okuyabilir.
-->


Bir soru üzerine, windows'da Python eklenti modülü derlemeyi denemeye
karar verdim. İlk önce deneme amaçlı olarak, internetten çok basit bir
eklenti modülü arakladım ve *hello.c* ismiyle kaydettim. <!-- TEASER_END -->

    :::c
    #include 
    
     
    static PyObject* helloworld(PyObject* self)
    {
        return Py_BuildValue("s", "Hello, Python extensions!!");
    }
    
    static char helloworld_docs[] =
        "helloworld( ): Any message you want to put here!!\n";
    
    static PyMethodDef helloworld_funcs[] = {
        {"helloworld", (PyCFunction)helloworld, 
         METH_NOARGS, helloworld_docs},
        {NULL}
    };
    
    void inithelloworld(void)
    {
        Py_InitModule3("helloworld", helloworld_funcs,
                       "Extension module example!");
    }

Kaynak: [http://www.tutorialspoint.com/python/python_further_extensions.htm](http://www.tutorialspoint.com/python/python_further_extensions.htm)

Daha sonra, bir windows'da bir derleyicim olmadığı için, [mingw'nin son sürümünü][] indirip, sorunsuzca kurdum. Daha sonra, yine aynı yerden
gerekli setup.py dosyasını arakladım;

    :::python
    from distutils.core import setup, Extension
    setup(name='helloworld', version='1.0',  \
          ext_modules=[Extension('helloworld', ['hello.c'])])

Daha sonra, mingw ve distutils'e birkaç ince ayar çekmem gerekti.
Öncelikle, *C:\\MinGW\\bin* adresini Path'e ekledim. Tıpkı daha önce
[Python'u eklemiş olduğum][] gibi. Sonra, *C:\\Python27\\Lib\\distutils*
adresine distutils.cfg isimli bir dosya açıp, şunu yazdım;

<pre>
[build]
compiler=mingw32
</pre>

Böylece, artık distutils hangi derleyici kullanması gerektiğini
bilebilecek. Daha sonra [bir bug] dolayısıyla, *C:\\Python27\\Lib\\distutils\\cygwincompiler.py* dosyasında gördüğüm `-mno-cygwin`'leri kaldırdım. Bu bug mingw'nin son
sürümünde `-mno-cygwin` seçeneği kalktığı halde, elimdeki Python'da
henüz bunun güncellenmemesinden kaynaklanıyor. Herkesde bu hata
olmayabilir.

Daha sonra, windows komut satırından *hello.c* ve *setup.py*
dosyalarının olduğu yere gelip, şu komutu verdim;

    :::python
    python setup.py install

Sorunsuz bir şekilde derlendi
ve *C:\\Python27\\Lib\\site-packages\\helloworld.pyd *dosyası
oluşturuldu. Artık, python komut satırından modülümüzü import edip
kullanabiliriz;

    :::python
    >>> import helloworld
    >>> help(helloworld)
	"""
    Help on module helloworld:
    
    NAME
        helloworld - Extension module example!
    
    FILE
        c:\python27\lib\site-packages\helloworld.pyd
    
    FUNCTIONS
        helloworld(...)
            helloworld( ): Any message you want to put here!!
    
    >>> dir(helloworld)
    ['__doc__', '__file__', '__name__', '__package__', 'helloworld']
    >>> helloworld.helloworld()
    'Hello, Python extensions!!'
	"""

İlginç bir şekilde, .dll uzantılı bir dosya beklerken, .pyd uzantılı bir
dosya elde ettim. Bunun nedenini araştırdım. [Öğrendim ki][], pyd
dosyaları DLL imiş. pyd demek, Python eklentisi olan DLL demek
oluyormuş.

Bu arada, eklenti derlemenin birden fazla yolu olabilir. Bana en rahat
gelen yöntem bu olduğu için bu şekilde derledim. Umarım faydalı
olmuştur.

  [mingw'nin son sürümünü]: http://sourceforge.net/projects/mingw/files/latest/download
    "mingw"
  [Python'u eklemiş olduğum]: http://www.istihza.com/py2/windows-path.html
    "Windows'ta Python'ı YOL'a (PATH) Eklemek"
  [bir bug]: http://bugs.python.org/issue12641
    "Remove -mno-cygwin from distutils"
  [Öğrendim ki]: http://docs.python.org/faq/windows.html#is-a-pyd-file-the-same-as-a-dll
    "Is a *.pyd file the same as a DLL?"