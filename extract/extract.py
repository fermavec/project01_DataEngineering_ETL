import requests
from bs4 import BeautifulSoup
import csv
import logging
logging.basicConfig(level=logging.INFO)
import datetime

logger = logging.getLogger(__name__)


def get_response(url):
    """Takes an url to get a response, then creates a soup to work with.

    Args:
        url (_str_): _web page domain_

    Returns:
        _object_: _soup created with BS4_
    """
    logging.info('Getting response...') 
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
    except Exception as e:
        print('URL response error')
        print(e)

    logging.info('Response OK') 
    
    return soup


def extract_links(soup):
    """Takes a soup object to get the link information from elpais.com

    Args:
        soup (_object_): _Soup created with get_response(url)_

    Returns:
        _list_: _list with all links from the given domain_
    """
    logging.info('Extracting links...')

    links = soup.find('section', attrs={'class':'_g'}).find_all('article')
    links = [link.a.get('href') for link in links]

    logging.info('Links OK...')

    return links


def extract_titles(soup):
    """Takes the a soup object to get the title from elpais.com

    Args:
        soup (_object_): _Soup created with get_response(url)_

    Returns:
        _list_: _list with all titles from the given domain_
    """
    logging.info('Extracting titles...')

    titles = soup.find('section', attrs={'class':'_g'}).find_all('article')
    titles = [title.a.get_text() for title in titles]

    logging.info('Titles OK')

    return titles


def extract_resume(url, links):
    """This function gets the article from link and an url in elpais.com homepage

    Args:
        url (_str_): _The domain url_
        links (_list_): _list of links_

    Returns:
        _list_: _list of articles from elpais.com homepage_
    """
    logging.info('Extracting articles...')

    articles = []
    links = [link[1:] for link in links]
    
    for link in links:
        try:
            visit = url + link
            response = requests.get(visit)
            soup = BeautifulSoup(response.text, 'lxml')
            article = soup.find('article', attrs={'class':'_g'})
            article = article.find('p').get_text()
            articles.append(article)
        except Exception as e:
            print('response error')
            print(e)
    
    logging.info('Articles OK')

    return articles


def info_to_dict(url):
    """Turns all the information extracted into a dictionary

    Args:
        url (_str_): _used to format link's objectn_

    Returns:
        _dict_: _All the information extracted in a dictionary_
    """
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
        
    #print(news)

    return news


def run():
    """The main function wich runs all the scripts to get data from elpais.com

    Returns:
        _file_: _csv file with all the data from elpais.com_
    """
    logging.info('Beginning Scraper...')

    URL = 'https://elpais.com/'
    data = info_to_dict(URL)
    now = datetime.datetime.now().strftime('%Y_%m_%d')

    out_file_name = 'elpais_{datetime}_articles.csv'.format(datetime=now)
    csv_headers = ['title', 'link', 'article']

    with open(out_file_name, mode='w+') as f:
        writer = csv.DictWriter(f, fieldnames=csv_headers)
        writer.writeheader()
        writer.writerows(data)

    logging.info('Process Done')


if __name__ == '__main__':
    run()
