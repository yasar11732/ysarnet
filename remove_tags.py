from conf import POSTS
import os
from glob import iglob
from utils import parse_headers, split_headers, compile_new_headers
from shutil import copy

for wildcard, _, _ in POSTS:
	dirname = os.path.dirname(wildcard)
	for dirpath, _, _ in os.walk(dirname):
		dir_glob = os.path.join(dirpath, os.path.basename(wildcard))
		for file in iglob(dir_glob):
			with open(file, "r") as f:
				headers, content = split_headers(f.read())
			header_dict = parse_headers(headers)
			if "tags" in header_dict:
				del header_dict["tags"]
				copy(file,"%s.bak" % file)
				new_headers = compile_new_headers(header_dict)
				with open(file,"w") as f:
					f.write("%s\n\n%s" % (new_headers, content))
					print("Rewrote %s\n" % file)
					