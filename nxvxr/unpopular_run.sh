#!/bin/bash
for i in {0..1300}
do
    scrapy crawl nxvxr2 -a start_index=$i -o review$i.json --nolog -s CONCURRENT_REQUESTS_PER_DOMAIN=16
done
