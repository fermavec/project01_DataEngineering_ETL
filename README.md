*Note: Before you make a webscraping process please review the robots.txt file. In some countries, this process is illegal too.*

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