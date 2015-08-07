#! /usr/bin/env python
import numpy as np
import os, sys

# usage: score to label 
# chose label-design policy

list_name = sys.argv[1]
with open(list_name) as f:
    content = f.readlines()
file_name = list_name.split('.')[0] + '_labeled.lst'
fd = open(file_name, 'w+')

def binary_label(s):
    score = float(s)
    if score >= 0.99:
        return '1'
    else:
        return '0'

def fiveClass_label(s):
    score = float(s)
    if score >= .995:
        return '0'
    elif score >= .99:
        return '1'
    elif score >= .95:
        return '2'
    elif score >= .9:
        return '3'
    elif score < .9:
        return '4'

def fifty_label(s):
    score = float(s)
    if score >= .95:
        return str(int((1-score) * 1000))
    elif score >= .9:
        return '51'
    elif score >= .8:
        return '52'
    else :
        return '53'
    
for line in content: 
    elem = line.split(' ')
    score = elem[2].split('/')[0]
    # change label conversion policy
    label = fifty_label(score)
    new_line = elem[0] + ' '+ elem[1] + ' ' + label
    fd.write(new_line+'\n')
fd.close()
