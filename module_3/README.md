# Introduction to Scrapy
## Scrapy Shell command
- The Scrapy Shell can be used to run some exploratory commands prior to starting a full-blown project
- Use the _shell_ command + a URL to make a direct request to the website
- We often get a "403 - forbidden" response, meaning the website has identified us a bot and banned us
- We have access to different objects like _response_ and _request_ and attributes like _headers_ and _status_
- We can also process data using _response.xpath(INCLUDE XPATH)_

## Creating our first Scrapy project
1. Create a Python virtual environment
2. Create a new scrapy project using "scrapy startproject NAME"
3. The project directory will contain another dir with the same name and a scrapy.cfg file. Inside the dir, we will be able to access multiple spiders under the spiders sub-dir as well as items, middleware, pipelines, settings, etc.

- Under _settings.py_, we will have a Robotstxt_Obey = True. Many websites have a robots.txt file that tell a bot visting them what is encouraged and what is discouraged (About, Privacy Page, etc). Choosing to obey is optional.
- _items.py_ contains all the items/attributes that we would like to scrape
- _middleware.py_ gives us a template to decide what kind of logic we want to apply before visiting a website AND how we want to process it after
- _pipeline.py_ provides options for post-processing and storage after scraping
