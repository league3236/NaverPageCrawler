	# -*- coding: utf-8 -*-

    
    
import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse
from collections import OrderedDict
from datetime import datetime
import sys

def price_stock(code_num):
    basic_url = "https://finance.naver.com/item/main.nhn?code="
    full_url = basic_url+code_num
    
    fp = urllib.request.urlopen(full_url)
    source = fp.read()
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    try :
        soup = soup.findAll("em",class_="no_up")
    except :
        soup = soup.findAll("em",class_="no_down") #장 마감
    soup = soup[0]
    soup = soup.findAll("span")
    return soup[0].string



stock_list = [['주가이름','주가번호']]

stock_data = OrderedDict()

code_name = sys.argv[1]
for name in range(len(stock_list)):
    if stock_list[name][0] == code_name:
        code_num = stock_list[name][1]
        break

stock_data[code_name] = price_stock(code_num)

now = datetime.now()

stock_data['all_time'] = '%s-%s-%s %s:%s:%s'%(now.year, now.month, now.day, now.hour, now.minute, now.second)
stock_data['year'] = now.year
stock_data['month'] = now.month
stock_data['day'] = now.day
stock_data['hour'] = now.hour
stock_data['minute'] = now.minute
stock_data['second'] = now.second


        
print(json.dumps(stock_data, ensure_ascii=False, indent="\t"))
