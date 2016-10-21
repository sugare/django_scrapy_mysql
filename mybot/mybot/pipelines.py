# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import PersonItem

class MybotPipeline(object):
    def process_item(self, item, spider):
        #a = PersonItem()
        #a['name'] = item['name']
        #a.save
        item.save()
        #print item
        return item
