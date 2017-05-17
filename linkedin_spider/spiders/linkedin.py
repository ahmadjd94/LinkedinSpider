# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

from linkedin_spider.items import LinkedinSpiderItem
class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_START_DELAY = 10
    allowed_domains = ["linkedin.com"]
    handle_httpstatus_list=[999] # without this line the crawler would stop
    # working since it ignores all the non 200 responses
    start_urls = (

        'https://www.linkedin.com/jobs/management-jobs/',
    )

    def init_driver(self):
        return webdriver.PhantomJS("phantom/bin/phantomjs")

    def parse(self, response):
        print (response.status)
        # if response.status==999:
        # print ("using selenium to open the site")
        print (response.url)

        # browser = self.init_driver()
        # browser.get(response.url)
        # browser.save_screenshot('test.png')
        #### testing xpath for finding anchor page elements####
        # test= browser.find_elements_by_xpath("//a")
        # for i in  test:
        #     print (i.get_attribute("href"))
        # print (response.body)
        # scrapper=scrapy.Selector(response)
        try:
            # links=browser.find_elements_by_xpath("//a[@class='job-title-link']")
            f=open("dumb.html",'w+')
            f.writelines(response.body)
            f.close()
            links=response.xpath("//a[@class='job-title-link']").extract()
            print(response.body)
            print(type(links),len(links))
            targets=[]
            for i in links:
                targets.append(i)
                print (i)
        except:
            print ("error while fetching links ")
        # if targets:
        #     for target_page in targets:
        #         yield scrapy.Request(target_page,callback=self.traverse_page)


    # def traverse_page(self,response):
    #     item=LinkedinSpiderItem()
    #     print ("inside traverse pages")
    #     if response.status==999:
    #         browser= self.init_driver()
    #         browser.get(response.url)
    #         excpected_fields=["Industry","Experience"]
    #         for key in excpected_fields:
    #             try:
    #                 target=browser.find_element_by_xpath("//*[text()='{0}']/following::*[1]".format(key))
    #                 item[key]=(target.text.encode("utf-8"))
    #             except:
    #                 print("could not find element{0}".format(key))
    #
    #     yield  item
    #     # define items for export as json