#!/usr/bin/env python3

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: dnldw.py <url>")
    sys.exit(1)

url = sys.argv[1]

file_name = url.split('/')[-1]
u = urllib.request.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(u.length)
print("Downloading: %s Bytes: %s" % (file_name, file_size))

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    sys.stdout.flush()
    sys.stdout.write(status)

f.close()