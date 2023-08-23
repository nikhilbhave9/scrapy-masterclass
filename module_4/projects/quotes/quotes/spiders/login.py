import scrapy
from scrapy import Request, FormRequest

class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    # Handles to response after the initial request to the login page is made
    def parse_login(self, response):
        req = FormRequest.from_response(response, formdata={"username": "nick", "password": "mypass"})
        self.log("Sent:" + str(req.body))

    # Gathers the initial requests that the spider needs to begin crawling 
    def start_requests(self):
        return [Request("http://quotes.toscrape.com/login", callback=self.parse_login)]
    
    def parse(self, response, **kwargs):
        pass