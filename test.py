import re

i = re.compile(r'.{,}?5')

s = i.findall('1234555511231335')

for j in range(len(s)):
    print (s[j])