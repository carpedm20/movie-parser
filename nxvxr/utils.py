#!/usr/bin/python2.7
import json
import os
import requests
from bs4 import BeautifulSoup

def auto_spacing(text):
    url = "http://s.lab.naver.com/autospacing/"

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36 Paros/3.2.13', 'Origin': 'http://s.lab.naver.com', 'Referer': 'http://s.lab.naver.com/autospacing/?'}

    payloads = {'query': text, 'result_type': 'paragraph', 'x': '35', 'y': '9'}

    r = requests.post(url, headers=headers, data=payloads)

    soup = BeautifulSoup(r.text)
    div = soup.find('div', {'class':'wrap_spacing2'}).findChild()

    return str(div).replace('<p>\n','').replace('<strong>','').replace('</strong>','')

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

            review_list.extend(j)
    bar.finish()
    print " * Finished * \n"

    return review_list

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

            review_list.extend(j)
    bar.finish()
    print " * Finished * \n"

    return review_list
