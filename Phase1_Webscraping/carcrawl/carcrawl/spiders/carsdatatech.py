import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import CarDataTechItem
import re


class CarsSpider(CrawlSpider):
    name = "cars-data-tech"
    allowed_domains = ["cars-data.com"]
    start_urls = ["https://www.cars-data.com/en/car-brands-cars-logos.html"]

    rules = (
                Rule(LinkExtractor(allow='en', deny='tech')),
                Rule(LinkExtractor(allow='tech'), callback = 'parse_item_specs')
    )

    def parse_item_specs(self, response):
        item = CarDataTechItem()
        
        # Extract the URL
        url = response.url
        match = re.search(r'(\d{5})', url)
        
        if match:
            car_id = match.group(1) 

        item ['brand'] = response.css('#breadcrumb > li:nth-child(2) > a > span::text').get()
        item['car_id'] = car_id
        item ['model'] = response.css('#breadcrumb > li:nth-child(5) > span::text').get()
        item['cylinders'] = response.css('.grippy-host , table:nth-child(3) .grey:nth-child(2) .grey::text').get()
        item ['transmission'] = response.css('table:nth-child(1) .grey:nth-child(6) .grey::text').get()
        item ['drive_wheel'] = response.css('.grippy-host , table:nth-child(2) .grey:nth-child(2) .grey::text').get()
        item ['power'] = response.css('table:nth-child(2) tr:nth-child(7) .col-6+ .col-6::text').get()
        item['max_power_rpm'] = response.css('table:nth-child(3) .grey:nth-child(10) .grey::text').get() 
        item ['torque'] = response.css('table:nth-child(2) tr:nth-child(8) .col-6+ .col-6::text').get()
        item['max_torque_rpm'] = response.css('table:nth-child(3) .grey:nth-child(12) .grey::text').get() 
        item ['turbo'] = response.css('tr:nth-child(15) .col-6+ .col-6::text').get()
        item ['fuel']  =  response.css('table:nth-child(2) .grey:nth-child(4) .grey::text').get()
        item ['top_speed'] = response.css('table:nth-child(4) .grey:nth-child(2) .grey::text').get()
        item ['acc_0_100'] = response.css('table:nth-child(4) .grey+ tr .col-6+ .col-6::text').get()
        item ['gear_1'] = response.css('table:nth-child(8) .grey:nth-child(2) .grey::text').get()
        item ['gear_2'] = response.css('table:nth-child(8) tr:nth-child(3) .col-6+ .col-6::text').get()
        item ['gear_3'] = response.css('table:nth-child(8) tr:nth-child(4) .col-6+ .col-6::text').get()
        item ['gear_4'] = response.css('table:nth-child(8) tr:nth-child(5) .col-6+ .col-6::text').get() 
        item ['gear_5'] = response.css('table:nth-child(8) tr:nth-child(6) .col-6+ .col-6::text').get()
        item ['gear_6'] = response.css('table:nth-child(8) tr:nth-child(7) .col-6+ .col-6::text').get()
        item ['gear_7'] = response.css('table:nth-child(8) tr:nth-child(8) .col-6+ .col-6::text').get()
        item ['gear_8'] = response.css('table:nth-child(8) tr:nth-child(9) .col-6+ .col-6::text').get()
        item ['gear_9'] = response.css('table:nth-child(8) tr:nth-child(10) .col-6+ .col-6::text').get() 
        item ['gear_r'] = response.css('table:nth-child(8) tr:nth-child(11) .col-6+ .col-6::text').get()  
        item ['gear_final'] = response.css('table:nth-child(8) tr:nth-child(12) .col-6+ .col-6::text').get() 
        item ['front_tire'] = response.css('table:nth-child(7) .grey:nth-child(10) .grey::text').get()
        item ['rear_tire'] = response.css('table:nth-child(7) tr:nth-child(11) .col-6+ .col-6::text').get() 
        item['eng_capacity'] = response.css('table:nth-child(3) .grey:nth-child(4) .grey::text').get()
        
        yield item