import re

long_word = input()

ls1 = re.findall("fish", long_word, flags=re.IGNORECASE)
ls2 = re.findall("sun", long_word, flags=re.IGNORECASE)
ls3 = re.findall("water", long_word, flags=re.IGNORECASE)
ls4 = re.findall("sand", long_word, flags=re.IGNORECASE)
ls = ls1 + ls2 + ls3 + ls4

if not ls:
    print(0)
else:
    print(len(ls))