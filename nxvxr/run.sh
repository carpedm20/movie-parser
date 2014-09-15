#!/bin/bash
rm review.json
scrapy crawl nxvxr -o review.json --nolog -s CONCURRENT_REQUESTS_PER_DOMAIN=16
