# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

from linkedin_spider.items import LinkedinSpiderItem
class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    download_delay = 2
    allowed_domains = ["linkedin.com"]
    handle_httpstatus_list=[999]
    start_urls = (
        'https://www.linkedin.com/jobs/view/270970043/?refId=2c745db4-5cfe-459c-ac45-8b253acc867b&trk=d_flagship3_job_home',
    )

    def parse(self, response):
        print (response.status)
        item=LinkedinSpiderItem()
        if response.status==999:
            print ("using selenium to open the site")
            print (response.url)
            browser =webdriver.PhantomJS("phantom/bin/phantomjs")
            excpected_fields=["Industry","Experience"]
            browser.get(response.url)
            for key in excpected_fields:
                try:
                    target=browser.find_element_by_xpath("//*[text()='{0}']/following::*[1]".format(key))
                    item[key]=(target.text.encode("utf-8"))
                except:
                    print("could not find element{0}".format(key))

            yield  item
    # define items for export as json