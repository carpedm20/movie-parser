#!/bin/bash
rm review.json
for i in 0 1 2 3 4 5 6 7 8 10 11 12 13 14 15 16 17 18 19
do
    scrapy crawl nxvxr -a start_index=$i -o review$i.json --nolog -s CONCURRENT_REQUESTS_PER_DOMAIN=16
done
