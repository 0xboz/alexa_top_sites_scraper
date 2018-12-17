##Alexa.com Top Sites Scraper


####What is this all about?
Alexa.com is an internet traffic ranking company which provides premium data for its customers. It also offers [a limited list of top sites](https://www.alexa.com/topsites) on the web for free.

This script was created to scrape those top sites and store them in a text file. It simply goes through all sub-catagories, retrieve the sites in each table and remove any duplicates.

And of course, if you need the premium data from Alexa.com, you can find more information [here](https://aws.amazon.com/alexa-top-sites/). 

Pricing: $0.0025 per URL returned (e.g. <b>$.25 for 100 URLs</b>) at the time of writing.

####Prerequisite

Virtualenv or similar (such as, pipenv) is recommended before running the script. 

Python 3.6.7

```
pip install requests==2.21.0
pip install beautifulsoup4==4.6.3
```

####How to use the script

```
git clone https://github.com/0xboz/alexatopsites.git
cd alexatopsites
python alexatopsites.py
```

A folder named as the current date will be created when you run the script each time. All results will be stored in a text file.
