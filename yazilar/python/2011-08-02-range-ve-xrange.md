<!--
.. date: 2011/08/02 03:45:56
.. slug: range-ve-xrange
.. title: Python range ve xrange
.. description: Bu pratik ipucu sayesinde Python 3'de bulunan range fonksiyonunun davranışını, kodları değiştirmeden Python 2'de elde edebilirsiniz.
-->

*Python* 2 ile *python* 3 arasında `range` fonksiyonu farklılık
gösteriyor. *Python* betiklerinde kullanılan bu fonksiyon, eğer doğru
*python* yorumlayıcısında çalıştırılmazsa, istenildiğinden farklı
davranabilir. Bu sorundan kurtulmak için, aşağıdaki yöntemi
kullanıyorum. <!-- TEASER_END -->

Yöntemden bahsetmeden önce, sorun hakkında biraz bilgi vereceğim.
*Python* 2 sürümünde, `range` ve `xrange` adıyla iki farklı fonksiyon
var. `range` isimli fonksiyon, bir liste döndürüyor. `xrange` isimli
fonksiyon ise bir "generator" (tr: üretici) fonksiyon. Bu iki fonksiyon
arasındaki fark, hafıza kullanımında. `xrange` fonksiyonu her
çağırıldığında yeni bir obje döndürdüğü için, daha az hafıza
kullanılıyor.

`range` ve `xrange` arasındaki bu fark nedeniyle, programlarınızda
`xrange` fonksiyonunu tercih edenlerdenseniz, kodlarınızı *python* 3
yorumlayıcı çalışıtırmayacaktır. Çünkü *python* 3 ile birlikte, xrange
fonksiyonu kaldırıldı ve `range` fonksiyonu, *python* 2'deki xrange
fonksiyonu gibi davranmaya başladı.

Aşağıda görülebilen örnek kod ile, *python* sürümleri arasındaki farkdan
oluşan bu sorunun üstesinden gelebilirsiniz. Bu kodları modülünüzün
yukarılarında kullanmalı, ve `xrange` kullanmak yerine range kullanmayı
tercih etmelisiniz. Bu kodun çalıştığı platforma göre, `xrange` ve
`range` fonksiyonu kendiliğinden kullanılacak.

	:::python
	from sys import version_info
	if version_info[0] == 2:
		range = xrange