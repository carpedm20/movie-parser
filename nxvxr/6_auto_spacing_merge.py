#!/usr/bin/python2.7
import json
import os

print " * Start merging auto_spaced reviews * "

files = [f for f in os.listdir('.')]

review_fs = []

for f_name in files:
    if 'auto_spaced_review' in f_name:
        review_fs.append(f_name)

review_fs.sort()

reviews = []
for review_f in review_fs:
    print "READING %s" % review_f
    with open(review_f) as f:
        reviews.extend(json.loads(f.read()))

#output = 'merged_auto_spaced_n_review.json'
#with open(output,'w') as f:
#    json.dump(reviews, f)

