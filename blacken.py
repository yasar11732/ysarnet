from glob import glob
from os import walk, remove
from os.path import join

with open('template.html') as f:
    template = f.read()

for root, _, files in walk("output"):
    for f in files:
        if f.endswith(".gz"):
            remove(join(root, f))
