# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreeimagesItem(scrapy.Item):

    # In-built names?
    image_urls = scrapy.Field()
    images = scrapy.Field()