init:
	vw train.vw -c -k --cache_file test.cache --passes 10 --ngram 7 -b 30 --ect 5 -f model.vw --compressed

test:
	#vw -t --cache_file test.cache -i model.vw -p test.vw
	vw test.vw -t -i model.vw -p pred.vw
