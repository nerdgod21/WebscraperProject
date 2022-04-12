from ast import Import
from cgi import parse
import scrapy
from scrapy import cmdline


class BlogSpider(scrapy.Spider):
    w1 = 'KAMINEOSET'
    w2 = 'REVISESET'
    w3 = 'Mind'
    w4 = 'Sculptor'
    t = '#online'
    name = 'price'
    start_urls = ['https://tinyurl.com/{}'.format(w1)]
    def parse(self, response):
      page = response.url
      filename = 'Prices.html'
      with open (filename, 'wb') as f :
            f.write (response.body)
cmdline.execute("scrapy runspider Project2.py".split())
