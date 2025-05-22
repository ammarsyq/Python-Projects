from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib

url = 'https://www.amazon.com/World-War-Oral-History-Zombie/dp/0307346617/ref=sr_1_1?crid=2IX6DF181LA2D&dib=eyJ2IjoiMSJ9.MpaeniOw1FKqMXzEU_74pkKC02YGcwqX26r4mg0o8u_6ZSwlBBnXzZMrjy3InEd3eWkcn72Do1eSn5vyHUnFgh90Nv0mw5dg5MgaahFlEmbblkZCWyStFSjZOc_hdzcjwvvijK-x4qFugQ6g9W9vmiubYxGq_lNTwVQVbOoACksuI7yEh6bYHrho4isEAkmWn9iHAI8QB83xFD9K8QYbb2wZzRmjGZYu6xct2hw1oCM.K5VdsvYM4BLc7bIoGKKJThdaa2mnVAbucBP0rR0XsuQ&dib_tag=se&keywords=world+war+z&qid=1746750238&sprefix=world+war+%2Caps%2C419&sr=8-1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(class_='a-size-base a-color-price a-color-price').get_text()

price = price.strip()[1:]
title = title.strip()
today = datetime.date.today()

import csv

header = ['book title', 'price','insert date']
data = [title, price, today]

with open('amz_webscrp_data.csv', 'w', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

import pandas as pd

df = pd.read_csv('amz_webscrp_data.csv')
df

#adding data
with open('amz_webscrp_data.csv', 'a+', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

#add data automation
def check_price():
    url = 'https://www.amazon.com/World-War-Oral-History-Zombie/dp/0307346617/ref=sr_1_1?crid=2IX6DF181LA2D&dib=eyJ2IjoiMSJ9.MpaeniOw1FKqMXzEU_74pkKC02YGcwqX26r4mg0o8u_6ZSwlBBnXzZMrjy3InEd3eWkcn72Do1eSn5vyHUnFgh90Nv0mw5dg5MgaahFlEmbblkZCWyStFSjZOc_hdzcjwvvijK-x4qFugQ6g9W9vmiubYxGq_lNTwVQVbOoACksuI7yEh6bYHrho4isEAkmWn9iHAI8QB83xFD9K8QYbb2wZzRmjGZYu6xct2hw1oCM.K5VdsvYM4BLc7bIoGKKJThdaa2mnVAbucBP0rR0XsuQ&dib_tag=se&keywords=world+war+z&qid=1746750238&sprefix=world+war+%2Caps%2C419&sr=8-1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(class_='a-size-base a-color-price a-color-price').get_text()
    price = price.strip()[1:]
    title = title.strip()
    import datetime
    today = datetime.date.today()
    import csv

    header = ['book title', 'price','insert date']
    data = [title, price, today]
    with open('amz_webscrp_data.csv', 'a+', newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


while(True):
    check_price()
    time.sleep(5)