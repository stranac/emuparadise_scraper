# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.python import to_bytes

import hashlib
import os


class ResponseExtFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        if response:
            media_guid = hashlib.sha1(to_bytes(response.url)).hexdigest()
            media_ext = os.path.splitext(response.url)[1]
            return f'{media_guid}.{media_ext}'
