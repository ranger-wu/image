# -*- coding: utf-8 -*-
import scrapy
from image.items import ImageItem


class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['www.xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']

    def parse(self, response):
        # name_xpath =('.//span[@class="price"]/text()')
        # name =response.xpath(name_xpath).extract()
        # url_xpath =('//a[@target="_blank"]/img/@src')
        # url= response.xpath(url_xpath).extract()
        item = ImageItem()
        urls = response.xpath('//a[@target="_blank"]/img/@src').extract()

        for i in urls:
            url = 'http://www.xiaohuar.com'+i
            item['image_url'] = url
            yield item


        # item['name'] = name
        # scrapy.item['image_urls'] = image_urls



'''
#  如何脱坑: ①这里url路径最初选取的是src相对路径,那么发现通过html打开连接会找不到图片
说明图片的URL路径错误! 
         ②在pipeline 里:  'def get_media_requests(self, item, info):'
                                 return Request(item['image_url'])
          这里出错:因为从爬虫image   yiled推送过来的数据是一条                       
一条推过来的,不是一个列表所以不需要进行遍历列表!
        ③ pipeline里继承的对象如果是文本字符串类的可以默认 object,如果是图片需要
        导入框架内的images pipeline
'''