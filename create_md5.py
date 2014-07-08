import os
import hashlib

def create_hashes():
    hashes = set()

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
            
            hashes.add((filepath, s.hexdigest()))

    return hashes

def write_hashes(hashes):

    h = open("hashes","w")

    try:
        for filepath, hexdigest in hashes:
            h.write("%s\0%s\n" % (filepath, hexdigest))
    finally:
        h.close()
