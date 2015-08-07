#! /usr/bin/env python
import numpy as np
import os, sys
from collections import namedtuple

video_list_name = sys.argv[1]
tracker_result_path = sys.argv[2]
score_list_name = sys.argv[3]

# collections of named tuple
score_statistic = namedtuple('score', 'path videonum mean std max min')
# a Tracker dict
T = {}
TR = {} # tracker results dictionary
attr_set = []
results = []
total_scores = []

# traverse the tracker's result and dict all score values
for root, dirs, files in os.walk(tracker_result_path):
    for f in files:
        # modify, if we want to get different type of scores
        if f.endswith('_all.txt'):
            continue
        if f.endswith('txt'):
            type_ = f.split('-')[1].rstrip('.txt').split('_')
            video_name = f.split('-')[1].rstrip('.txt')
            attr = type_[0]
            attr_set.append(attr)
            video_num = type_[1]
            score_path = '/'.join([root, f])
            score = np.genfromtxt(score_path, dtype=[('index', int), ('score', float)], delimiter=',')
            if not score['score'].size:
                print score_path, 'is empty file'
                continue
            avg_ = np.mean(score['score'])
            std_ = np.std(score['score'])
            max_= np.max(score['score'])
            min_= np.min(score['score'])
            if score['score'].size >1:
                total_scores.extend(score['score'].tolist())
            else:
                total_scores.append(score['score'].tolist())
            # set the dict which key=attribute, value is a tuple list
            T.setdefault(attr, []).append(score_statistic(score_path, video_num, avg_, std_, max_, min_))
            if score['score'].size >1:
                for s in score:
                    # IMPORTANT: 5 index shifting in DATASET!
                    clip_num = '{0:08d}'.format(s['index'] -5)
                    score_value = s['score']
                    video_clip = video_name + '_' + clip_num
                    TR[video_clip] = score_value
            else:
                    clip_num = '{0:08d}'.format(score['index'] -5)
                    score_value = score['score']
                    video_clip = video_name + '_' + clip_num
                    TR[video_clip] = score_value
attr_set = set(attr_set)
# travel through all attribute

# create the dict of score
output_file = open(score_list_name, 'w+')
with open(video_list_name) as f:
    file_content = f.readlines()
for line in file_content:
    line_list = line.split(' ')
    path = line_list[0]
    prefix = path.split('/')[-2].split('-')[1]
    clip_num = line_list[1].rstrip('\n')
    key = prefix + '_' + clip_num
    try:
        output_score = TR[key]
    except KeyError:
        print key, 'missed video clip'
        output_score = -1.0
        pass
    new_line = ' '.join([path, clip_num, str(output_score)])
    output_file.write(new_line +'\n')
output_file.close()
