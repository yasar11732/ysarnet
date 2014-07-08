<!--
.. date: 2012-12-18 18:31:18
.. slug: python-narsist-sayilar
.. title: Python narsist sayılar
.. description: Python ile yazılmış, narsist sayıları bulma algoritması. Algoritma meraklıları okuyabilirler.
-->

n haneli bir sayının basamaklarının n'inci üstlerinin toplamı, sayının
kendisine eşitse, böyle sayılara narsist sayılar (armstrong sayıları da
olur...) deniyor. Örneğin, 153, 3 haneli `1^3 + 5^3 + 3^3 = 153`,
olduğu için, 153 sayısı bir armstrong sayısı oluyor. Bununla ilgili bir
forum konusu [şurada][] vardı. Ben de en basitinden şöyle birşey yazdım; <!-- TEASER_END -->

    :::python
    a = input("Kac Hane...")
    
    for i in xrange(10**(a-1),10**a):
        if sum(int(x)**a for x in str(i)) == i:
            print i

Tabi bu geliştirilmeye açık :)

  [şurada]: http://www.istihza.com/forum/viewtopic.php?f=40&t=270