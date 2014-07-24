<!-- 
.. description: Evrimsel algoritmları kullanarak, 5x5lik bir gridi, tüm satır ve sütunları aynı olacak şekilde doldurma problemini çözmeye çalıştım.
.. date: 2013/11/04 01:59
.. title: Evrimsel Algoritmalar
.. slug: evrimsel-algoritmalar
-->

Ne zamandır, evrimsel algoritmalar ve genetik algoritmalarına göz atmak istiyordum.. Bugün biraz fırsat bulup, evrimsel algoritmalara
göz attım.

Evrimsel algoritma, bana biraz breadth-first search algoritmalarını andırdı. Genel gidişat şu şekilde:

 * Rastgele bireylerden ilk popülasyonu oluştur
 * Her bireyin, aranan sonuca benzerliğini test et
 * En iyi bireylerden, mutasyon ve eşleşme ile yeni bireyler oluştur.
 * En iyi bireylerden yeni popülasyon oluştur.
 * Yeterince iyi bireyler elde edene kadar tekrarla

Bu tür algoritmaları genelde arama uzayının çok büyük olduğu durumlarda kullanıyorlar. Daha önce gördüğüm algoritmalara
nazaran, doğru sonuca bir hayli hızlı yaklaşıyor, ancak, bazı sıkıntılar da yaşadım, bunlardan birazdan bahsedeceğim. <!-- TEASER_END -->

## Problem

Küçükken, diyanet takvimlerinin arkasında, çözmekten zevk aldığım bir bulmaca vardı. 5x5'lik bir alanı, 1'den 25'e kadar
sayılarla öyle bir şekilde doldurmalısın ki, bütün satır ve sütun toplamları aynı olsun.

Problem, NP-hard gibi görünüyor. Evrimsel algoritmam için iyi bir aday olabilir diye düşündüm. İlk iş, bir sınıf oluşturdum.

	:::python
	class EqualSumGrid(object):
		"""
		Construct n x n matrix such that;

		 * each cell will be filled with numbers from 1 to n ^ 2
		 * sum of each row and column will be equal to sum(range(n**2)) / n

		Genetic Algorithm will be utilized to find the solution.
		"""

		def __init__(self, rowlabels, collabels):
			"""
			len(rowlabels) and len(collabels) should be equal

			rowlabels[i] + collabels[i] should be valid and hashable
			"""
			assert len(rowlabels) == len(collabels)
			self.rowlabels = rowlabels
			self.collabels = collabels
			self.dim = len(rowlabels)
			self.squares = [a+b for a in rowlabels for b in collabels]

			self.sumtarget = sum(range(1, self.dim**2+1)) / self.dim        
			# each row and column is said to be a unit
			self.rows = [[r+c for c in collabels] for r in rowlabels]
			self.columns = [[r+c for r in rowlabels] for c in collabels]
			self.units = self.rows + self.columns

			self.population = None
			
Burada sadece daha sonra kullanacağım değişkenleri başlattım. Pek değişik birşey yok. Evrimsel algoritmayı
kullanmak için, önce rastgele bir popülasyon oluşturmamız gerekiyor.
	
	:::python
    def randompopulation(self, populationsize):
        """
        Initialize a random populations with size populationsize. random.shuffle will be used to shuffle range(1, m*n+1)
        """

        population = []
        genomes = list(range(1,self.dim**2+1))
        
        for i in range(populationsize):
            shuffle(genomes)
            population.append(dict(izip(self.squares, genomes)))

        return population
		
Bu fonksiyon, 1'den n karaye kadar olan sayıları rastgele dizerek, verilen büyüklükte bir popülasyon oluşturuyor. Daha sonra yapmamız
gereken şey, bireylerin aradığımız sonuca ne kadar yakın olduğunu bulmak. Bunun için, cost function (maliyet fonksiyonu) denen fonksiyonlar
kullanılıyor. Ben her bir satır ve sütun için, hata terimini `(olmasını istediğimiz toplam - satır veya sütun toplamı)**2` olarak tanımladım.
Her bireyin maliyeti, hata terimlerinin toplamının karekökü olacak.
	
	:::python
    def costs(self, population):
        """
        Return a list of costs. costs[i] is cost of population[i]
        Each row and column is said to be a unit.
        (sum(unit) - sum(1..n^2) / n) ^ 2 is a squared residual
        costs[i]["SSR"] = sum(squaredresiduals)
        """

        costs = []

        for individual in population:
            errorterms = {}
            for unit in self.units:
                errorterms[str(unit)] = (self.sumtarget - sum(v for k,v in individual.items() if k in unit)) ** 2
            errorterms["SSR"] = sqrt(sum(errorterms.values())) # take square root to normalize
            costs.append(errorterms)

        return costs
		
Asıl maliyet, `errorterms` sözlüğünün içindeki 'SSR' anahtarında. Her satır ve sütunun için ayrı ayrı hata terimlerini gerek duyabilirim diye
döndürüyorum. Artık, yeni bir nesil oluşturabilmek için gerekli fonksiyonlar tanımlandı. Evrimsel algoritmanın en merkezi noktası burası:

	:::python
    def nextgeneration(self, population, costs):
        """
        Picks best 1/4 of population, they survive to next generation
        Randomly mutates them 3 time, and add this to new generation too.

        Best one will get extra mutations
        """
        popfitness = sorted(izip(population, costs), key=lambda x: x[1]["SSR"])

        elites = popfitness[:len(population) / 4]
        nextgen = []
        nextgen.extend(x[0] for x in elites)

        # Random swap 2 squares
        for individual, _ in elites:
            for unit in sample(self.units, 2):
                new_individual = {k:v for k,v in individual.iteritems()}
                values = [new_individual[s] for s in unit]
                for square, value in izip(unit, values[1:]):
                    new_individual[square] = value
                new_individual[unit[-1]] = values[0]
                nextgen.append(new_individual)

        # Shift a row or column
        for individual, _ in elites:
            new_individual = {k:v for k,v in individual.iteritems()}
            s1, s2 = sample(self.squares, 2)
            new_individual[s1], new_individual[s2] = new_individual[s2], new_individual[s1]
            nextgen.append(new_individual)

        king, cost = popfitness[0]

        # Find 2 rows that has biggest error
        r1, r2 = (x[0] for x in sorted(((r[0][0], cost[str(r)]) for r in self.rows), key=lambda x: x[1], reverse=True)[:2])
        
        # Find 2 columns that has biggest error
        c1, c2 = (x[0] for x in sorted(((c[0][1], cost[str(c)]) for c in self.columns), key=lambda x: x[1], reverse=True)[:2])

        # Swap and add

        new_individual = {k:v for k, v in king.iteritems()}
        new_individual[r1+c1], new_individual[r2+c2] = new_individual[r2+c2], new_individual[r1+c1]
        nextgen.append(new_individual)

        new_individual = {k:v for k, v in individual.iteritems()}
        new_individual[r1+c2], new_individual[r2+c1] = new_individual[r2+c1], new_individual[r1+c2]
        nextgen.append(new_individual)
        

        return nextgen

Ben burada bir sonraki nesili elde etmek için, farklı mutasyonlar kullandım. Eşleşme yapmayı da denemiştim,
ama güzel sonuç vermedi. Burada, eski nesilden en uygun çeyreğini, olduğu gibi yeni nesile kopyaladım. Ayrıca,
bunların her biri için, rastgele iki kare seçip bunları yerlerini değiştirip, bu yeni hallerini yeni nesile ekledim.
Bu rastgele iki kare değiştirme işlemini, her birey için 2 şer kez yaptım. Daha sonra, yine bu en uygun 1/4 lük
bireyler için, her birinden bir satır veya bir sütun seçip, bunu sağa veya aşağı doğru, bir adım kaydırdım. Son olarak,
en uygun bireye, ekstra mutasyon uyguladım. Bu nesilden nesile geçişi nasıl kodladığınız, algoritmanızın sonuç üretebilme
gücünü bir hayli değiştiriyor.

Son olarak, ihtiyacım olan şey, ana döngüyü kurmak.

    def geneticsearch(self, maxgenerations = 100, populationsize = 40, limit=0):
        
        population = self.randompopulation(populationsize)
        costs = self.costs(population)
        found = False
        bestcost = -1
        solution = None

        for i in range(maxgenerations):
            SSRS = [c["SSR"] for c in costs]
            bestcost = min(SSRS)
            solution = population[SSRS.index(bestcost)]
            
            
            if bestcost <= limit:
                found = True
                break
		
            population = self.nextgeneration(population, costs)
            costs = self.costs(population)

        return solution, found, i
		
Evet, ana döngüde ekstra birşey yok. Belli şartlar yerine getirilinceye kadar, popülasyonu yeniliyor.

## Çalışma Süresi

Bu algoritmayı, 3x3, 4x4, 5x5 ve 6x6 lık oyunlar için yüzer defa çalıştırdım. Sonuca ulaşmak için gereken
nesil sayıları şöyle oldu.

![](/images/evol3.png)
![](/images/evol4.png)
![](/images/evol5.png)
![](/images/evol6.png)

3x3lük oyunda, çoğu zaman 10 nesilden daha kısa bir zamanda sonuç bulunuyor. 4x4'de bu rakam 80'lere, 5x5'de
300'lere ulaşıyor. 6x6'da ise, sonucu bulmak için, 100'den fazla nesil gerekebiliyor.

Bu biraz benim acemeliğime de gelmiş olabilir ancak, algoritmayı pek scaleable bulmadım açıkçası. Ancak, algoritmanın
şöyle güzel bir yanı var ki, doğru sonuca çok hızlı yaklaşıyor. Örneğin, 5x5lik bir oyunda, her nesilin sonuca ne kadar
yaklaştığını gösteren grafiğe bir bakalım.

![](/images/costpergeneration.png)

Yukardaki grafikte, 79. nesilde gelinen durum, doğru sonuca bir değişim uzak kalınan durum. Yani bir sonraki nesil, doğru
iki kareyi kendi arasında değiştirdiğinde, doğru sonuca ulaşılmış olacak. Ancak bu değişimin gerçekleşme ihtimali çok düşük.
Örneğin, 5x5lik oyunda, yapılabilecek `25*24 = 600` farklı ikili değişim var. Yani, doğru değişimi yapma ihtimali, 1/600. Ancak,
her nesilde tek bir değişim değil, bir sürü değişim yapılıyor tabi ki. Ancak, yine de doğru değişimi yapma ihtimali çok düşük. Bu da
yukarıdaki grafikte, neden doğru sonuca 154. nesilde erişildiğini açıklıyor bence.

Bu algoritma doğru sonuca hızlı yaklaştığı için, belli bir yakınlığa erişinceye kadar bunu, o noktadan sonra, daha kontrollü
bir seçimler yapan bir algoritmayı kullanmak, sonucu bir hayli hızlandırır diye düşünüyorum, ancak henüz bunu denemedim. Belki
müsait bir zamanda onu da denerim.

[Evrimsel algoritma](https://gist.github.com/yasar11732/7296161) kodları her zamanki gibi, gist üzerinde erişilebilir durumda.