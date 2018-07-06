# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return Request(item['image_url'])

    # def item_completed(self, results, item, info):
    #     if isinstance(item, dict) or self.images_result_field in item.fields:
    #         item[self.images_result_field] = [x for ok, x in results if ok]
    #     return item



