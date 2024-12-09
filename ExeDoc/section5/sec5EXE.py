import json

import requests
from lxml import etree
import csv

url = "https://27.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406768413684890973_1733749469237&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&dect=1&wbp2u=|0|0|0|web&fid=f3&fs=i:100.DJIA,i:100.SPX,i:100.NDX,i:100.TSX,i:100.BVSP,i:100.MXX&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f124,f107&_=1733749469321"
myheaders = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

resp = requests.get(url,headers=myheaders)

resp_2 = resp.text.strip('jQuery1124023218628531122332_1733408424929(').strip(');')
js = json.loads(resp_2)

open("./AmericaStock.csv",mode= 'w',encoding='utf-8' )

f = open("./AmericaStock.csv",mode= 'a',encoding='utf-8' )
csvwriter = csv.writer(f)

js_2 = js['data']['diff']

for i in range(6):
    name = js_2[i]['f14']
    newPrice = js_2[i]['f2']
    raisePrice = js_2[i]['f4']
    raisePercentage = js_2[i]['f3']
    maxPrice = js_2[i]['f15']
    minPrice = js_2[i]['f16']
    csvwriter.writerow([name,newPrice,raisePrice,raisePercentage,maxPrice,minPrice])

