<!--
.. date: 2013-01-01 18:50:00
.. slug: python-olum-istatistik
.. title: Ben senin 80 yaşına kadar yaşama ihtimalini sevdim.
.. description: TUIK'den alınmış istatistiklere dayanarak, belirli bir yaşa kadar yaşama ihtimalizini hesaplayan bir Python programı.
-->


Aşağıda belli bir yaşa kadar yaşama ihtimalinizi hesaplayan programı
bulabilirsiniz. <!-- TEASER_END -->

    :::python
    # -*- coding: cp1254 -*-
    oranlar = [(8184, 6865), (870, 791), (545, 483),
               (424, 348), (392, 330), (375, 330),
               (339, 412), (281, 261), (235, 204),
               (260, 190), (263, 194), (266, 197),
               (242, 182), (248, 191), (305, 209),
               (358, 224), (404, 215), (472, 211),
               (497, 252), (479, 193), (448, 204),
               (402, 203), (526, 206), (452, 173),
               (474, 219), (471, 215), (494, 224),
               (501, 220), (572, 270), (532, 311),
               (580, 293), (530, 295), (595, 294),
               (550, 260), (487, 290), (552, 332),
               (638, 370), (662, 392), (717, 411),
               (732, 395), (836, 471), (737, 428),
               (855, 487), (809, 459), (1194, 653),
               (1413, 790), (1449, 733), (1518, 695),
               (1643, 785), (1652, 776), (2163, 967),
               (1901, 821), (1888, 846), (1983, 871),
               (3241, 1360), (2991, 1384), (2803, 1304),
               (2936, 1281), (2722, 1192), (2857, 1304),
               (4025, 1967), (3353, 1745), (3435, 1853),
               (3295, 1754), (3585, 2004), (3931, 2302),
               (3823, 2333), (4017, 2414), (4098, 2631),
               (4218, 2728), (4939, 3511), (4837, 3586),
               (4977, 3803), (4820, 3730), (4557, 3953),
               (4646, 3836), (7187, 5059), (7883, 6251),
               (6493, 5918), (5796, 5928), (5567, 6489),
               (5254, 6036), (4864, 6304), (4771, 6247),
               (4417, 6178), (3567, 5339), (3067, 4717),
               (2415, 3809), (1914, 3201), (1533, 2607),
               (1089, 2354), (767, 1796), (508, 1291),
               (487, 1079), (426, 982), (419, 1014),
               (322, 848), (208, 563), (418, 1577)]
    def main():
        current = input("Kac Yasindasin: ")
        target = input("Hedef yasin kac: ")
        sex = input("Erkek için 0, kadın için 1 giriniz: ")
    
        if current > 97:
            import sys
            sys.stderr.write("Sen hala ölmedin mi?")
            sys.exit(1)
    
        if target > 97:
            target = 98
    
        total = sum(x[sex] for x in oranlar[current:])
        part = sum(x[sex] for x in oranlar[current:target])
        senelik = 100 * (float(oranlar[current][sex]) / total)
        print "Bu gün ölme ihtimalin %", senelik / 360
        print "Bu sene ölme ihtimalin %", senelik
        print target, "yaşına kadar yaşama ihtimalin % " , 100 * (1 - (float(part)/total))
    
    if __name__ == "__main__":
        main()
    

Veriler TİK'in 2010 ölüm istatistiklerinden alınmıştır.