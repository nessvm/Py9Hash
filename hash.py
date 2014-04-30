#! usr/bin/python

import sys
from Crypto.Hash import SHA

"""This program reads the file found in the path given as a command line
    argument and applies the SHA-1 algorithm on the contents and then
    writes the digest on a new file called hash.txt"""


def hash_file(path):
    in_stream = open(path, 'r')
    contents = in_stream.read()
    sha_obj = SHA.new()
    sha_obj.update(bytes(contents))

    return sha_obj.digest()


def main():
    digest = hash_file(sys.argv[1])
    out_stream = open('hash.txt', 'w')
    out_stream.write(digest)


if __name__ == '__main__':
    main()
