import urllib.request
import json

API_KEY = 'f57ab94947d847f5a371d6a903ddd7f8'


url = ('https://newsapi.org/v2/everything?'
       'q=buoyant&'
       'from=2019-03-21&'
       'sortBy=popularity&'
       'apiKey=f57ab94947d847f5a371d6a903ddd7f8')


#url='https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=f57ab94947d847f5a371d6a903ddd7f8'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
json_obj = json.loads(content)
#print(json_obj['articles'][0]['title'])


i=0
for each in json_obj['articles']:
    sentence = each['description']
    #if 'inundate' not in str(sentence):
     #   continue
    #else:
    print('[{}] {}\n'.format(i,sentence))
    i+=1