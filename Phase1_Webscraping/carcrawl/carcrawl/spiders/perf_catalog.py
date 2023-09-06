import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AutocatalogItem
import re

class AutocatalogspiderSpider(CrawlSpider):
    name = "perf_catalog"
    allowed_domains = ["automobile-catalog.com"]
    start_urls = ["https://www.automobile-catalog.com/auta_sp_browse_2.php"]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    
        # Rule 1: Extract links containing 'list-'
    rules = (
        Rule(LinkExtractor(allow=('/list-')), callback='parse_list_links'),
    )

    # Callback for links containing 'list-'
    def parse_list_links(self, response):
        # Rule 2: Extract links containing '/model'
        model_links = LinkExtractor(allow=('/model')).extract_links(response)
        for model_link in model_links:
            yield scrapy.Request(model_link.url, callback=self.parse_model_links, headers=self.headers)

    # Callback for links containing '/model'
    def parse_model_links(self, response):
        # Rule 3: Extract links containing '/make'
        make_links = LinkExtractor(allow=('/make')).extract_links(response)
        for make_link in make_links:
            yield scrapy.Request(make_link.url, callback=self.parse_make_links, headers=self.headers)

    # Callback for links containing '/make'
    def parse_make_links(self, response):
        # Rule 4: Extract links containing '/performance'
        performance_links = LinkExtractor(allow=('/performance')).extract_links(response)
        for performance_link in performance_links:
            yield scrapy.Request(performance_link.url, callback=self.parse_performance_links, headers=self.headers)

    # Callback for links containing '/performance'
    def parse_performance_links(self, response):
        item = AutocatalogItem ()
        
        # Extract the URL
        url = response.url
        match = re.search(r'(\d{6,7})', url)
        
        if match:
            car_id = match.group(1)  
        
        print("Parsing performance page:", response.url)
        item['car_id'] = car_id
        item['brand'] = response.css('.v .v table+ table tr:nth-child(7) b::text').get()
        item['model'] = response.css('.v tr:nth-child(8) a font::text').get()
        item['generation'] = response.css('tr:nth-child(10) td+ td p b a font::text').get()
        item['engine_type'] = response.css('.v .v table+ table tr:nth-child(18) b::text').get()
        item['cyl_align'] = response.css('.v .v table+ table tr:nth-child(20) b::text').get()
        item['eng_capacity'] = response.css('.v .v table+ table tr:nth-child(21) b::text').get()
        item['transmission_type'] = response.css('tr:nth-child(24) b::text').get()
        item['drive_wheel'] = response.css('.v .v table+ table tr:nth-child(17) b::text').get() 
        item['top_speed'] = response.css('.v td+ td font table:nth-child(1) tr:nth-child(2) b::text').get()   
        item['n_gears'] = response.css('.v .v table+ table tr:nth-child(25) td p font b::text').get()
        item['acc_0_30'] = response.css('.v table:nth-child(8) tr:nth-child(1) b::text').get()
        item['acc_0_40'] = response.css('.v table:nth-child(8) tr:nth-child(2) b::text').get() 
        item['acc_0_50'] = response.css('.v table:nth-child(8) tr:nth-child(3) b::text').get()  
        item['acc_0_60'] = response.css('.v table:nth-child(8) tr:nth-child(4) b::text').get() 
        item['acc_0_70'] = response.css('.v table:nth-child(8) tr:nth-child(5) b::text').get() 
        item['acc_0_80'] = response.css('.v table:nth-child(8) tr:nth-child(6) b::text').get()
        item['acc_0_90'] = response.css('.v table:nth-child(8) tr:nth-child(7) b::text').get() 
        item['acc_0_100'] = response.css('table:nth-child(8) tr:nth-child(8) td b::text').get()
        item['acc_0_110'] = response.css('table:nth-child(8) tr:nth-child(9) b::text').get()
        item['acc_0_120'] = response.css('table:nth-child(8) tr:nth-child(10) b::text').get() 
        item['acc_0_130'] = response.css('table:nth-child(8) tr:nth-child(11) b::text').get()
        item['acc_0_140'] = response.css('table:nth-child(8) tr:nth-child(12) b::text').get()
        item['acc_0_150'] = response.css('table:nth-child(8) tr:nth-child(13) b::text').get()
        item['acc_0_160'] = response.css('table:nth-child(8) tr:nth-child(14) b::text').get() 
        item['acc_0_170'] = response.css('table:nth-child(8) tr:nth-child(15) b::text').get()
        item['acc_0_180'] = response.css('table:nth-child(8) tr:nth-child(16) b::text').get() 
        item['acc_0_190'] = response.css('table:nth-child(8) tr:nth-child(17) b::text').get()
        item['acc_0_200'] = response.css('table:nth-child(8) tr:nth-child(18) b::text').get()
        item['acc_0_210'] = response.css('table:nth-child(8) tr:nth-child(19) b::text').get()
        item['acc_0_220'] = response.css('table:nth-child(8) tr:nth-child(20) b::text').get()
        item['acc_0_230'] = response.css('table:nth-child(8) tr:nth-child(21) b::text').get()
        item['acc_0_240'] = response.css('table:nth-child(8) tr:nth-child(22) b::text').get()
        item['acc_0_250'] = response.css('table:nth-child(8) tr:nth-child(23) b::text').get()
        item['acc_0_270'] = response.css('table:nth-child(8) tr:nth-child(24) b::text').get()
        item['acc_0_300'] = response.css('table:nth-child(8) tr:nth-child(25) b::text').get()
        item['gear4th_60_100'] = response.xpath('//font[contains(text(),"(or top gear if total number of gears <4):")]/../../../td/p/font/b/text()').get()
        item['gear4th_80_120'] = response.xpath('//font[contains(text(),"(or top gear if total number of gears <4):")]/../../../td/p/font/b/text()')[1].get()
        item['gear5th_80_120'] = response.xpath('//font[contains(text(),"80-120 km/h on Vth gear (sec):")]/../../../td/p/font/b/text()').get()
        item['gear6th_80_120'] = response.xpath('//font[contains(text(),"80-120 km/h on VIth gear (sec):")]/../../../td/p/font/b/text()').get()
        item['gear1st_top_speed'] = response.xpath('//font[text()="I:"]/../../../td/p/font/b/text()').get()
        item['gear2nd_top_speed'] = response.xpath('//font[text()="II:"]/../../../td/p/font/b/text()').get()
        item['gear3rd_top_speed'] = response.xpath('//font[text()="III:"]/../../../td/p/font/b/text()').get() 
        item['gear4th_top_speed'] = response.xpath('//font[text()="IV:"]/../../../td/p/font/b/text()').get()  
        item['gear5th_top_speed'] = response.xpath('//font[text()="V:"]/../../../td/p/font/b/text()').get()
        item['gear6th_top_speed'] = response.xpath('//font[text()="VI:"]/../../../td/p/font/b/text()').get()
        item['gear7th_top_speed'] = response.xpath('//font[text()="VII:"]/../../../td/p/font/b/text()').get()
        item['gear8th_top_speed'] = response.xpath('//font[text()="VIII:"]/../../../td/p/font/b/text()').get()
        item['gear9th_top_speed'] = response.xpath('//font[text()="IX:"]/../../../td/p/font/b/text()').get()
        item['gear10th_top_speed'] = response.xpath('//font[text()="X:"]/../../../td/p/font/b/text()').get()
        item['rpm1000_gear1st_speed'] = response.xpath('//font[text()="I:"]/../../../td/p/font/b/text()')[1].get() 
        item['rpm1000_gear2nd_speed'] = response.xpath('//font[text()="II:"]/../../../td/p/font/b/text()')[1].get() 
        item['rpm1000_gear3rd_speed'] = response.xpath('//font[text()="III:"]/../../../td/p/font/b/text()')[1].get()
        item['rpm1000_gear4th_speed'] = response.xpath('//font[text()="IV:"]/../../../td/p/font/b/text()')[1].get()
        item['rpm1000_gear5th_speed'] = response.xpath('//font[text()="V:"]/../../../td/p/font/b/text()')[1].get()
        item['rpm1000_gear6th_speed'] = response.xpath('//font[text()="VI:"]/../../../td/p/font/b/text()')[1].get()
        item['rpm1000_gear7th_speed'] = response.xpath('//font[text()="VII:"]/../../../td/p/font/b/text()')[1].get()
        item['rpm1000_gear8th_speed'] = response.xpath('//font[text()="VIII:"]/../../../td/p/font/b/text()')[1].get()
        item['rpm1000_gear9th_speed'] = response.xpath('//font[text()="IX:"]/../../../td/p/font/b/text()')[1].get()
        item['rpm1000_gear10th_speed'] = response.xpath('//font[text()="X:"]/../../../td/p/font/b/text()')[1].get()
        item['qrt_mile_time'] = response.xpath('//font[text()="0- 1/4mile (s):"]/../../../td/p/font/b/text()').get()
        item['speed_at_qrt_mile'] = response.xpath('//font[text()="speed at 1/4mile:"]/../../../td/p/font/b/text()').get()
        item['kilometer_time'] = response.xpath('//font[text()="0- 1km (s):"]/../../../td/p/font/b/text()').get()
        
        yield item
