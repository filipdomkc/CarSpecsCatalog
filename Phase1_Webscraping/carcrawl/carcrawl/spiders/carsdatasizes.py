import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import CarDataSizesItem
import re

class CarsSpiderSizes(CrawlSpider):
    name = "cars-data-sizes"
    allowed_domains = ["cars-data.com"]
    start_urls = ["https://www.cars-data.com/en/car-brands-cars-logos.html"]

    rules = (
                Rule(LinkExtractor(allow='en', deny='sizes')),
                Rule(LinkExtractor(allow='sizes'), callback = 'parse_item_sizes')
    )

    def parse_item_sizes(self, response):
        item = CarDataSizesItem()
        
        # Extract the URL
        url = response.url
        match = re.search(r'(\d{5})', url)
        
        if match:
            car_id = match.group(1)  

        item ['car_id'] = car_id   
        item ['brand'] = response.css('#breadcrumb > li:nth-child(2) > a > span::text').get()
        item ['model'] = response.css('#breadcrumb > li:nth-child(5) > span::text').get()
        item['weight'] = response.css('.grippy-host , table:nth-child(1) .grey:nth-child(2) .grey::text').get()
        item['height'] = response.css('table:nth-child(3) .grey:nth-child(4) .grey::text').get()
        item['width'] = response.css('table:nth-child(3) tr:nth-child(3) .col-6+ .col-6::text').get()
        item['length'] = response.css('table:nth-child(3) .grey:nth-child(2) .grey::text').get()
        item['wheelbase'] = response.css('table:nth-child(3) tr:nth-child(5) .col-6+ .col-6::text').get()

        yield item
