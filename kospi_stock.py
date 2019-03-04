	# -*- coding: utf-8 -*-

    
    
import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse
from collections import OrderedDict
from datetime import datetime

def kospi_stock():
    basic_url = "https://finance.naver.com/sise/"
    
    fp = urllib.request.urlopen(basic_url)
    source = fp.read()
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("span",class_="num")

    return soup[0].string

stock_data = OrderedDict()
stock_data['kospi'] = kospi_stock()

now = datetime.now()

stock_data['all_time'] = '%s-%s-%s %s:%s:%s'%(now.year, now.month, now.day, now.hour, now.minute, now.second)
stock_data['year'] = now.year
stock_data['month'] = now.month
stock_data['day'] = now.day
stock_data['hour'] = now.hour
stock_data['minute'] = now.minute
stock_data['second'] = now.second


        
print(json.dumps(stock_data, ensure_ascii=False, indent="\t"))
