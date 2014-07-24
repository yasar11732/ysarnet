<!--
.. date: 2013-08-14 03:13:20
.. slug: java-izlenimleri-2
.. title: Java izlenimleri 2
.. description: 1-2 haftalık java deneyimimden sonra, java'nın biraz fazla yorucu olduğuna karar verdim. Üstelik, bir c performansı da sağlamıyor. Ancak, yanlış yapma riskiniz bir hayli düşük bu dilde.
-->


Yaklaşık 1 haftadır (belki daha fazla da olabilir, tam emin değilim) az
çok Java'yla uğraşıyorum, az çok birşeyler yazdım;

-   [yas][] git benzeri versiyon kontrol sistemi (gibi birşey)
-   [HttpTools][] Http araçları kütüphanesi olacak, şimdilik sadece
    sitelerin durum kodların topluca almaya yarayan bir class var.
-   [MathTools][] Asal sayı, narsist sayı bulma ve labirent oluşturma
    class'ları
-   [wikicategory][] WikiPedia'a bir kategorideki makaleleri komple
    almak için bir class 

Java'nın ve NYP'nin mantığını biraz daha iyi kavramaya başladığımı
hissediyorum. Ancak, halen alışamadığım şeyler var. <!-- TEASER_END -->Örneğin, şu program
kullanıcıdan bir sayı isteyip, o sayıya kadar olan sayıları ekrana
basıyor; <!-- TEASER_END -->

	:::java
	package com.github.yasar.AllStupidThings;

	import java.io.BufferedReader;
	import java.io.IOException;
	import java.io.InputStreamReader;

	public class WhileLooper {

		public static void main(String[] args) {
			Integer num;
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			System.out.println("Enter a number\t");
			try {
				num = Integer.parseInt(br.readLine());
			} catch (IOException e) {
				System.err.println(e.getMessage());
				return;
			}
			int i = 0;
			do {
				i++;
				System.out.println(i);
			} while (num>i);

		}
	}

Problem şu ki, bu kadar basit bir şey için, bu kadar çok kod yazmak
zorunda kalmam. Örneğin Python ile;

	:::python
	for i in range(0,input("Bir sayi giriniz:\t")):
		print i + 1

C ile ise sanırım şöyle birşey olur.
	
	:::c
	#include <stdio.h>

	int main() {
		int n;
		printf("Lutfen bir sayi giriniz:\t");
		scanf ("%d",&n);
		int i = 0;
		do {
			i++;
			printf("%d\n");
		} while (i<num);
		return 0;
	}

Bu kadar basit bir şekilde yapabiliyoruz. Ben açıkcası Java'nın biraz
daha ifade yeteneği yüksek bir dil olmasını bekliyordum. Belki henüz tam
anlamıyla dile hakim olmadığım için öyle geliyordur. 

Neyse, bekleyip göreceğiz.

  [yas]: https://github.com/yasar11732/yas
  [HttpTools]: https://github.com/yasar11732/HttpTools
  [MathTools]: https://github.com/yasar11732/MathTools
  [wikicategory]: https://github.com/yasar11732/wikicategory