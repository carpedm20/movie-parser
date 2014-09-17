#!/usr/bin/python2.7
import json
import os

def get_nxvxr_review_list(count=-1):
    print " * Start making reviews * "
    review_list = []

    if count != -1:
        files = [f for f in os.listdir('data')][:count+1]
    else:
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

            for movie in j:
                code = movie['code']
                reviews = movie['stars']

                for review in reviews:
                    review['code'] = code
                review_list.extend(reviews)
    bar.finish()
    print " * Finished * \n"

    return review_list
