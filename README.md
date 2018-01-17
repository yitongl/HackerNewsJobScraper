# HackerNewsJobScraper
Filter the jobs from monthly "who's hiring" posts at HackerNews

## Usage instructions
1. pipenv install 
2. pipenv shell
3. run scraper.py with url to hn thread, list of locations & a list of role keywords to filter for
`python scraper.py scrape URL_TO_THREAD "['LOCATION']" "['ROLE']"`
Eg. ```python scraper.py scrape https://news.ycombinator.com/item?id=16052538 "['new york']" "['data scientist', 'data science']"```