<!--
.. date: 2013-02-04 11:44:37
.. title: Python'da iki tarih arasındaki gün farkı
.. slug: iki-tarih-arasindaki-gun-farki
.. description: Python da iki tarih arasındaki gün farkını bulmak için datetime modülündeki date objeleri arasında çıkarma işlemi yapılabilir.
-->


Bu çok kısa bir yazı olacak. Elimizde iki adet date veya iki adet
datetime objesi varken;

    :::python
    >>> from datetime import date
	>>> a = date(2012,12,25)
	>>> b = date(2012,12,18)
	>>> a-b
	datetime.timedelta(7)
	>>> (a-b).days
	7

İki tarihi birbirinden çıkarmak timedelta objesi döndürüyor. Bu objenin
de days niteliği iki tarih araındaki zaman farkının gün cinsinden
değeri. Unutmamak için buraya not alıyorum.