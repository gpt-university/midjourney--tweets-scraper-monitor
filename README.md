# keyword-tweets-scraper

[![Scrape any hashtag tweets](https://github.com/ahmedshahriar/depression-tweets-scraper/actions/workflows/scrape.yml/badge.svg)](https://github.com/ahmedshahriar/depression-tweets-scraper/actions/workflows/scrape.yml)

gui  with github action input




Git scraper for `#hashtag` tweets.

This scraper will scrape  tweets with `hashtag` hashtag and save them in a json file under `data` folder daily.



##  automatic cron task
by default it scrape #midjourney,#niijourney,#hugginggpt

## manually task
you can select the action and run,
in the gui,you can input any other more keywords and output saving directory


## filter twitters

https://github.com/JustAnotherArchivist/snscrape/issues/201


For likes and retweets, you can use the min_faves and min_retweets filters, respectively. For example: snscrape twitter-search 'foobar (min_faves:500 OR min_retweets:500)'

To filter by all three at once, you'd have to go the first route since you'd miss some results that only satisfy the followers limitation otherwise. For example:

import snscrape.modules.twitter

scraper = snscrape.modules.twitter.TwitterSearchScraper('test')
for tweet in scraper.get_items():
	if tweet.likeCount >= 500 or tweet.retweetCount >= 500 or tweet.user.followersCount >= 500:
		print(tweet.json())
		


## Pdf 邮件推送

https://github.com/wanghaisheng/garss

