# scraping garfield comics
import requests
from bs4 import BeautifulSoup
import random
from datetime import date

todays_date = date.today()
print(todays_date.year)
def randomDate():
    year = random.randint(1978,todays_date.year)
    if year==1978:
        day = random.randint(19,30)
        month = random.randint(6,12)
    else:
        month = random.randint(1,12)
        if month in [1,3,5,7,8,10,12]:
            day = random.randint(1,31)
        elif month == 2:
            day = random.randint(1,28)
        else:
            day = random.randint(1,30)
    if len(str(day))==1:
        day = '0' + str(day)
    if len(str(month))==1:
        month = '0' + str(month)
    s = f'{year}/{month}/{day}'
    return s

# for i in range(11):
s = randomDate()
url = f'https://www.gocomics.com/garfield/{s}'
print('website url = ',url)
html = requests.get(url)
soup = BeautifulSoup(html.text , 'html.parser')

tag = soup('img',class_='lazyload img-fluid')[1]

imageUrl = tag.get('src',None)
print('image Url = ',imageUrl)