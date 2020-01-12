# -*- coding: utf-8 -*-
import scrapy
from zhihuScrapy.items import PictureBookItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
 #   allowed_domains = ['www.zhihu.com']
    start_urls = ['https://huiben.iboniao.com/?cat=3']

    def parse(self,response):
        pageNumbers = response.xpath('//a[@class="page-numbers"]/text()').extract()
        maxPageNumer = pageNumbers[len(pageNumbers)-1]
        for index in range(1,int(maxPageNumer)):
            yield scrapy.Request('https://huiben.iboniao.com/?cat=3&paged={}'.format(index),callback = self.parsePage)

    def parsePage(self,response):
        list = response.xpath('//span[@class="entry-more"]/a/@href').extract()
        for url in list:
            yield scrapy.Request(url,callback = self.parsePictureBook)
    
    def parsePictureBook(self, response):
        item = PictureBookItem()

        nameStr = response.xpath(u"//div/span[contains(text(),'名称')]/text()").extract()[0]
        item['name'] = nameStr.split(u'：')[1]
        
        authorNameStr = response.xpath(u"//div/span[contains(text(),'作者')]/text()").extract()[0]
        item['author'] = authorNameStr.split(u"：")[1]
        
        publisherNameStr = response.xpath(u"//div/span[contains(text(),'出版社')]/text()").extract()[0]
        item['publisher'] = publisherNameStr.split(u'：')[1]

        isbnStr = response.xpath(u"//div/span[contains(text(),'ISBN')]/text()").extract()[0]
        item['isbn'] = isbnStr.split(u'：')[1]

        priceStr = response.xpath(u"//div/span[contains(text(),'单价')]/text()").extract()[0]
        item['price'] = priceStr.split(u'：')[1]

        serialStr = response.xpath(u"//div/span[contains(text(),'系列')]/text()").extract()[0]
        item['serial'] = serialStr.split(u'：')[1]

        languageStr = response.xpath(u"//div/span[contains(text(),'语言')]/text()").extract()[0]
        item['language'] = languageStr.split(u'：')[1]

        images = response.xpath('//p/img/@src').extract()
        item['images'] = images;

        item['storyText'] = response.xpath('//div[@style="width: 95%;margin: 20px 0;"]/text()').extract()

        yield item