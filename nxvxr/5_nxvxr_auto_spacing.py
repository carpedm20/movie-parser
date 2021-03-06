#!/usr/bin/python
#-*- coding: utf-8 -*-
import json
from utils import get_nxvxr_review_list, auto_spacing

reviews = get_nxvxr_review_list(20)
texts = [review['text'] for review in reviews]

START_IDX = 0
VERBOSE = False
TEST = True

output = 'auto_spaced_review_'+str(START_IDX)+'-%s.json'

texts = texts[START_IDX:]

start_idx = 0
data = ""
next_text = ""

import progressbar
bar = progressbar.ProgressBar(maxval=len(texts), \
                widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

is_saved = False
try:
    for idx, text in enumerate(texts):
        bar.update(idx+1)

        data += text+'\r\n'
        if len(data) < 1000000:
            continue

        new_text = auto_spacing(data).split('<br>')
        if len(new_text) == 1:
            new_text = new_text[0].split('<br/>')

        for i, review in enumerate(reviews[start_idx:idx+1]):
            try:
                if reviews[start_idx+i]['text'] != new_text[i]:
                    reviews[start_idx+i]['text'] = new_text[i]
            except Exception as e:
                if VERBOSE:
                    print "=== 1 ==="
                    print e
                continue

        data = ""
        start_idx = idx+1

        if TEST:
            break
except Exception as e:
    if VERBOSE:
        print "=== 2 ==="
        print e

    is_saved = True
    with open(output % idx,'w') as f:
        json.dump(reviews, f)

bar.finish()

if not is_saved:
    with open(output % idx,'w') as f:
        json.dump(reviews, f)
