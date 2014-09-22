#!/usr/bin/python
import progressbar

#predicted = "t_w_with_n_pred_large.vw"
#tested = "wxtchx_train.vw"

predicted = "t_n_with_w_pred_large.vw"
tested = "nxvxr_train.vw"

def to_reviewduk():
    with open(predicted) as predf,\
         open(tested) as testf,\
         open('sample.vw','w') as samplef:
        test_lines = testf.readlines()
        pred_lines = predf.readlines()

        bar = progressbar.ProgressBar(maxval=len(test_lines), \
              widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        for idx, line in enumerate(test_lines):
            bar.update(idx+1)

            text = test_lines[idx].split('|')[1][2:]
            code = test_lines[idx].split(' ')[1][1:]
            original = test_lines[idx][0]
            pred = pred_lines[idx].split(' ')[0]

            samplef.write("%s %s %s %s\n" % (original, pred, code, text))

        bar.finish()

to_reviewduk()
