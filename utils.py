from glob import glob
import os
import re

tags = re.compile(r"</?[^>]+/?>")
date = re.compile("\d{4}-\d{2}-\d{2}-")
header_line = re.compile("\.\. (?P<key>\w+): (?P<value>.+)")

def remove_multi_blank_lines(string):
	lines = string.splitlines()
	output = []
	add_blank_line = True
	for line in lines:
		if line == "":
			if add_blank_line:
				output.append("")
				add_blank_line = False
		else:
			output.append(line)
			add_blank_line = True
	
	return "\n".join(output)

def split_headers(string):
	"""
	Also removes multiple blank lines
	"""
	lines = string.splitlines()
	end_headers = lines.index("")
	return ("\n".join(lines[:end_headers]), "\n".join(lines[end_headers+1:]))
	
def parse_headers(string):
	lines = string.splitlines()
	hdrs = {}
	while True:
		line = lines.pop(0)
		if line == "<!--":
			continue
		if line == "-->":
			break
		m = header_line.match(line)
		if not m:
			continue
			
		hdrs[m.group("key")] = m.group("value")
	return hdrs

def parse_old_headers(string):
	lines = string.splitlines()
	hdrs = {}
	for line in lines:
		parts = line.split(":")
		hdrs[parts[0].lower()] = ":".join(parts[1:])
	return hdrs
def compile_new_headers(hdrs):
	new_hdrs = ["<!--"]
	for k,v in hdrs.items():
		if k in ["author","category","tags"]:
			continue
		if k == "slug":
			v = date.sub("",v)
		new_hdrs.append(".. %s: %s" % (k,v))
	new_hdrs.append("-->")
	
	return "\n".join(new_hdrs)
def convert_code(string):
	lines = string.splitlines()
	new_lines = []
	code_block = False
	for line in lines:
		if code_block:
			if line.startswith("~~~~"):
				code_block = False
			else:
				new_lines.append("    %s" % line)
		elif line.startswith("~~~~"):
			code_block = True
			new_lines.append("    :::python")
		else:
			new_lines.append(line)
	return "\n".join(new_lines)

"""	
def convert()
	for f_name in glob("*.md"):
		with open(f_name,"r") as f:
			# output.write("\n==== FILENAME ==== \n%s" % f_name)
			# raw = f.read()
			# output.write("\n==== RAW==== \n%s" % raw)
			headers, content = split_headers(f.read())
			# output.write("\n==== SPLIT==== \n%s" % content)
			header_dict = parse_headers(headers)
			print header_dict
			new_headers = compile_new_headers(header_dict)
			content = tags.sub("",content)
			# output.write("\n==== REMOVE P ==== \n%s" % content)
			content = remove_multi_blank_lines(content)
			# output.write("\==== REMOVE MULTI BLANK ==== \n%s" % content)
			content = convert_code(content)
			dirname = "%s/%s" % ("converted", header_dict.get("category"))
			if not os.path.exists(dirname):
				os.makedirs(dirname)
			with open("%s/%s" % (dirname, f_name),"w") as output:
				output.write("%s\n\n%s" % (new_headers, content))
"""