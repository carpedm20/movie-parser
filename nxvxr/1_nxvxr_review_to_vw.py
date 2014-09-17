#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
import re
import sys
import json
import codecs

from utils import get_nxvxr_review_list
reviews = get_nxvxr_review_list()

def clean(s):
    s = s.encode('utf-8')
    try:
        return " ".join(re.findall(r'[가-힣\w]+', s, flags=re.UNICODE|re.LOCALE)).decode('utf-8').lower()
    except:
        #print "Error : %s" % s
        return False
    #return " ".join(s.split())

import progressbar
bar = progressbar.ProgressBar(maxval=len(reviews), \
            widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

output = "train.vw"

print " * Start creating %s" % output
with codecs.open(output, 'w', encoding='utf-8') as outfile:
    for idx, review in enumerate(reviews):
        bar.update(idx+1)
        code = review['code']
        point = review['point']/2 or 1
        text = clean(review['text'])
        if not text:
            continue
        encrypted_id = review['encrypted_id']

        outfile.write("%s '%s |f %s |a word_count:%s\n"
                % (point, code, text, len(text)))

bar.finish()
print " * Finished * \n"
