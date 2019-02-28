# -*- coding: utf-8 -*-

    
    
import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse
import json
from collections import OrderedDict
from datetime import datetime

def price_stock(code_num):
    basic_url = "https://finance.naver.com/item/main.nhn?code="
#     code_num = "286940"
    full_url = basic_url+code_num
    
    fp = urllib.request.urlopen(full_url)
    source = fp.read()
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("em",class_="no_down")
    soup = soup[0]
    soup = soup.findAll("span")
    
    return soup[0].string

stock_list = [['롯데정보통신','286940'],
             ['롯데지주','004990'],
             ['롯데케미칼','011170'],
             ['롯데쇼핑','023530'],
             ['롯데정밀화학', '004000']]

stock_data = OrderedDict()

for row in range(len(stock_list)):
    for col in range(len(stock_list[0])):
        if col%2 == 0:
            name=stock_list[row][col]
        else:
            code=stock_list[row][col]
        stock_data[name] = price_stock(code)

now = datetime.now()

stock_data['all_time'] = '%s-%s-%s %s:%s:%s'%(now.year, now.month, now.day, now.hour, now.minute, now.second)
stock_data['year'] = now.year
stock_data['month'] = now.month
stock_data['day'] = now.day
stock_data['hour'] = now.hour
stock_data['minute'] = now.minute
stock_data['second'] = now.second


        
print(json.dumps(stock_data, ensure_ascii=False, indent="\t"))
