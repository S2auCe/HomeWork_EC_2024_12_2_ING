import bs4
import requests
import csv
import re

from bs4 import BeautifulSoup

url = "http://hksclz.com/groceries/index"
myheaders = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}

req = requests.get(url, headers= myheaders)
req.encoding = 'utf-8'

page = BeautifulSoup(req.text,"html.parser")
table = page.find("table")

trs = table.find_all("tr")[1:]
lable = table.find("tr")

open("./priceOfVegetables1.csv", mode='w', encoding='utf-8')

f = open("./priceOfVegetables1.csv", mode='a', encoding='utf-8')
csvwriter = csv.writer(f)

for tr in trs:
    tds = tr.find_all("td")
    date_ = tds[0].text
    name_ = tds[1].text
    price_=tds[2].text
    csvwriter.writerow([date_,name_,price_])

req.close()

