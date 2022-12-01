from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date
import logging
logging.basicConfig(level=logging.INFO)

import pandas as pd


engine = create_engine('sqlite:///artiucles.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

logger = logging.getLogger(__name__)


class Article(Base):
    __tablename__ = 'articles'

    index = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String)
    article = Column(String)
    date = Column(String)
    n_tokens_article = Column(Integer)
    

    def __init__(self, index, title, link, article, date, n_tokens_article):
        self.indexd = index
        self.title = title
        self.link = link
        self.article = article
        self.date = date
        self.n_tokens_article = n_tokens_article


def run(filename):
    """This function takes the csv file wich was created in the transform process to return a Data Base

    Args:
        filename (_str_): _The route to the csv file created in the transform process_

    Returns:
        articles.db (_db_): _A Database file created with the given data_
    """
    Base.metadata.create_all(engine)
    session = Session()
    articles = pd.read_csv(filename)

    for i, row in articles.iterrows():
        logger.info('Loading articles...')
        article = Article(row['index'],
                          row['title'],
                          row['link'],
                          row['article'],
                          row['date'],
                          row['n_tokens_article']
                          )
                          
        session.add(article)

    session.commit()
    session.close()


if __name__ == '__main__':
    run('../transform/clean_csv.csv')