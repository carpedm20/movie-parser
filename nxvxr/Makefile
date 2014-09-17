init:
	./0_data_analyze.py
	./1_review_to_vw.py
train:
	#time vw train.vw -c -k --cache_file test.cache --passes 10 --ngram 7 -b 30 --ect 5 -f nxvxr_model.vw --compressed
	time vw wxtchx_train.vw -c -k --cache_file test.cache --passes 10 --ngram 7 -b 30 --ect 5 -f wxtchx_model.vw --compressed

test:
	#vw -t --cache_file test.cache -i nxvxr_model.vw -p test.vw
	# 1. small test (nxvxr)
	#vw test.vw -t -i nxvxr_model.vw -p pred.vw
	# 2. small test2 (nxvxr)
	vw test2.vw -t -i nxvxr_model.vw -p n_pred.vw
	# 3. large wxtchx test (nxvxr)
	#vw watcha_train.vw -t -i nxvxr_model.vw -p pred_large.vw
	# 4. small test2 (wxtchx)
	vw test2.vw -t -i wxtchx_model.vw -p w_pred.vw
	# 0. print result
	#./3_visualize_sample.py test2.vw n_pred.vw
	./3_visualize_sample.py test2.vw w_pred.vw

sample:
	# wxtchx sample test
	./2_get_sample_data.py
	vw sample_watcha_train.vw -t -i nxvxr_model.vw -p pred_sample.vw
	./3_visualize_sample.py

info:
	vw-varinfo train.vw > train.vw.info
