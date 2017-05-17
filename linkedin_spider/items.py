# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LinkedinSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    job_title = scrapy.Field() #done
    # company_name = scrapy.Field()
    Industry = scrapy.Field() #done
    Experience = scrapy.Field()
    job_Employment_type = scrapy.Field()
    job_function = scrapy.Field()


    pass
