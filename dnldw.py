#!/usr/bin/env python3

import urllib.request
import sys
import math
import datetime

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

if len(sys.argv) < 2:
    print("Usage: dnldw.py <url> [filename]\nFile Name is Opcional")
    sys.exit(1)

url = sys.argv[1]

file_name = url.split('/')[-1]

if len(sys.argv) > 2:
    url = sys.argv[1]
    file_name = sys.argv[2]

initial_time = datetime.datetime.now()
u = urllib.request.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(u.length)
file_size_mb = convert_size(file_size)
print('\033[1m\033[37m')
title = '''
    .___     .__       .___        
  __| _/____ |  |    __| _/_  _  __
 / __ |/    \|  |   / __ |\ \/ \/ /
/ /_/ |   |  \  |__/ /_/ | \     / 
\____ |___|  /____/\____ |  \/\_/  
     \/    \/           \/         
'''

print(title)
print("\n\033[1;34mDownloading: %s Size: %s\n" % (file_name, file_size_mb))

file_size_dl = 0
block_sz = 8192
def progress_bar(current, total, dnldw_bytes, bar_length=15):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '█' + '█'
    padding = int(bar_length - len(arrow)) * '░'

    ending = '\n' if current == total else '\r'

    print(f'- Progress: [{arrow}{padding}] {int(fraction*100)}% | Status: {u.getcode()} | Downloading: {convert_size(dnldw_bytes)}  ', end=ending)

while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    progress_bar(file_size_dl, file_size, file_size_dl)

f.close()
print("\n\n\033[1;32mDownload complete!\033[0m")
print("\n\n\033[1;92mDownloaded: %s Size: %s\n" % (file_name, convert_size(file_size)))
final_time = datetime.datetime.now()
total_time = final_time - initial_time
total_time = str(total_time).split('.')[0]
print(f"\033[1;34mTime: {total_time}\n")
res = input('Do you want to see the details? (y/n): ')
if res == 'y':
    print('----------------------------------------')
    print(u.info(), end='')
else:
    print()
    pass
sys.exit(0)