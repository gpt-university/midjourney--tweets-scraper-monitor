import datetime
import os
# import twint
import pathlib
hashtags = os.getenv('hashtags').strip()
outdir = os.getenv('outdir').strip()
keywords=[]


if len(outdir)==0:
    outdir='data'
if ',' in hashtags:
    keywords = hashtags.split(',')

else:
    keywords=[].append(hashtags)

# keywords=['midjourney,niijourney']

def sns_scrape(keyword,DATE_START,JSON_FILENAME,min_faves):
    min_retweets=0
    if min_faves =='':
        min_faves=50
    min_replies=10
    
    print('scrapeing job:',f'snscrape --jsonl --progress --since {DATE_START} twitter-hashtag "{keyword}" > {JSON_FILENAME}.json')
#     os.system(f'snscrape --jsonl --progress --since {DATE_START} twitter-hashtag "{keyword}" > {JSON_FILENAME}.json')
    os.system(f'snscrape --jsonl --progress --since {DATE_START} twitter-hashtag "{keyword} )"   (min_faves:{min_faves}  > {JSON_FILENAME}+"-"+{min_faves}.json')

    print('done',keyword)

    # with end date
    # os.system(f'snscrape --jsonl --progress --since {DATE_START} twitter-hashtag "{HASHTAG} until:{DATE_END}" > {JSON_FILENAME}.json')

def scrape_twint():
    c = twint.Config()
    # c.Until = str(datetime.datetime.today().date() + datetime.timedelta(days=1))
    c.Since = str(datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1))
    # c.Username = "test"
    c.Search = "#depression"
    c.Location=True
    c.Images = True
    # c.Limit = 50
    # c.Custom["user"] = ["id", "tweet", "user_id", "username", "hashtags", "mentions"]
    c.User_full = True
    c.Store_csv = True
    c.Output = "test3.csv"
    c.Debug = True
    twint.run.Search(c)



if __name__ == "__main__":
    # scrape_twint()
#     keywords=list(set(keywords))
    if keywords is None:
        keywords=[]
    if len(keywords) | len(list(set(keywords)))==0:
#         keywords=['niijourney']
        keywords=['HuggingGPT','niijourney','midjourney','chatgpt']

    for keyword in keywords:
        DATE_START = str(datetime.datetime.today().date() - datetime.timedelta(days=1))

        DATA_PATH = pathlib.Path((keyword+'-'+outdir).replace('/','')+"/")
        DATA_PATH.mkdir(parents=True, exist_ok=True)

        if not DATA_PATH.exists():
            os.mkdir(DATA_PATH)

        # MAX_RESULT = 100
        # DATE_END = '2020-05-08'
        JSON_FILENAME = DATA_PATH / str(datetime.datetime.today().date())   
        print('============\nkeyword start:',keyword)
        print('===========\n',JSON_FILENAME)
        sns_scrape(keyword,DATE_START,JSON_FILENAME,50)
        print('============\nkeyword end:',keyword)
        sns_scrape(keyword,DATE_START,JSON_FILENAME,100)


# reference
# https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af
# https://github.com/hansheng0512/tweets-scrapping-using-python
# https://github.community/t/can-github-actions-directly-edit-files-in-a-repository/17884/7
