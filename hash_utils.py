import os
import hashlib


def create_hashes():
    hashes = dict()

    for root, _, files in os.walk("output"):
        for name in files:
            s = hashlib.sha256()
            filepath = os.path.join(root, name)

            # there is no with statament in py 2.5 ...
            f = open(filepath)
            try:
                s.update(f.read())
            finally:
                f.close()
            
            hashes[filepath] = s.hexdigest()

    return hashes

def write_hashes(hashes):

    h = open("hashes","w")
    data = "\n".join(("%s\0%s" % (filepath, hexdigest) for filepath, hexdigest in hashes.items()))
    try:
        h.write(data)
    finally:
        h.close()

def get_hashes():
    
    strp = str.strip
    splt = str.split

    def dictmaker(acc, new):
        k,v = splt(strp(new),'\0')
        acc[k] = v
        return acc

    with open("hashes") as f:
        return reduce(dictmaker, f.readlines(), {})
