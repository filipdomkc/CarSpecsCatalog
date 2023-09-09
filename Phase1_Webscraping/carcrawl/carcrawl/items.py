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
    
class CarInfoItem(scrapy.Item):
    # define the fields for your item here like:
    brand = scrapy.Field()
    generation = scrapy.Field()
    model = scrapy.Field()
    drive_wheel = scrapy.Field()
    power_kw = scrapy.Field()
    power_hp = scrapy.Field()
    torque_nm = scrapy.Field()
    cylinders = scrapy.Field()
    eng_config = scrapy.Field()
    eng_capacity = scrapy.Field()
    drag_coefficient = scrapy.Field()
    transmission = scrapy.Field()

class AutocatalogItem(scrapy.Item):
    # define the fields for your item here like:
    car_id = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    generation = scrapy.Field()
    year = scrapy.Field()
    engine_type = scrapy.Field()
    power = scrapy.Field()
    cyl_align = scrapy.Field()
    eng_capacity = scrapy.Field()
    transmission_type = scrapy.Field()
    drive_wheel = scrapy.Field()
    top_speed = scrapy.Field()
    n_gears = scrapy.Field()
    acc_0_30 = scrapy.Field()
    acc_0_40 = scrapy.Field()
    acc_0_50 = scrapy.Field()
    acc_0_60 = scrapy.Field()
    acc_0_70 = scrapy.Field()
    acc_0_80 = scrapy.Field()
    acc_0_90 = scrapy.Field()
    acc_0_100 = scrapy.Field()
    acc_0_110 = scrapy.Field()
    acc_0_120 = scrapy.Field()
    acc_0_130 = scrapy.Field()
    acc_0_140 = scrapy.Field()
    acc_0_150 = scrapy.Field()
    acc_0_160 = scrapy.Field()
    acc_0_170 = scrapy.Field()
    acc_0_180 = scrapy.Field()
    acc_0_190 = scrapy.Field()
    acc_0_200 = scrapy.Field()
    acc_0_210 = scrapy.Field()
    acc_0_220 = scrapy.Field()
    acc_0_230 = scrapy.Field()
    acc_0_240 = scrapy.Field()
    acc_0_250 = scrapy.Field()
    acc_0_270 = scrapy.Field()
    acc_0_300 = scrapy.Field()
    gear4th_60_100 = scrapy.Field()
    gear4th_80_120 = scrapy.Field()
    gear5th_80_120 = scrapy.Field()
    gear6th_80_120 = scrapy.Field()
    gear1st_top_speed = scrapy.Field()
    gear2nd_top_speed = scrapy.Field()
    gear3rd_top_speed = scrapy.Field()
    gear4th_top_speed = scrapy.Field()
    gear5th_top_speed = scrapy.Field()
    gear6th_top_speed = scrapy.Field()
    gear7th_top_speed = scrapy.Field()
    gear8th_top_speed = scrapy.Field()
    gear9th_top_speed = scrapy.Field()
    gear10th_top_speed = scrapy.Field()
    rpm1000_gear1st_speed = scrapy.Field()
    rpm1000_gear2nd_speed = scrapy.Field()
    rpm1000_gear3rd_speed = scrapy.Field()
    rpm1000_gear4th_speed = scrapy.Field()
    rpm1000_gear5th_speed = scrapy.Field()
    rpm1000_gear6th_speed = scrapy.Field()
    rpm1000_gear7th_speed = scrapy.Field()
    rpm1000_gear8th_speed = scrapy.Field()
    rpm1000_gear9th_speed = scrapy.Field()
    rpm1000_gear10th_speed = scrapy.Field()
    qrt_mile_time = scrapy.Field()
    speed_at_qrt_mile = scrapy.Field()
    kilometer_time = scrapy.Field()
