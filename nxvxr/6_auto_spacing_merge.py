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

for f in review_fs:

