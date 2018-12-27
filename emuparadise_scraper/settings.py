# -*- coding: utf-8 -*-

# Scrapy settings for emuparadise_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'emuparadise_scraper'

SPIDER_MODULES = ['emuparadise_scraper.spiders']
NEWSPIDER_MODULE = 'emuparadise_scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Referer': 'https://www.emuparadise.me/roms/get-download.php',
    'Cookie': 'downloadcaptcha=1',
}
# Stop the CookiesMiddleware from messing with our cookies
COOKIES_ENABLED = False

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'emuparadise_scraper.pipelines.ResponseExtFilesPipeline': 300,
}
MEDIA_ALLOW_REDIRECTS = True
FILES_STORE = 'ROMs'

RETRY_TIMES = 30
