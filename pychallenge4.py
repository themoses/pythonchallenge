### linkedlist.php?nothing=12345 and then linkedlist.php?nothing=44827 --> parse this and do it 400 times with urllib

import urllib.request
import re

requesturl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
numberList = [12345]

def getNothings(number):

    responseText = urllib.request.urlopen(requesturl + str(number)).read().decode()

    numbers = re.findall("([0-9]+)$", responseText)
    return int(numbers[0])

for i in range(1):
    print(numberList[i])
    numberList.append(getNothings(numberList[-1]))
    

print(numberList) # last number is 16044 and says "Yes, divide by two and keep going"
print(16044 / 2) # 8022

numberList = [8022]

for i in range(400):
    print(numberList[i])
    numberList.append(getNothings(numberList[-1])) # 66831 gives us peak.html