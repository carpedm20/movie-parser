#!/bin/bash
for i in {0..100}
do
    scrapy crawl nxvxr -a start_index=$i -o review$i.json --nolog -s CONCURRENT_REQUESTS_PER_DOMAIN=24
done

for i in {0..1300}
do
    scrapy crawl nxvxr2 -a start_index=$i -o unpopular_review$i.json --nolog -s CONCURRENT_REQUESTS_PER_DOMAIN=24
done
