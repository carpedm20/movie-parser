init:
	./1_data_analyze.py
	./2_review_to_vw.py
train:
	# 1. Train with nxvxr
	time vw nxvxr_train.vw -c -k --cache_file test.cache --passes 13 --ngram 7 -b 30 --ect 5 -f nxvxr_model.vw --compressed

train-info:
	# 1. Train with nxvxr
	time ~/bin/vw-varinfo -c -k --passes 13 --ngram 7 -b 30 nxvxr_train.vw > varinfo.txt

train2:
	# 2. Train with wxtchx
	time vw wxtchx_train.vw -c -k --cache_file test.cache --passes 10 --ngram 7 -b 30 --ect 5 -f wxtchx_model.vw --compressed

train-info2::
	# 1. Train with nxvxr
	time ~/bin/vw-varinfo -c -k --passes 13 --ngram 7 -b 30 wxtchx_train.vw > varinfo.txt

test:
	#vw -t --cache_file test.cache -i nxvxr_model.vw -p test.vw
	# 1. small test (nxvxr)
	#vw test.vw -t -i nxvxr_model.vw -p pred.vw
	# 2. small test2 (nxvxr)
	#vw test2.vw -t -i nxvxr_model.vw -p n_pred.vw
	# 3. large wxtchx test (nxvxr)
	vw wxtchx_train.vw -t -i nxvxr_model.vw -p t_w_with_n_pred_large.vw
	./4_visualize_sample.py test2.vw n_pred.vw

test2:
	# 1. small test2 (wxtchx)
	#vw test2.vw -t -i wxtchx_model.vw -p w_pred.vw
	# 2. large wxtchx test (wxtchx)
	vw nxvxr_train.vw -t -i wxtchx_model.vw -p t_n_with_w_pred_large.vw
	# 0. print result
	./4_visualize_sample.py test2.vw w_pred.vw

sample:
	# wxtchx sample test with nxvxr model
	./3_get_sample_data.py wxtchx_train.vw
	vw sample_wxtchx_train.vw -t -i nxvxr_model.vw -p n_pred_sample.vw
	./4_visualize_sample.py sample_wxtchx_train.vw n_pred_sample.vw

sample2:
	# wxtchx sample test with wxtchx model
	./3_get_sample_data.py nxvxr_train.vw
	vw sample_nxvxr_train.vw -t -i wxtchx_model.vw -p w_pred_sample.vw
	./4_visualize_sample.py sample_nxvxr_train.vw w_pred_sample.vw

info:
	vw-varinfo nxvxr_train.vw > nxvxr_train.vw.info
