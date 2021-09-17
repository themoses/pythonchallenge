''' K -> M means shift alphabet to the right by two. This script does not shift x and z to the beginning but it's good enough '''

encryptedString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for char in encryptedString:
    if (char == ' '):
        print(' ', end='')
    else:
        print(chr(ord(char) + 2), end='')

print('#############')

# URL is map, so applying this to URL gives us ocr

for char in 'map':
    print(chr(ord(char) + 2), end='')