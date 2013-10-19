from conf import POSTS
import os
from glob import iglob
from utils import parse_headers

for wildcard, _, _ in POSTS:
	dirname = os.path.dirname(wildcard)
	for dirpath, _, _ in os.walk(dirname):
		dir_glob = os.path.join(dirpath, os.path.basename(wildcard))
		for file in iglob(dir_glob):
			with open(file, "r") as f:
				hdrs = parse_headers(f.read())
				if not hdrs.get("description"):
					print file