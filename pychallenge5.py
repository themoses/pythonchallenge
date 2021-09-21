# peak hell? pronounce it? -> peakhill -> pickle is python object serialization, had to google that...

import pickle
import requests

pickleurl = 'http://www.pythonchallenge.com/pc/def/banner.p'

# download the file
r = requests.get(pickleurl)

with open('banner.p', 'wb') as pic:
    pic.write(r.content)

# unpickle the file
with open('banner.p', 'rb') as f:
    mysterydata = pickle.load(f)
    #print(mysterydata) # tuples with a symbol and a number in array-> create a string with each array entry as a row and each symbol number times

for row in mysterydata:
    for line in row:
        print(line[1]*line[0], end="")
    print('\n')
# -> spells out "channel" in ascii art -> channel.html