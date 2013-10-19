<!--
.. date: 2013-02-01 22:12:00
.. slug: google-fusion-tables-twitter-follower-haritasi
.. title: İki adımda takipçi haritanızı oluşturun
.. description: Google Fusion Tables ve Twitter api kullanarak, google maps üzerinde sizi takip eden kişilerin bir haritasını oluşturmak mümkün. Ayrıca, göze güzel görünüyor.
-->

### 1 - Takipçilerin bilgilerini csv formatında kaydedin.

Öncelikle gerekli datayı twitter api'sinden almamız gerekiyor. Bunun için aşağıdaki kodları kullanacağız: <!-- TEASER_END -->
	
	:::python
	from urllib import urlencode
	from os import makedirs
	from os.path import dirname
	import json
	from datetime import datetime

	def lookup(screenname=False, user_id=False):
		if screenname is False and user_id is False:
			raise ValueError("Suppy either screenname or user_id")

		params = {}
		
		if screenname:
			params["screen_name"] = screenname
		else:
			params["user_id"] = user_id

		return call_twitter_api("users/lookup.json",params)

	def call_twitter_api(endpoint, params):
		"""
		Calls twitter api, and parses returned json, than returns.

		string, {"string": ?} -> ?
		"""

		query = "%s?%s" % (endpoint, urlencode(params,doseq=1))
		print query
		try:
			makedirs(dirname(query))
		except OSError:
			pass
			
		try:
			with open(query,"r") as dosya:
				raw_json = dosya.read()
				return json.loads(raw_json)
		except IOError:        
			url = "https://api.twitter.com/1/%s" % (query)
			conn = urlopen(url)
			raw_json = conn.read()

			conn.close()
			parsed  = json.loads(raw_json)
			if "error" not in parsed:  
				with open(query,"w") as dosya:
					dosya.write(raw_json)
			else:
				raise TwitterError(parsed["error"])
			
			return parsed


	def get_follower_ids(screenname=False, user_id=False):
		
		if screenname is False and user_id is False:
			raise ValueError("Suppy either screenname or user_id")

		params = {}
		
		if screenname:
			params["screen_name"] = screenname
		else:
			params["user_id"] = user_id

		return call_twitter_api("followers/ids.json",params)["ids"]

	def export_users(filename, user_ids):
		columnheaders = [
			"userid",
			"screenname",
			"fullname",
			"statusses",
			"friends",
			"followers",
			"favourites",
			"url",
			"lang",
			"location",
			"created",
			"timezone",
			]

		headerline = ",".join("\"%s\"" % i for i in columnheaders) + "\n"
		lineformat = ",".join(["\"%s\""] * len(columnheaders)) + "\n"

		print lineformat
		
		with open(filename, "w") as dosya:
			dosya.write(headerline)
			now = datetime.now()
			for id in user_ids:
				try:
					user = lookup(user_id=id)[0]
				except IOError:
					continue
				except KeyError:
					continue

				dosya.write( (lineformat % (
						user["id_str"],
						user["screen_name"],
						user["name"],
						user["statuses_count"],
						user["friends_count"],
						user["followers_count"],
						user["favourites_count"],
						user["url"],
						user["lang"],
						user["location"],
						user["created_at"],
						user["time_zone"],
						)).encode("utf-8"))

Önce [Twitter follower bilgilerini kaydeden kodlar]ı kaydedin, daha sonra
`export_users("myfollowers.csv",get_follower_ids("y_arabaci"))` şeklinde
bir fonksiyon çağrısı yapın (y\_arabaci yerine kendi kullanıcı adınızı
yazmayı unutmayın). Bu takipçileriniz hakkındaki bilgileri
*myfollowers.csv* ismindeki dosyaya kaydedecek. Twitter api saatte
150'den fazla fonksiyon çağrısı kabul etmiyor. O yüzden bir kısmını
indirdikten sonra biraz beklemeniz gerekebilir. Program indirdiği
verileri [keşliyor][]. O yüzden bir dahaki sefere sadece yeni kullanıcı
bilgilerini indirecek. <!-- TEASER_END -->

### 2 - Oluşturduğunuz tabloyu google fusion tables'a yükleyin.

[Google Fusion Tables import sayfası][] tıklayın ve oluşturduğunuz csv dosyasını yükleyin. Ayraç
(seperator) olarak virgül (comma), kodlama olarak utf-8 kullanın.
*location* sütununun bir yer ifade ettiği otomatik olarak algılayan
google, sizin için bu yerlerin haritada nereye düştüğünü bulup sizin
için işaretleyecek. "Map of location" isimli tabda haritanızı
görebilirsiniz. Bunun oluşması biraz süre alabilir. O aşağıdaki kırmızı
noktalara tıklayabiliyorsunuz.

<iframe frameborder="no" height="575" scrolling="no" src="https://www.google.com/fusiontables/embedviz?viz=MAP&amp;q=select+col9+from+1i_TtB5OlXUCLB2Iak7oNc8_FJ-Qe5UlU41h48qo&amp;h=false&amp;lat=35.15116205872891&amp;lng=30.962948649999912&amp;z=3&amp;t=1&amp;l=col9&amp;y=2&amp;tmplt=2" width="770"></iframe>

### Opsiyonel - Grafik falan da çizebilirsiniz.

<iframe frameborder="no" height="575" scrolling="no" src="https://www.google.com/fusiontables/embedviz?containerId=gviz_canvas&amp;q=select+col1%2C+col4%2C+col5+from+1i_TtB5OlXUCLB2Iak7oNc8_FJ-Qe5UlU41h48qo+order+by+col1+asc+limit+10&amp;viz=GVIZ&amp;t=COLUMN&amp;uiversion=2&amp;gco_forceIFrame=true&amp;gco_hasLabelsColumn=true&amp;gco_type=columns&amp;width=770&amp;height=575" width="770"></iframe>

### Özetle

Google fusion tables olayının ilk fanboylarından oldum galiba.

  [Twitter follower bilgilerini kaydeden kodlar]: https://gist.github.com/raw/4693569/0387520d2b391c971b2a272a47bcc65be7138da9/twit.py
  [keşliyor]: http://www.idefix.com/kitap/django-mustafa-baser/tanim.asp?sid=OQFCL6MHX32LQUJYWSSU#urunelestirileri
  [Google Fusion Tables import sayfası]: https://www.google.com/fusiontables/DataSource?dsrcid=implicit&redirectPath=data