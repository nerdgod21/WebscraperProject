from ast import Import
from cgi import parse
import scrapy
from scrapy import cmdline
import webbrowser
import os
from lxml import html
import requests
page = requests.get('https://www.ebay.com/itm/403592776720?hash=item5df8010c10:g:jncAAOSwsptiPwy~.html')
tree = html.fromstring(page.content)
buyers = tree.xpath('//*[@id="viTabs_0_is"]/div/div[2]/div/div[4]/div[4]/div/div/span/text()')

class BlogSpider(scrapy.Spider):
  #Set Scrapy to take the price websites
    #Different sets
    if buyers == ['Kamigawa: Neon Dynasty']:
        setname = "KAMINEOSET"
    name = 'Price'
    start_urls = ['https://tinyurl.com/{}'.format(setname)]
    def parse(self, response):
      page = response.url
      filenam = 'Prices.html'
      with open(filenam, 'wb') as f:
            f.write(response.body)
      #create HTML file out of website

filename = 'file:///'+os.getcwd()+'/' + 'Prices.html'
webbrowser.open_new_tab(filename)
#Open the price file
cmdline.execute("scrapy runspider WebProject/Project2.py".split())
#Necesary scrapy run
