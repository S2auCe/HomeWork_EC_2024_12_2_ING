import json

import requests
from lxml import etree
import csv

url = "https://77.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124023218628531122332_1733408424929&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&dect=1&wbp2u=|0|0|0|web&fid=f3&fs=i:1.000001,i:0.399001,i:0.399005,i:0.399006,i:1.000300,i:100.HSI,i:100.HSCEI,i:124.HSCCI,i:100.TWII,i:100.N225,i:100.KOSPI200,i:100.KS11,i:100.STI,i:100.SENSEX,i:100.KLSE,i:100.SET,i:100.PSI,i:100.KSE100,i:100.VNINDEX,i:100.JKSE,i:100.CSEALL&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f124,f107&_=1733408424930"
myheaders = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

resp = requests.get(url,headers=myheaders)

resp_2 = resp.text.strip('jQuery1124023218628531122332_1733408424929(').strip(');')
js = json.loads(resp_2)

open("./asianStock.csv",mode= 'w',encoding='utf-8' )

f = open("./asianStock.csv",mode= 'a',encoding='utf-8' )
csvwriter = csv.writer(f)

js_2 = js['data']['diff']

for i in range(20):
    name = js_2[i]['f14']
    newPrice = js_2[i]['f2']
    raisePrice = js_2[i]['f4']
    raisePercentage = js_2[i]['f3']
    maxPrice = js_2[i]['f15']
    minPrice = js_2[i]['f16']
    csvwriter.writerow([name,newPrice,raisePrice,raisePercentage,maxPrice,minPrice])

