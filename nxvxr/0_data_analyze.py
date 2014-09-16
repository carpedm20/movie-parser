#!/usr/bin/python2.7
import json
import sys, os
import pprint
from collections import Counter

from utils import get_review_list

VERBOSE = False
COUNT = 3

review_list = get_review_list(COUNT)

c = Counter([review['code'] for review in review_list])
print "# of movies with reviews : %s" % "{:,}".format(len(c))
print "# of reviews : %s" % "{:,}".format(len(review_list))
print "# of unique reviews : %s" % "{:,}".format(len(list(set([review['text'] for review in review_list]))))

if VERBOSE:
    print "Top Movies with the most reviews"
    pprint.pprint(c.most_common(20))

if VERBOSE:
    user_list = [review['encrypted_id'] for review in review_list]
    print "# of reviewer : %s" % len(set(user_list))

    c = Counter(user_list)
    pprint.pprint(c.most_common(20))

if VERBOSE:
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
