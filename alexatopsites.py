import requests
from bs4 import BeautifulSoup
import datetime
import os

#  Set up the path
path = datetime.datetime.today().strftime('%Y-%m-%d')

#  Set up the filename for the results
result = 'result-{}.txt'.format(datetime.datetime.today().strftime('%H-%M-%S'))

top_sites = []
cat_pages = []


def getCategory(page):
    '''
    Get all sub-categories URLs
    An extra function in case you need sub-categories URLs
    '''

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}

    try:
        html = requests.get(page, headers=headers)
        bs = BeautifulSoup(html.content, 'html.parser')
    except Exception as e:
        raise e

    for ul in bs.find_all('ul', class_='subcategories span3'):
        for li in ul.findChildren('li'):
            relative_path = li.a['href']
            newPage = 'https://www.alexa.com/' + relative_path

            if newPage not in cat_pages:
                print(newPage)
                cat_pages.append(newPage)
                getCategory(newPage)

    return cat_pages


def getSites(page):
    '''
    Get all top site domains
    '''

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}

    try:
        html = requests.get(page, headers=headers)
        bs = BeautifulSoup(html.content, 'html.parser')
    except Exception as e:
        raise e

    # Loop for Subcategories
    for ul in bs.find_all('ul', class_='subcategories span3'):
        for li in ul.findChildren('li'):
            relative_path = li.a['href']
            newPage = 'https://www.alexa.com/' + relative_path
            if newPage not in cat_pages:
                # print(newPage)

                try:
                    html = requests.get(newPage, headers=headers)
                    bs = BeautifulSoup(html.content, 'html.parser')

                except Exception as e:
                    raise e

                for td in bs.find_all('div', class_="td DescriptionCell"):
                    site = td.p.a.get_text()

                    if site not in top_sites:
                        print (site)
                        if not os.path.exists(path):
                            os.makedirs(path)
                        with open(os.path.join(path, result), 'a') as r:
                            r.write(site + '\n')

                        top_sites.append(site)

                cat_pages.append(newPage)
                getSites(newPage)

    # Loop for Countries
    for ul in bs.find_all('ul', class_='countries span3'):
        for li in ul.findChildren('li'):
            relative_path = li.a['href']
            newPage = 'https://www.alexa.com/' + relative_path
            if newPage not in cat_pages:
                # print(newPage)

                try:
                    html = requests.get(newPage, headers=headers)
                    bs = BeautifulSoup(html.content, 'html.parser')

                except Exception as e:
                    raise e

                for td in bs.find_all('div', class_="td DescriptionCell"):
                    site = td.p.a.get_text()

                    if site not in top_sites:
                        print (site)
                        if not os.path.exists(path):
                            os.makedirs(path)
                        with open(os.path.join(path, result), 'a') as r:
                            r.write(site + '\n')

                        top_sites.append(site)

                cat_pages.append(newPage)
                getSites(newPage)

    # Loop for Topsites
    for td in bs.find_all('div', class_="td DescriptionCell"):
        site = td.p.a.get_text()

        if site not in top_sites:
            print (site)
            if not os.path.exists(path):
                os.makedirs(path)
            with open(os.path.join(path, result), 'a') as r:
                r.write(site + '\n')

            top_sites.append(site)

    return top_sites


staringPages = [
    'https://www.alexa.com/topsites',
    'https://www.alexa.com/topsites/countries',
    'https://www.alexa.com/topsites/category'
]

for staringPage in staringPages:
    getSites(staringPage)
