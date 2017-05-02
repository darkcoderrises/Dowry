import os
import sys
import re

word_list = filter(bool, open('in3').read().split('\n'))
g = open(sys.argv[1]).read()

g.replace('\r', ' ').lower().replace('\n', ' ').replace('.',' ').replace('-', ' ').replace(',',' ').replace(":", " ").replace('`', ' ').replace('=',' ').replace('(', ' ').replace(')', ' ')

for i in range(10):
    g = g.replace(str(i), '')

for index, word in enumerate(word_list):
    val = sum(1 for _ in re.finditer(r'\b%s\b' %re.escape(' '+word+' '), g))
    if val > 0:
        print (word, val),

print
