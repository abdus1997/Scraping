# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags
from w3lib.html import replace_escape_chars

def remove_quoutations(value):
    return value.replace(u"\u201d",'').replace(u"\u201c",'').replace(u"\u2019",'').replace(u"\u2026",'')

class GoodReadsItem(scrapy.Item):
    text = scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quoutations),
        output_processor= TakeFirst()
    )
    author = scrapy.Field(
        input_processor= MapCompose(replace_escape_chars),
        output_processor= TakeFirst()
    )
    tags = scrapy.Field(
        input_processor= MapCompose(remove_tags),
        output_processor=Join(",")
    )
