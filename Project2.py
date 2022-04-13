from ast import Import
from cgi import parse
import scrapy
from scrapy import cmdline
import webbrowser
import os
class BlogSpider(scrapy.Spider):
  #Set Scrapy to take the price websites
    w1 = 'KAMINEOSET'
    w2 = 'REVISESET'
    #Different sets
    name = 'price'
    start_urls = ['https://tinyurl.com/{}'.format(w1)]
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
