# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class StoryPipeline(object):
    def __init__(self):
        self.res_path = "../Data/stories"

    def process_item(self, item, spider):
        with open(self.res_path + "/" + item['title']+'.json', 'a') as f:
            json.dump(dict(item), f, ensure_ascii=False)
            f.write('\n')
        return item
