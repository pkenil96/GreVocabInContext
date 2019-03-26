import re
import urllib.request as ur
import requests
import logging
from bs4 import BeautifulSoup
from src.util import removeDuplicates
from src.util import createURL


logging.basicConfig(filename='../logs/logs.txt')

parent_url = 'https://www.thehindu.com/search/'
search_word = 'synergy'
order = 'DESC'
sortBy = 'publishdate'

url = createURL(parent_url, search_word, order, sortBy)
if url is not None:
    logging.info('INFO: url successfully created: {} '.format(url))
else:
    logging.error('ERROR: url is Null')

content = requests.get(url).text
soup = BeautifulSoup(content, 'html.parser')

sections = soup.find_all('section', attrs={'class': None})
news_links = []
for links in sections[0].find_all('a', href=True):
    if '.ece' in links['href']:
        news_links.append(links['href'])

news_links = removeDuplicates(news_links)

first_link = news_links[0]

res = ur.urlopen(first_link)
res = BeautifulSoup(res, 'html.parser')

para = res.find_all('div', id=re.compile("content-body*"))

para = BeautifulSoup(para[0].prettify(), 'html.parser')
final_para = para.get_text()
final_para = final_para.replace('\n', ' ')
re.sub('\s+', '', final_para).strip()
f = open('../docs/response.txt', 'w+')
f.write(final_para)
