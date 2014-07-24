<!--
.. date: 2013-01-26 13:20:53
.. title: Wikipedi kategorisindeki makaleleri almak - HTML
.. slug: wikipedia-api-kategori-export-html
.. description: Dünkü yazıda, bir wikipedia kategorisindeki makaleleri wikitex formatında almayı göstermiştim. Bu yazıda ise, HTML olarak alacağız.
-->

Dünkü yazıda, bir wikipedia kategorisindeki makaleleri wikitex formatında almayı göstermiştim. Bu yazıda ise, HTML olarak alacağız.  <!-- TEASER_END -->

	:::python
	# -*- coding: utf-8 -*-
	import os
	import errno
	from urllib import quote
	import requests
	import json
	from HTMLParser import HTMLParser
	from sys import version
	 
	# Fill in please
	your_name = "Yaşar Arabacı"
	email = "yasar11732@gmail.com"
	 
	useragent = "Export a category -- Python %s, %s %s" % (version, your_name, email)
	 
	 
	category = "Kategori:Fizik"
	dirname = quote(category)
	 
	h = HTMLParser()
	 
	template = "{title}{content}"
	 
	# Create target directory
	try:
		os.makedirs(quote(category))
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
	 
	class WikiError(Exception):
		pass
	 
	def process_pages(pages):
		for i, page in pages.items():
			print page["title"]
			filename = "%s.html" % quote(page["title"].encode("utf-8"))
			html = h.unescape(page["revisions"][0]["*"])
			rendered = template.format(title=page["title"].encode("utf-8"), content=html.encode("utf-8"))
			with open(os.path.join(dirname,filename), "w") as f:
				f.write(rendered)
		 
	def get(action,**kwargs):
		endpoint = "http://tr.wikipedia.org/w/api.php"
		 
		kwargs.update({"action":action,"format":"json"})
	 
		headers = {"User-Agent":useragent}
		r = requests.get(endpoint, headers=headers, params=kwargs)
		print r.url
		js = json.loads(r.text)
		if "error" in js:
			raise WikiError(js["error"]["info"])
		else:
			return js
	 
	# Params that gives you content off all pages in a given category
	params = {
		"generator" : "categorymembers",
		"gcmtitle" : category,
		"gcmtype": "page",
		"prop" : "revisions",
		"rvprop" : "content",
		"rvparse" : 1
		}
	 
	 
	a = get("query",**params)
	 
	process_pages(a["query"]["pages"])
	 
	while "query-continue" in a:
		nparams = dict(params)
		nparams.update(a["query-continue"]["categorymembers"])
		a = get("query",**nparams)
		process_pages(a["query"]["pages"])

	print "done"