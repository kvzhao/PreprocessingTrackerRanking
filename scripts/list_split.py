#! /usr/bin/env python
import sys
from random import shuffle

list_file = sys.argv[1]
with open(list_file) as f:
    content = f.readlines()
    
shuffle(content)
total_num = len(content)
train_list_name = list_file.split('.')[0] + '_train.txt'
test_list_name = list_file.split('.')[0] + '_test.txt'
test_num = total_num / 4
train_num = total_num - test_num
print test_num, train_num
trainlist = open(train_list_name, 'w+')
testlist = open(test_list_name, 'w+')

train = content[:train_num]
test = content[train_num:]

for item in train:
    trainlist.write('%s' % item)
for item in test:
    testlist.write('%s' % item)

print len(train), len(test)
trainlist.close()
testlist.close()
