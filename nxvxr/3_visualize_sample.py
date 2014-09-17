#!/usr/bin/python2.7
import sys

if len(sys.argv) < 2:
    test_file_name = 'sample_watcha_train.vw'
else:
    test_file_name = sys.argv[1]

if len(sys.argv) < 3:
    pred_file_name = 'pred_sample.vw'
else:
    pred_file_name = sys.argv[2]

def percent(a, b):
    return "%s/%s [%.2f%%]" % ((a), b, (float(a)/b*100))

with open(test_file_name) as test, open(pred_file_name) as pred:
    tests = test.readlines()
    preds = pred.readlines()

    total = len(tests)
    miss, big_miss, terrible_miss = 0, 0, 0

    for idx, i in enumerate(tests):
        text = i[i.find('|f')+2:i.find('|a')]
        ori = i[0]
        new = int(preds[idx].split()[0][0])

        if int(ori) != int(new):
            miss += 1

        if abs(int(ori) - int(new)) > 1:
            big_miss += 1

        if abs(int(ori) - int(new)) > 2:
            terrible_miss += 1

        print "%s->%s:%s" % (ori, new, text)

    print "\nTerrible miss (>2)\t: %s" % percent(terrible_miss, total)
    print "Big miss (>1)\t\t: %s" % percent(big_miss, total)
    print "Miss (>0)\t\t: %s\n" % percent(miss, total)
