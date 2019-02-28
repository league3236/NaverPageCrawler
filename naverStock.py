	# -*- coding: utf-8 -*-

    
    
import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse

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

print(price_stock("286940"))
