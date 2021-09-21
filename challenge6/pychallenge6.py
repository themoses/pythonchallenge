# zip in comment means to change html to zip (this stuff is hard)

import requests
from zipfile import ZipFile

zipurl = 'http://www.pythonchallenge.com/pc/def/channel.zip'

response = requests.get(zipurl)

# download the zip file
with open('channel.zip', 'wb') as dl:
  dl.write(response.content)

# extract the zip file
with ZipFile('channel.zip', 'r') as archive:
  archive.extractall()

# readme.txt:
# welcome to my zipped list.
#
# hint1: start from 90052
# hint2: answer is inside the zip

# cat 90052.txt -> Next nothing is 94191


