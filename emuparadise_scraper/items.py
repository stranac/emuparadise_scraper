# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Compose, MapCompose


class ROMItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    file_urls = scrapy.Field()


def clean_title(title):
    """Remove leading "Download " from the link text."""
    return title[9:]


def absolute_url(url, loader_context):
    return loader_context['response'].urljoin(url)


class ROMLoader(ItemLoader):
    default_item_class = ROMItem
    url_out = TakeFirst()
    title_out = Compose(TakeFirst(), clean_title)
    file_urls_out = MapCompose(absolute_url)
