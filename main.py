import requests

# r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-11-27&to=2022-12-28&sortBy=popularity&language=en&apiKey=b2ae49eb975f497f84774617a6b72971')

# content = r.json()
# # print(content['articles'][0]['title'])

# articles = content['articles']

# for article in articles:
#   print("Title:\n", article['title'], "\nDescription:\n", article['description'])

def get_news(topic, from_date, to_date, language='en', api_key='b2ae49eb975f497f84774617a6b72971'):
  url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&{language}=en&apiKey={api_key}"
  r = requests.get(url)
  content = r.json()
  articles = content['articles']

  results = []
  for article in articles:
    results.append(f"TITLE:\n{article['title']}\nDESCRIPTION:\n{article['description']}")

  return '\n'.join(results)
  
print(get_news(topic='stock', from_date='2022-12-25', to_date='2022-12-28')) 