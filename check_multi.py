from conf import POSTS
from glob import iglob
import os

basedir = path.abspath(".")

islenecek_glob = path.join(basedir, "islenecekler","*.md")


islenecekler = set([os.path.basename(x) for x in iglob(islenecek_glob)])

print "\n==== ISLENECEK ===\n%s" % islenecekler

yazilar = set()

for wildcard, _, _ in POSTS:
	dirname = os.path.dirname(wildcard)
	for dirpath, _, _ in os.walk(dirname):
		dir_glob = os.path.join(dirpath, os.path.basename(wildcard))
		for file in iglob(dir_glob):
			yazilar.add(os.path.basename(file))

print "\n==== yazilar ===\n%s" % yazilar	
for file in yazilar.intersection(islenecekler):
	print file