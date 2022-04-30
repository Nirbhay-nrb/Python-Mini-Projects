import requests
from bs4 import BeautifulSoup
import random
import datetime
from datetime import date

todays_date = date.today()

def randomDate():
    year = random.randint(1950,todays_date.year)
    if year==1950: # from october 2nd
        month = random.randint(10,12)
        if month == 10:
            day = random.randint(2,31)
        elif month == 11:
            day = random.randint(1,30)
        else: 
            day - month.randint(1,31)
    else:
        month = random.randint(1,12)
        if month in [1,3,5,7,8,10,12]:
            day = random.randint(1,31)
        elif month == 2:
            day = random.randint(1,28)
        else:
            day = random.randint(1,30)
    if year in [1950,1951]:
        day_name = datetime.date(year,month,day) 
        if day_name.strftime("%A") == 'Sunday':
            randomDate()
    if len(str(day))==1:
        day = '0' + str(day)
    if len(str(month))==1:
        month = '0' + str(month)
    s = f'{year}/{month}/{day}'
    return s

def randomImage():
    s = randomDate()
    url = f'https://www.gocomics.com/peanuts/{s}'
    print('Website url = ',url)
    html = requests.get(url)
    soup = BeautifulSoup(html.text , 'html.parser')
    tag = soup('img',class_='lazyload img-fluid')[1]
    imageUrl = tag.get('src',None)
    print('image Url = ',imageUrl)

randomImage()