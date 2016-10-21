import scrapy, re
from mybot.items import PersonItem

class Movies_Spider(scrapy.spiders.Spider):
    name = 'movies'
    allowed_domains = ["80s.tw"]
    start_urls = ["http://www.80s.tw/movie/list/----h"]


    def parse(self, reponse):
        selector = scrapy.Selector(reponse)
        movies = selector.xpath('//div[@class="clearfix noborder block1"]/ul[@class="me1 clearfix"]/li')
        for i in movies:
            b = PersonItem()
            name = i.xpath('h3/a/text()').extract()[0]
            name = name.replace(' ', '').replace('\n', '')
            b['name'] = name
            #b.save()
            yield b
