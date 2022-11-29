import requests
from bs4 import BeautifulSoup

#1 GET the url and response to work
URL = 'https://elpais.com/'

response = requests.get(URL)

#Webpage's text content
#print(response.text)
#Webpage's binaries
#print(response.content)
#Webpage's headers
#print(response.headers)
#Request header
#print(response.request.headers)

#2 Parsing URL with Beautiful Soup 4
soup = BeautifulSoup(response.text, 'lxml')
#print(type(soup))

#3. Work with the soup
articles = soup.find('section', attrs={'class':'_g'}).find_all('article')

#print(articles[0].a.get('href'))
#links = [article.a.get('href') for article in articles]
#titles = [title.a.get_text() for title in articles]
#print(titles)
#link = [article.a.get('href') for article in articles],
#title = [title.a.get_text() for title in articles]

news = {
    'title': [],
    'link': [],
    'article': []
}

for element in articles:
    news['title'].append(element.a.get_text())
    news['link'].append(element.a.get('href'))


links = [article.a.get('href') for article in articles]
links = [link[1:] for link in links]
for link in links:
    visit = URL + link
    response = requests.get(visit)
    soup = BeautifulSoup(response.text, 'lxml')
    article = soup.find('article', attrs={'class':'_g'})
    article = article.find('p').get_text()
    #print(article)
    #print('*'*10)


for item in news.items():    
    print(item)

#print(news )