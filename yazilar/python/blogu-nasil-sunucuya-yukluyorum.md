<!-- 
.. description: rsync kullanamadığım için, değişen dosyaları bulmak için sha256, dosyaları upload etmek için ftputil kullanıyorum.
.. date: 2013/10/25 22:36:29
.. title: Bloğu nasıl sunucuya yüklüyorum?
.. slug: sha256-ftputil
-->

Bu bloğu barındırdığım sunucumda, rsync kullanma ihtimalim yok, çünkü sadece
html dosyaları upload edebildiğim bir paket kullanıyorum. SSH erişimi gibi
bir şansım yok. Bundan önce dosyaları sunucuya atmak için, filezilla kullanıyordum.
Filezilla ile upload yaparken, boyutu farklı ise veya kaynak daha yeniyse upload
et gibi bir seçeneği var. Bu az çok işimi görüyordu. Ancak bunun da kendine göre
bir takım sıkıntıları var. Bazen output klasörünü silip baştan oluşturma ihtiyacı
duyuyorum. Bu gibi durumlarda, çoğu dosyanın içereği aslında değişmemiş olsa bile,
tüm dosyaları baştan upload ediyor. Bir de bazen dosyaları yanlış yere atma gibi
bir problem yaşıyorum. Geçenlerde anasayfa'nın index sayfası üzerine, başka
bir klasörün index sayfasını atmışım mesela, biraz geç farkettim. Ayrıca, önceden
attığım ama sonradan sildiğim içeriğin takibi yapmam da mümkün olmuyordu bu şekilde. <!-- TEASER_END -->

Ben de şöyle birşey düşündüm, bütün dosyaların sha256 digest'lerini bir dosyada
tutuyorum. Yükleme yapacağım zaman, eski digest'leri yenileriyle karşılaştırıyorum.
Böylece, hangi dosyalar güncellenmiş, hangileri silinmiş, hangi dosyalar eklenmiş
görebiliyorum. Dosyaları yüklemek için de, başta Python'un ftplib modülünü denedim,
ama benim amaçlarım için fazla low-level bir modül olduğunu anladım. Daha sonra
[ftputil](https://pypi.python.org/pypi/ftputil/2.2.3) modülünü buldum. Bu Python'un
kütüphanesine göre daha high-level bir kütüphane. İşimi bir hayli rahatlattı. Kodları
da göstereyim:

	:::python
	import os
	import hashlib

	def create_hashes():
		hashes = dict()

		for root, _, files in os.walk("output"):
			for name in files:
				s = hashlib.sha256()
				filepath = os.path.join(root, name)

				# there is no with statament in py 2.5 ...
				f = open(filepath)
				try:
					s.update(f.read())
				finally:
					f.close()
				
				hashes[filepath] = s.hexdigest()

		return hashes

	def write_hashes(hashes):

		h = open("hashes","w")

		try:
			for filepath, hexdigest in hashes.items():
				h.write("%s\0%s\n" % (filepath, hexdigest))
		finally:
			h.close()

	def get_hashes():

		f = open("hashes")
		hashes = {}

		try:
			for line in f.readlines():
				k,v = line.strip().split('\0')
				hashes[k] = v
		finally:
			f.close()

		return hashes

Bu *hash_utils.py* dosyası. 3 tane fonksiyonu var. `create_hashes` o anki durumun hash'lerini oluşturuyor. `write_hashes` kendisine verilen hash'leri dosyaya yazıyor. `get_hashes` ise dosyadaki hashleri okuyup döndürüyor.
Bu da *deploy.py* dosyam:

	:::python
	import ftputil
	import hash_utils
	import os
	import posixpath

	oldhashes = hash_utils.get_hashes()
	newhashes = hash_utils.create_hashes()
	# print oldhashes
	# print newhashes

	new_files = set()
	dangling_files = set()

	for filepath, hexdigest in oldhashes.items():
		if filepath not in newhashes:
			dangling_files.add(filepath)
		elif newhashes[filepath] != oldhashes[filepath]:
			new_files.add(filepath)

	for filepath, _ in newhashes.items():

		if filepath not in oldhashes:
			new_files.add(filepath)

	host = ftputil.FTPHost('ftphost', 'ftpname', 'ftppassw')


	if not new_files:
		print "no new file"

	for f in new_files:
		parts = f.split(os.sep)

		# remove output
		parts = parts[1:]
		target = posixpath.join("/httpdocs",*parts)
		print "writing", target
		host.makedirs(posixpath.dirname(target))
		host.upload(f, target)
		

	if not dangling_files:
		print "no dangling files"

	for f in dangling_files:

		parts = f.split(os.sep)
		parts = parts[1:]
		target = posixpath.join("/httpdocs",*parts)
		print "removing file",target
		host.remove(target)
		


	hash_utils.write_hashes(newhashes)
	
Bu dosya, yeni ve güncellenmiş dosyaları sunucuma yazıyor, eğer silinmiş bir dosya varsa, sunucumdan siliyor.