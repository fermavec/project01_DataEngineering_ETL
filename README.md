*Note: Before you make a webscraping process please review the robots.txt file. In some countries, this process is illegal too.*
*Note 2: In every directory you will find a raw file where I did some trials*

# Data Engineering
### First step.
Don't forget to create a virtual environment to run this project by executing the next commands in your bash:
```
-> cd <path\to\the\directory\where\you\save\or\clone\this\project>
-> python3 -m venv venv
-> .\venv\Scripts\activate
-> pip install requirements.txt
```

## ETL Process

### Extract
For this project, I'm gonna use a web scraping process to get data from elpais.com digital version.
Please run the next command in your shell if you just want to get the data from elpais.com
```
-> cd extract
-> py extract.py
```
This returns a csv file to work with.

### Transform
First of all, you need to install nltk stopwords and punt so run the next command in your terminal:
```
-> cd transform
-> python -m nltk.downloader stopwords
-> python -m nltk.downloader punkt
```
Then you can run:
```
-> py transform.py
```
The result is a "clean" csv file in your directory ./transform

### Load
To load the data in a database I'm gonna use sqlalchemy so please be sure that library is installed in your virtual environment befora run the program. Follow the next commands to get the DB.
```
-> cd load
-> py load.py
```
You will find a fille called articles.db.

## Thanks
There is no final recomendation just have fun changing and playing with this code on your computer. 

You can follow me on instagram, twitter, Facebook, Medium, Github and Linkedin as @fermavec or you can visit my webpage: http://fermavec.com