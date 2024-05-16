import sys
import os
from os import path
import hashlib

def main(directory):
    print("REMOVING DUPLICATES >>>>>>> " + directory)
    hashes = set()

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        digest = hashlib.sha1(open(path,'rb').read()).digest()
        if digest not in hashes:
            hashes.add(digest)
        else:
            os.remove(path)

main(sys.argv[1])