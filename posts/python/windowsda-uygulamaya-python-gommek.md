<!-- 
.. description: Python'un windows'da çalışması için exe yapmaya alternatif olarak, Python dll'sini kullanan bir program yazma denemesi.
.. date: 2013/10/12 04:15
.. title: cx_freeze ve py2exe alternatifi
.. slug: windows-exe-yapma-alternatifi
-->


Yazdığı kodları Windows'da son kullanıcıya dağıtmak isteyen
Pythoncular bildiğim kadarıyla, iki farklı yol izliyor:

 * Kullanıcıdan Python yüklemesini istemek
 * cx_freeze, py2exe gibi programlarla Python ve yazılan uygulamayı tek dosya altında birleştirmek

Bu iki yöntemin de kendine göre bir takım sıkıntıları var. İlk yöntem, son kullanıcı açısından yorucu olabilir.
Aynı zamanda, son kullanıcının Python'u kuracak ve sistem yoluna ekleyecek kadar bilgili olmasını gerektiriyor.

İkinci yöntem ise, hem bir açıdan kodları sakladığı için açık kaynak felsefesiyle ters düşüyor, diğer yandan
bozuk exe dosyası üretme riski var. Ayrıca, şahsen hiç estetik bulmuyorum bu yöntemi.

Bu yazıda, muhtemel bir üçüncü yöntemden bahsedeceğim. <!-- TEASER_END -->Bu yazıdaki adımları takip etmek istiyorsanız, şunlara ihtiyacınız olacak;

 * Python 2.7.5: Ben bu versiyonu kullandım. Belki bir takım şeyler sürümden sürüme farklılık gösteriyor olabilir.
 * [Visual C++ 2008](http://www.mediafire.com/download/znddpn202gt/vcsetup.exe): C derleyicisi olarak kullanacağız. Python 2.7 sürümüne uyumlu olması için 2008 versiyonu olması önemli
3.x sürümlerinde bu yöntemi denemek isteyen olursa, 2010 sürümü kullanması gerekiyor.

Yapacağımız şeyi özetlemek gerekirse, python'un dll dosyasından, birtakım fonksiyonları çağırarak, Python dosyalarını
çalıştırabilecek ufak bir program yazacağız. Bu programı ve python dll'sini uygulamamızla birlikte dağıtacağız. Bu yaptığımız
şeye, [harici uygulamaya python gömmek](http://docs.python.org/2/extending/embedding.html#embedding-python-in-another-application) deniyor.

İlk önce visual'da yeni boş bir proje oluşturup, bu projenin içinde tek bir dosya açacağız. Ben buna `main.c` dedim, ama ismin bir önemi yok.
İçeriği şöyle olacak:

	:::c
	#define MS_NO_COREDLL
	#include <Python.h>

	int
	main(int argc, char *argv[])
	{
	  PyObject* PyFileObject;
	  putenv("PYTHONPATH=Lib");
	  putenv("PYTHONHOME=.");
	  Py_SetProgramName(argv[0]);
	  Py_Initialize();
	  PyFileObject = PyFile_FromString("main.py", "r");
	  PyRun_SimpleFileEx(PyFile_AsFile(PyFileObject), "main.py", 1);
	  Py_Finalize();
	  return 0;
	}

Bunu derlemek için, visual'a Python'un header ve kütüphanelerini nerede bulacağını, ayrıca, hangi `.lib` dosyasını
kullanacağını belirtmemiz gerekiyor. Gerekli dosya yollarını belirtmek için, *Tools* > *Options* > *Projects and Solutions* >
*VC++ Directories* bölüme gelmemiz gerekiyor. *Show directories for* seçenek kutusundan *include files*'ı seçtikten sonra, `C:\Python27\include`
yolunu ekliyoruz. Bu yolu, kendinize göre ayarlamayı unutmayın.

Bu pencereyi kapatmadan, library files bölümüne de, `C:\Python27\libs` yolunu ekliyoruz ve bu pencereyi kapatıyoruz. Son olarak, projeye sağ tıkladıktan
sonra *Properties* -> *Linker* -> *Inpu*t yolunu izleyip, *Additional dependencies* kısmına `python27.lib` eklemeniz gerekiyor.

Eğer bir sıkıntı yaşanmadı ise, `C:\Users\kullanici\Documents\Visual Studio 2008\Projects\projeadi\Debug` içerisinde, bir
exe dosyası oluşturulmuş olmalı. Eğer *Debug* içerisinde değilse, *Release* olarak da derlemiş olabilirsiniz, oraları arayın biraz, bulursunuz.

Şimdi yapmamız gereken, python dll'sini, hazırladığımız exe'yi, yazdığımız programı temsil eden main.py dosyasını ve gerekli kütüphaneleri
tek klasör altında toplamak. Bunun için, herhangi yerde bir klasör oluşturun ve oluşturduğunuz exe'yi bunun içine atın. Daha sonra, Python dll'sini
bulmanız gerekiyor. `python27.dll` dosyası için `C:\Windows\system` ve `C:\Windows\SysWOW64` klasörlerini kontrol edin. Oralarda bir yerde bulabilirsiniz. Gerekli
kütüphaneler için ise, ben `C:\Python27\Lib` klasörünü olduğu gibi exe'nin bulunduğu yere kopyaladım. Bunların hepsine ihtiyacımız yok, ama
tek tek elle seçmek istemedim. Eğer programınız ihtiyaç duyacaksa, `C:\Python27\DLLs` klasörünü de kopyalayın. Bunu da yaptıktan sonra, main.py dosyasını oluşturup,
içine denemelik kodlar yazmanız gerekiyor.

Tüm bunları yaptıktan sonra, Python'u silip, bilgisayarı yeniden başlattım ve exe'ye tıkladığım zaman main.py dosyası çalıştı. Yalnız, çıktıyı görebilmek
için ya exe'nizi komut satırından çalıştırmanız, veya c kodunuzda `return`'den önce `getchar()` fonksiyonunu çağırmanız gerekiyor.

Böylece, yazdığımız kodları windows üzerinde tıkla-çalıştır haline getirebiliriz. Ayrıca, bu işlemleri bir kez yapmak yeterli, aynı exe dosyasını
farklı projeleriniz içerisine kopyalayıp yapıştırarak, onları da tıkla çalıştır haline getirebilirsiniz. Bana göre, eğer çalırsa, bu yöntem windows
üzerinde Python kodları dağıtmak için ideal bir yöntem olabilir. Ancak, başka kişilerin de bu yöntemi deneyip, çalıştığını teyit etmesi gerekiyor.