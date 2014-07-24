<!-- 
.. description: Önceki girdimdeki Python paket istatistiklerine bazı eklemeler
.. date: 2013/10/18 23:57
.. title: Python Paket İstatistikleri - Ekleme
.. slug: python-paket-istatistik-ekleme
-->


Daha önceki blog yazımda, [Python paketleriyle ilgili bazı istatistikler](python-paket-istatistikleri.html). Python kullanıcıları
mail listesinden bir kişi, bu kadar eğik (skew) bir veride, ortalama ve standard sapma gibi istatistiklerin anlamsız olduğunu
ve parametrik olmayan (non-parametric) istatistiklerin, veriyi daha iyi açıklayacağını belirtti. Bu sebeple, bu yazıda bazı
yeni istatistikler yayınlayacağım. <!-- TEASER_END -->

## Dosya Boyutu

Birinci, ikici ve üçüncü çeyrekler sırasıyla 4KB, 11.5KB ve 38KB. Aşağıda `log(boyut)`'un histogramını bulabilirsiniz.

![Python paket boyutu histogram](/images/figure_1.png)

## İndirmeler

### Günlük

İlk üç çeyrek sırasıyla 0, 2 ve 8. Veriyi log veya karakök alarak normalleştiremediğimden, histogram elde edemedim.

### Haftalık

İlk üç çeyrek sırasıyla 16,39 ve 100.

### Aylık

İlk üç çeyrek sırasıyla 56, 147 ve 375.

## Python kod satırı

Verinin eğikliği popülasyon ortalaması tahminine nasıl etki eder tam olarak emin değilim. Sadece elimdeki
örnek verideki parametreleri belirteceğim. İlk üç çeyrek 48, 199 ve 498 çıktı. Anlaşılan paket indeksindeki
çoğu paket oldukça küçük. Ayrıca bir boxplot da çizmiştim ama, baya bir basık olduğu için onu koymadım buraya.


