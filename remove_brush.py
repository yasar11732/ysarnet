import os
import re
from glob import iglob

br = re.compile("\{\.brush\s+\.py\}",re.MULTILINE)
for file in iglob("islenecekler/*.md"):
	print file
	with open(file) as f, open(os.path.join("convert",os.path.basename(file)),"w") as output:
		output.write(br.sub("",f.read()))