init:
	./1_data_analyze.py
	./2_review_to_vw.py
train:
	# 1. Train with nxvxr
	#time vw nxvxr_train.vw -c -k --cache_file test.cache --passes 10 --ngram 7 -b 30 --ect 5 -f nxvxr_model.vw --compressed
	# 2. Train with wxtchx
	time vw wxtchx_train.vw -c -k --cache_file test.cache --passes 10 --ngram 7 -b 30 --ect 5 -f wxtchx_model.vw --compressed

test:
	#vw -t --cache_file test.cache -i nxvxr_model.vw -p test.vw
	# 1. small test (nxvxr)
	#vw test.vw -t -i nxvxr_model.vw -p pred.vw
	# 2. small test2 (nxvxr)
	vw test2.vw -t -i nxvxr_model.vw -p n_pred.vw
	# 3. large wxtchx test (nxvxr)
	#vw watcha_train.vw -t -i nxvxr_model.vw -p pred_large.vw
	./4_visualize_sample.py test2.vw n_pred.vw

test2:
	# 1. small test2 (wxtchx)
	vw test2.vw -t -i wxtchx_model.vw -p w_pred.vw
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
