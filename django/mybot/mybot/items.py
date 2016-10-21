# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy_djangoitem import DjangoItem
from myapp.models import Person


class PersonItem(DjangoItem):
    django_model = Person
