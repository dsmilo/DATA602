## Dan Smilowitz
## DATA 602 hw3


# Design and implement a system that takes a webpage URL as input.
# The program will read the page and extract the important text (news story, blog post, etc.) from the page's source.

default_url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
import urllib

my_url = raw_input('Please enter a URL:\n')
try:
	my_html = urllib.urlopen(my_url).read()
except:
	my_html = urllib.urlopen(default_url).read()
	print '\nEntered url (%s) is invalid.\nUsing default url: %s\n' % (my_url, default_url)

from bs4 import BeautifulSoup as bs
my_soup = bs(my_html, 'html.parser')
for script in my_soup(["script", "style"]):
	extract = script.extract()
my_text = my_soup.get_text()


## Take the important text that you extracted from the page and submit it to the Alchemy API for analysis.
## Specifically, obtain the Ranked Keywords.  Once you have the keywords, print to the console the top ten results.

from watson_developer_cloud import AlchemyLanguageV1 as alc
alchemy_language = alc(api_key='194aa7702b99d164213259c1d835cfdccb97b8ad')

import json
alc_json = json.dumps(alchemy_language.keywords(max_items=10, text=my_text), indent=2)

import pandas as pd
alc_df = pd.read_json(alc_json)

keyword = []
relevance = []
for i in range(len(alc_df)):
	keyword.append(str(alc_df.keywords[i]['text'].encode('utf-8')))
	relevance.append(float(alc_df.keywords[i]['relevance']))

article_keywords = pd.DataFrame({"Keyword": keyword, "Relevance": relevance})
print article_keywords
