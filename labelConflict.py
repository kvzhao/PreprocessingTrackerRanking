#! /usr/bin/env python
import numpy as np
import os, sys
import matplotlib.pyplot as plt
from collections import namedtuple
from operator import itemgetter

# source list (video list), tracker list #1 and #2 ..
try:
    video_list_name = sys.argv[1]
except:
    video_list_name = 'static_txt/video_list.lst'
try:
    str_path = sys.argv[2]
except:
    str_path = 'analysis/str_all_labeled.lst'
try:
    tld_path = sys.argv[3]
except:
    tld_path = 'analysis/tld_all_labeled.lst'
try:
    csk_path = sys.argv[4]
except:
    csk_path = 'analysis/csk_all_labeled.lst'

# a Tracker dict
T = {}
results = []
total_scores = []

def readTrackerResult(path):
    T = {}
    with open(path) as f:
        content = f.readlines()
    for line in content:
        line_list = line.split(' ')
        path = line_list[0]
        prefix = path.split('/')[-2].split('-')[1]
        clip_num = line_list[1].rstrip('\n')
        label = line_list[2].rstrip('\n')
        key = prefix + '_' + clip_num
        T[key] = label
    return T

# create the dict of score
str_dict = readTrackerResult(str_path)
tld_dict = readTrackerResult(tld_path)
csk_dict = readTrackerResult(csk_path)

# Read from video list
video_list = []
with open(video_list_name) as f:
    file_content = f.readlines()
for line in file_content:
    line_list = line.split(' ')
    path = line_list[0]
    prefix = path.split('/')[-2].split('-')[1]
    clip_num = line_list[1].rstrip('\n')
    #lb = int(line_list[1].rstrip('\n')) -5
    #clip_num = '{0:08d}'.format(lb)
    key = prefix + '_' + clip_num
    video_list.append(key)
video_list.sort()

# compare and print out results
