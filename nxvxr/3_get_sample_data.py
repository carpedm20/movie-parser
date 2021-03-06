#!/usr/bin/python2.7
import sys
import random

COUNT = 10000

if len(sys.argv) < 2:
    train_name = "wxtchx_train.vw"
else:
    train_name = sys.argv[1]

out_name = "sample_" + train_name

with open(train_name) as trainf, open(out_name, 'w') as outf:
    lines = trainf.readlines()
    random.shuffle(lines)

    outf.writelines(lines[:COUNT])
