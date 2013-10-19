# -*- coding: utf-8 -*-
from conf import POSTS
import os
from glob import iglob
from utils import parse_headers
from string import Template
from datetime import datetime

post_template = Template("""<!--
.. title: $title
.. date: $date
.. slug: index
-->

$content
""")

target = "subindex"

time_string = datetime.now().strftime("%Y-%m-%d %H:%M")
for wildcard, _, _ in POSTS:
	dirname = os.path.dirname(wildcard)
	for dirpath, _, _ in os.walk(dirname):
		if dirpath == "yazilar":
			continue
		hdrs = []
		dir_glob = os.path.join(dirpath, os.path.basename(wildcard))
		for file in iglob(dir_glob):
			with open(file, "r") as f:
				hdrs.append(parse_headers(f.read()))
			
		tempdir = {
			"title": "Bu kategorideki yazılar",
			"date": time_string,
			"content": "\n".join([" * [%s - %s](%s.html)" % (x['date'], x["title"], x["slug"]) for x in sorted(hdrs, key=lambda x: x['date'])])
		}

		target_file = os.path.join(target, dirpath[8:], "index.md")
		if not os.path.isdir(os.path.dirname(target_file)):
			os.makedirs(os.path.dirname(target_file))
		with open(target_file,"w") as output:
			output.write(post_template.substitute(tempdir))