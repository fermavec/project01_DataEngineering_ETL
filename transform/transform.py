import pandas as pd
import datetime
import logging
logging.basicConfig(level=logging.INFO)
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

logger = logging.getLogger(__name__)


def create_df(file):
    """This function creates the Dataframe to work with

    Args:
        file (_str_): _The path where de raw csv is located_

    Returns:
        _Object_: _A Dataframe object to work_
    """
    logger.info('Creating df')
    
    df = pd.read_csv(file, sep=',')

    logger.info('Done')

    return df


def fill_na_titles(df):
    """This function fills the null values that we got in the title feature.

    Args:
        df (_Object_): _The Dataframe with nulls_

    Returns:
        _object_: _The function returns a Dataframe object with not nulls in the title feature_
    """
    logger.info('Filling missed values')

    na_titles = []
    for e in df['link']:
        e = e.split('/')
        e = e[-1]
        e = e.split('-')
        e = " ".join(e)
        e = e.replace('.html', '')
        e = e.capitalize()
        na_titles.append(e)
    
    df['title'] = na_titles

    logger.info('Done')

    return df


def set_date(df):
    """This function add a datetime object feature

    Args:
        df (_object_): _The dataframe where we want to add a date feature_

    Returns:
        _object_: _This function returns a Dataframe with date feature in %Y-%m-%d format_
    """
    logger.info('Setting Date')

    df['date'] = datetime.datetime.now().strftime('%Y-%m-%d')

    logger.info('Done')

    return df


def token_count(df, column_name):
    """This function counts the total tokens in the column given

    Args:
        df (_object_): _The dataframe which we want to process_
        column_name (_str_): _The feature name (column)_

    Returns:
        _object_: _A dataframe with an additional feature called token_
    """
    logger.info('Token count')

    stop_words = set(stopwords.words('spanish'))

    n_tokens =  (df
                 .dropna()
                 .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1)
                 .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
                 .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
                 .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
                 .apply(lambda valid_word_list: len(valid_word_list))
            )

    df['n_tokens_' + column_name] = n_tokens

    logger.info('Done')

    return df


def run():
    """The main function to run the entire transform process.

    Returns:
        _csv_: _A csv file in the ./transform directory_
    """
    route = '../extract/elpais_2022_11_29_articles.csv'
    df = create_df(route)
    fill_na_titles(df)
    set_date(df)
    token_count(df, 'article')
    
    clean_filename = 'clean_csv'
    
    df.to_csv(clean_filename+'.csv', index_label='index')
    #print(df)


if __name__ == '__main__':
    run()