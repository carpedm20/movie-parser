#!/usr/bin/python2.7
import json
import sys, os
import pprint
from collections import Counter

from time import sleep
review_list = []

files = [f for f in os.listdir('data')]

import progressbar
bar = progressbar.ProgressBar(maxval=len(files), \
            widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

for i, f_name in enumerate(files):
    bar.update(i+1)
    if 'vw' not in f_name and 'json' in f_name:
    #if 'unpopular' not in f_name and 'json' in f_name:
        try:
            j=json.loads(open('./data/'+f_name,'r').read())
        except:
            continue

        review_list.extend(j)
bar.finish()

print "# of review : %s" % "{:,}".format(len(review_list))
print "# of unique review : %s" % "{:,}".format(len(list(set([review['text'] for review in review_list]))))

print "Top Movies with the most reviews"
c = Counter([review['code'] for review in review_list])
pprint.pprint(c.most_common(20))

if False:
    user_list = [review['encrypted_id'] for review in review_list]
    print "# of reviewer : %s" % len(set(user_list))

    c = Counter(user_list)
    pprint.pprint(c.most_common(20))

word_list = [review['text'].split() for review in review_list]
word_list = [word for words in word_list for word in words]

c = Counter(word_list)
class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, _object, context, maxlevels, level):
        if isinstance(_object, unicode):
            return "'%s'" % _object.encode('utf8'), True, False
        elif isinstance(_object, str):
            _object = unicode(_object,'utf8')
            return "'%s'" % _object.encode('utf8'), True, False
        return pprint.PrettyPrinter.format(self, _object, context, maxlevels, level)

print "# of unique words : %s" % "{:,}".format(len(c))
MyPrettyPrinter().pprint(c.most_common(20))
