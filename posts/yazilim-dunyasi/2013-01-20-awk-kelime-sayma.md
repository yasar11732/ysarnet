<!--
.. date: 2013-01-20 02:21:00
.. title: awk'da kelime sayma programı
.. slug: awk-kelime-sayma
.. description: Bu birkaç satırlık awk programı ile bir dökümandaki kelimeleri sayabilirsiniz.
-->


	#!/usr/bin/awk -f
	BEGIN {
		FS="[^A-Za-z]"
	}
	{
		for (i=1; i<NF; i++) {
			words[i]++;
		}
	}
	END {for (word in words) print word,words[word]}
    
Bir diğer gece yarısı çiziktiriği...