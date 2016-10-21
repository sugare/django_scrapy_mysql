# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import BaseSpider
from mybot.items import PersonItem

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com/',
    )

    def parse(self, response):
        return PersonItem(name='rolando')
