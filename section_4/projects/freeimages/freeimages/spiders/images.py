import scrapy
from freeimages.items import FreeimagesItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ImagesSpider(scrapy.Spider):
    name = "images"
    allowed_domains = ["freeimages.com"]
    start_urls = ["https://freeimages.com/search/cat"]
    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=(
                "//div[contains(@class, 'masonry-container')]"
            )),
            callback="parse",
            follow=False
        ),
    )

    def parse(self, response):
        item = ItemLoader(item=FreeimagesItem(), response=response, selector=response)
        item.add_xpath("image_urls", "//div[@class='grid-image-wrapper']/img/@src")
        yield(item.load_item())
