import requests
from bs4 import BeautifulSoup
import csv
import datetime


def get_response(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    return soup


def extract_links(soup):
    links = soup.find('section', attrs={'class':'_g'}).find_all('article')
    links = [link.a.get('href') for link in links]

    return links


def extract_titles(soup):
    titles = soup.find('section', attrs={'class':'_g'}).find_all('article')
    titles = [title.a.get_text() for title in titles]

    return titles


def extract_resume(url, links):
    articles = []
    links = [link[1:] for link in links]
    
    for link in links:
        visit = url + link
        response = requests.get(visit)
        soup = BeautifulSoup(response.text, 'lxml')
        article = soup.find('article', attrs={'class':'_g'})
        article = article.find('p').get_text()
        articles.append(article)
    
    return articles


def info_to_dict(url):
    soup = get_response(url)
    links = extract_links(soup)
    titles = extract_titles(soup)
    articles = extract_resume(url, links)
    
    news = []
    for i, _ in enumerate(articles):
        news_details = {
            'title': titles[i],
            'link': links[i],
            'article': articles[i]
        }
        news.append(news_details)
        
    print(news)

    return news


def run():
    URL = 'https://elpais.com/'
    data = info_to_dict(URL)
    now = datetime.datetime.now().strftime('%Y_%m_%d')

    out_file_name = 'elpais_{datetime}_articles.csv'.format(datetime=now)
    csv_headers = ['title', 'link', 'article']

    with open(out_file_name, mode='w+') as f:
        writer = csv.DictWriter(f, fieldnames=csv_headers)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    run()
