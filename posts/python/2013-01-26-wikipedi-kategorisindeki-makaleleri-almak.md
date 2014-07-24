<!--
.. date: 2013-01-26 03:56:41
.. slug: wikipedia-api-kategori-export
.. title: Wikipedi kategorisindeki makaleleri almak
.. description: Wikipedia'nın bir apisi oldğuğunu biliyor muydunuz? Wikipedia apisi ile yapılabilecek şeylerden bir tanesi, bir kategorideki bütün makaleleri indirmek.
-->


Wikipedia'nın bir apisi olduğunu biliyor muydunuz? Wikipedia apisi ile yapılabilecek şeylerden bir tanesi, bir kategorideki bütün makaleleri indirmek. <!-- TEASER_END -->

Aşağıda bir wikipedi kategorisindeki sayfaları indiren programı
bulabilirsiniz.

    :::python
    # -*- coding: utf-8 -*-
    import os
    import errno
    from urllib import quote
    import requests
    import json
    from sys import version
    
    # Fill in please
    your_name = "Yaşar Arabacı"
    email = "yasar11732@gmail.com"
    
    useragent = "Export a category -- Python %s, %s %s" % (version, your_name, email)
    
    category = "Kategori:Matematik"
    dirname = quote(category)
    
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
            print page["title"],
            filename = "%s.txt" % quote(page["title"].encode("utf-8"))
            print filename
            with open(os.path.join(dirname,filename), "w") as f:
                f.write(page["revisions"][0]["*"].encode("utf-8"))
        
    def get(action,**kwargs):
        endpoint = "http://tr.wikipedia.org/w/api.php"
        
        kwargs.update({"action":action,"format":"json"})
    
        headers = {"User-Agent":useragent}
        r = requests.get(endpoint, headers=headers, params=kwargs)
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
        }
    
    a = get("query",**params)
    
    process_pages(a["query"]["pages"])
    
    while "query-continue" in a:
        nparams = dict(params)
        nparams.update(a["query-continue"]["categorymembers"])
        a = get("query",**nparams)
        process_pages(a["query"]["pages"])
    
    print "done"

Bu arada wikipedi apisi derya denizmiş, onu farkettim
bugün :) 