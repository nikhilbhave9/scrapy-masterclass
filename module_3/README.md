# Introduction to Scrapy
## Scrapy Shell command
- The Scrapy Shell can be used to run some exploratory commands prior to starting a full-blown website
- Use the _shell_ command + a URL to make a direct request to the website
- We often get a "403 - forbidden" response, meaning the website has identified us a bot and banned us
- We have access to different objects like _response_ and _request_ and attributes like _headers_ and _status_
- We can also process data using _response.xpath(INCLUDE XPATH)_
