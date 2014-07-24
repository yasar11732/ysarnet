import ftputil
import hash_utils
import os
import posixpath

oldhashes = hash_utils.get_hashes()
newhashes = hash_utils.create_hashes()
# print oldhashes
# print newhashes

new_files = set()
dangling_files = set()

for filepath, hexdigest in oldhashes.items():
    if filepath not in newhashes:
        dangling_files.add(filepath)
    elif newhashes[filepath] != oldhashes[filepath]:
        new_files.add(filepath)

for filepath, _ in newhashes.items():

    if filepath not in oldhashes:
        new_files.add(filepath)

with open("ftp_credentials.txt","r") as ftp_login:
	host = ftputil.FTPHost(*ftp_login.read().splitlines())

if not new_files:
    print("no new file")

for f in new_files:
    parts = f.split(os.sep)

    # remove output
    parts = parts[1:]
    target = posixpath.join("/httpdocs",*parts)
    print("writing", target)
    host.makedirs(posixpath.dirname(target))
    host.upload(f, target)
    

if not dangling_files:
    print("no dangling files")

for f in dangling_files:

    parts = f.split(os.sep)
    parts = parts[1:]
    target = posixpath.join("/httpdocs",*parts)
    print("removing file",target)
    try:
        host.remove(target)
    except ftputil.ftp_error.PermanentError as err:
        print(err)
        continue

hash_utils.write_hashes(newhashes)

