# -*- coding: utf-8 -*-

# Scrapy settings for linkedin_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'linkedin_spider'

SPIDER_MODULES = ['linkedin_spider.spiders']
NEWSPIDER_MODULE = 'linkedin_spider.spiders'
#############################

#############################
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS = 2
CONCURRENT_REQUESTS_PER_IP =2
DOWNLOAD_DELAY = 0.5
CONCURRENT_REQUESTS_PER_DOMAIN = 2
# DNSCACHE_ENABLED =False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'linkedin_spider (+http://www.yourdomain.com)'
