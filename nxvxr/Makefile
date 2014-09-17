init:
	./0_data_analyze.py
	./1_review_to_vw.py
train:
	time vw train.vw -c -k --cache_file test.cache --passes 10 --ngram 7 -b 30 --ect 5 -f model.vw --compressed

test:
	#vw -t --cache_file test.cache -i model.vw -p test.vw
	# small test
	#vw test.vw -t -i model.vw -p pred.vw
	# small test2
	vw test2.vw -t -i model.vw -p pred.vw
	# large wxtchx test
	#vw watcha_train.vw -t -i model.vw -p pred_large.vw
	./3_visualize_sample.py test2.vw pred.vw

sample:
	# wxtchx sample test
	./2_get_sample_data.py
	vw sample_watcha_train.vw -t -i model.vw -p pred_sample.vw
	./3_visualize_sample.py

info:
	vw-varinfo train.vw > train.vw.info
