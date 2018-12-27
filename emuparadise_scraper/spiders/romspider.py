# -*- coding: utf-8 -*-
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

from emuparadise_scraper.items import ROMLoader


class ROMSpider(CrawlSpider):
    name = 'emuparadise'
    allowed_domains = ['emuparadise.me']
    start_urls = [
        'https://www.emuparadise.me/Nintendo_Entertainment_System_ROMs/List-All-Titles/13',
        'https://www.emuparadise.me/Atari_2600_ROMs/List-All-Titles/49',
    ]

    rules = [
        Rule(LinkExtractor(restrict_css=['a.index.gamelist'])),
        Rule(LinkExtractor(allow=[r'/\d+-download']), callback='parse_item'),
        Rule(LinkExtractor(allow=[r'/roms/get-download'])),
    ]

    def parse_item(self, response):
        loader = ROMLoader(response=response)
        loader.add_value('url', response.url)
        loader.add_css('title', 'a#download-link::text')
        loader.add_css('file_urls', 'a#download-link::attr(href)')
        yield loader.load_item()
