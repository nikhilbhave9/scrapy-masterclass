# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import date
from scrapy.loader.processors import MapCompose
from w3lib.html import remove_tags

def convert_date(d):
    d = d/1000 # Remove milliseconds
    return str(date.fromtimestamp(d))

class NaukriItem(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    description = scrapy.Field(input_processor=MapCompose(remove_tags))
    date = scrapy.Field(output_processor=MapCompose(convert_date))
