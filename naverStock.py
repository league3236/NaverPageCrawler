	# -*- coding: utf-8 -*-

    
    
import urllib.request
from bs4 import BeautifulSoup
import json
from urllib import parse

origin_url = "https://search.naver.com/search.naver?"
basic_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
search_stock = "주식명"
full_url = parse.urlparse(basic_url + search_stock)
query = parse.parse_qs(full_url.query)
print(parse.urlencode(query, doseq=True))

# fp = urllib.request.urlopen(origin_url+parse.urlencode(query, doseq=True))
fp = urllib.request.urlopen("https://finance.naver.com/item/main.nhn?code=286940")
source = fp.read()
fp.close()

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("em",class_="no_down")
soup = soup[0]
soup = soup.findAll("span")
print(soup[0].string)
