<!--
.. date: 2012-11-26 16:54:48
.. title: Matlab'da Sieve of Erastosthenes algoritması
.. slug: matlabda-sieve-of-erastosthenes-algoritmasi
.. description: sieve of erastosthenes algoritması bir asal sayı bulma algoritmasıdır. Bu algoritmanın matlab'da uygulanmış hali için bunu okuyun.
-->


Matlab ile sieve algoritması kullanarak asal sayıları bulan bir
fonksiyon yazdım. İlgilenenler aşağıda bulabilir.

    :::matlab
    function P = sieve(x)
    %sieve Find prime numbers up to max using
    %   sieve of Eratosthenes
    P = 3:2:x;
    len = length(P);
    for n=1:fix((sqrt(x) - 1) / 2)
        if P(n)
            P((n+P(n)):P(n):len) = 0;
        end
    end
    
    P = [2 P(P ~= 0)];
    end