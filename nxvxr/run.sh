#!/bin/bash
for i in {0..30}
do
    scrapy crawl nxvxr -a start_index=$i -o review$i.json --nolog -s CONCURRENT_REQUESTS_PER_DOMAIN=16
done
