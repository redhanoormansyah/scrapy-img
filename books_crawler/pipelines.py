# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import re

class BooksCrawlerPipeline(object):
    def process_item(self, item, spider):
        os.chdir('D:/zona scraping/scrapy-img/foobar')

        if item['images'][0]['path']:
            new_image_name = item['title'][0] +'.jpg'
            new_image_name = re.sub('[\/:<>*?"|]', '', new_image_name)
            new_image_path = 'full/'+ new_image_name

            os.rename(item['images'][0]['path'], new_image_path)

