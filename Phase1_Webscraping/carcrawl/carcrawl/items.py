# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarDataTechItem(scrapy.Item):
    # define the fields for your item here like:
    car_id = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    generation = scrapy.Field()
    prod_start = scrapy.Field()
    prod_end = scrapy.Field()
    cylinders = scrapy.Field()
    transmission = scrapy.Field()
    drive_wheel = scrapy.Field()
    power = scrapy.Field()
    max_power_rpm = scrapy.Field()
    torque = scrapy.Field()
    max_torque_rpm = scrapy.Field()
    turbo = scrapy.Field()
    eng_capacity = scrapy.Field()
    fuel = scrapy.Field()
    top_speed = scrapy.Field()
    acc_0_100 = scrapy.Field()
    gear_1 = scrapy.Field()
    gear_2 = scrapy.Field()
    gear_3 = scrapy.Field()
    gear_4 = scrapy.Field()
    gear_5 = scrapy.Field()
    gear_6 = scrapy.Field()
    gear_7 = scrapy.Field()
    gear_8 = scrapy.Field()
    gear_9 = scrapy.Field()
    gear_r = scrapy.Field()
    gear_final = scrapy.Field()
    front_tire = scrapy.Field()
    rear_tire = scrapy.Field()
    weight = scrapy.Field()
    
class CarDataSizesItem(scrapy.Item):
    # define the fields for your item here like:
    car_id = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    weight = scrapy.Field()
    height = scrapy.Field()
    width = scrapy.Field()
    length = scrapy.Field()
    wheelbase = scrapy.Field()