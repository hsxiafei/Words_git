#coding=utf-8
import re
with open('from.txt') as f:
     result = re.findall(r'\b\w+\b', ''.join(f.readlines()))
     result.sort(key=lambda x: x[0])
with open('to.txt', 'w') as f:
    for i in result:
        f.write('%s\n' %i)
