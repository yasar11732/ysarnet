import os
import hashlib


def create_hashes():
    hashes = dict()

    for root, _, files in os.walk("output"):
        for name in files:
            s = hashlib.sha256()
            filepath = os.path.join(root, name)
            with open(filepath, 'rb') as f:
                s.update(f.read())

            hashes[filepath] = s.hexdigest()

    return hashes

def write_hashes(hashes):

    with open("hashes","w", encoding="utf-8") as h:
        data = "\n".join(("%s %s" % (filepath, hexdigest) for filepath, hexdigest in hashes.items()))
        h.write(data)

def get_hashes():
    try:
        with open("hashes", encoding="utf-8") as f:
            hashes = {}
            for line in f.readlines():
                k,v = line.strip().split(' ')
                hashes[k] = v   
            return hashes

    except FileNotFoundError:
        return {}
