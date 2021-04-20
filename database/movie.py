import requests
import pandas
import json
import codecs
from bs4 import BeautifulSoup

#def get_data(Link):
Link = "https://www.ambassador.com.tw/home/MovieContent?MID=75c9782a-1b2b-4f69-bc59-2377a81acce8&DT=2021/04/20"
header = {'User-Agent' : 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
requ = requests.get(Link,headers=header)




print(requ.text)