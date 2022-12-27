import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-11-27&to=2022-12-28&sortBy=popularity&language=en&apiKey=b2ae49eb975f497f84774617a6b72971')

content = r.json()
# print(content['articles'][0]['title'])

articles = content['articles']

for article in articles:
  print("Title:\n", article['title'], "\nDescription:\n", article['description'])