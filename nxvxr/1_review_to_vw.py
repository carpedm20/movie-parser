#!/usr/bin/python
import sys
import json

if len(sys.argv) < 2:
    print "Error: file name needed"
    sys.exit(1)

with open(sys.argv[1]) as f:
    j = json.loads(f.read())

output = "vw_" + sys.argv[1]
print output

def clean(s):
    #return " ".join(re.findall(r'\w+', s, flags=re.UNICODE|re.LOCALE)).lower()
    return " ".join(s.split())

with open(output,'w') as outfile:
    for review in j:
        code = review['code']
        point = review['point']
        text = clean(review['text'].encode('utf-8'))
        encrypted_id = review['encrypted_id']

        outfile.write("%s '%s |f %s |u userid: %s |a word_count: %s\n"
                % (point, code, text, encrypted_id, str(text.count(" ")+1)))
