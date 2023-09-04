import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import CarInfoItem


class CarInfoSpider(CrawlSpider):
    name = "carinfo"
    allowed_domains = ["car.info"]
    start_urls = ["https://www.car.info/en-se/brands"]

    rules = (
        Rule(LinkExtractor(allow="en-se", deny="specs")),
        Rule(LinkExtractor(allow="specs"), callback="parse_carinfo_item"),
    )
        
    def parse_carinfo_item(self, response):
        
        item = CarInfoItem()
        
        div_with_drag_coefficient = response.xpath('//div[contains(text(),"Drag Coefficient")]/../div[2]/text()').get()
        drivetrain = response.xpath('//div[contains(text(),"Drivetrain")]/../div[2]/text()').get()
        power_hp = response.xpath('//div[contains(text(),"Horsepower")]/../div[2]/text()').get()
        power_kw = response.xpath('//div[contains(text(),"Power")]/../div[2]/text()').get()
        torque_nm = response.xpath('//div[contains(text(),"Torque")]/../div[2]/text()').get()
        cylinders = response.xpath('//div[contains(text(),"Cylinders")]/../div[2]/text()').get()
        eng_config = response.xpath('//div[contains(text(),"Engine Configuration")]/../div[2]/text()').get()
        eng_capacity = response.xpath('//div[contains(text(),"Displacement")]/../div[2]/text()').get()
        transmission = response.xpath('//div[contains(text(),"Transmission")]/../div[2]/text()').get()
        
        item['brand'] = response.css('.d-inline:nth-child(2) a::text').get()
        item['generation'] = response.css('.d-inline:nth-child(4) a::text').get()
        item['model'] = response.css('.d-inline:nth-child(5) a::text').get()
        
        if drivetrain:
            item['drive_wheel'] = drivetrain.replace('\n','').strip()  
        else:
            item['drive_wheel'] = 'N/A'
            
        if power_kw:
            item['power_kw'] = power_kw.replace('\n','').replace('\xa0',' ').strip()
        else:
            item['power_kw'] = 'N/A'
        
        if power_hp:
            item['power_hp'] = power_hp.replace('\n','').replace('\xa0',' ').strip()
        else:
            item['power_hp'] = 'N/A'
            
        if torque_nm:
            item['torque_nm'] = torque_nm.replace('\n','').replace('\xa0',' ').strip()
        else:
            item['torque_nm'] = 'N/A'
        if cylinders:
            item['cylinders'] = cylinders.replace('\n','').replace('\xa0',' ').strip()
        else:
            item['cylinders'] = 'N/A'
        if eng_config:   
            item['eng_config'] = eng_config.replace('\n','').replace('\xa0',' ').strip()
        else:
            item['eng_config'] = 'N/A'

        if eng_capacity:
            item['eng_capacity'] = eng_capacity.replace('\n','').replace('\xa0',' ').strip() 
        else:
            item['eng_capacity'] = 'N/A'
        
        if div_with_drag_coefficient:
            item['drag_coefficient'] = div_with_drag_coefficient.replace('\n','').strip()
        else:
            item['drag_coefficient'] = "N/A"
            
        if transmission:
            item['transmission'] = transmission.replace('\n','').replace('\xa0',' ').strip()
        else:
            item['transmission'] = 'N/A'
        
        yield item
