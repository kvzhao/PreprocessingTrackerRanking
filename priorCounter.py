#! /usr/bin/env python
import sys
import math

list_file = sys.argv[1]
with open(list_file) as f:
    content = f.readlines()

label_list=[]
for c in content:
    #label = int(c.split(' ')[-1])
    label = round((float(c.split(' ')[-1])), 3) # round score to 3 digits
    label_list.append(label)
classet = set(label_list)
classet = sorted(classet)
total_num = len(label_list)
for c in classet:
    print 'The class #', c, 'contains', label_list.count(c), '/', total_num, '=', float(label_list.count(c))/total_num
