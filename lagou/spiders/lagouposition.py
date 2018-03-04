# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lagou.items import LagouItem


class LagoupositionSpider(CrawlSpider):
    name = 'lagouposition'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*')),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = LagouItem()
        item['position_name'] = response.xpath('//div[@class="job-name"]//span[@class="name"]/text()').extract()[0]
        # 公司名
        item['company'] = response.xpath('//div[@class="company"]/text()').extract()[0]
        # 薪水
        item['salary'] = response.xpath('//dd[@class="job_request"]//span[1]/text()').extract()[0]
        # 经验
        item['experience'] = response.xpath('//dd[@class="job_request"]//span[3]/text()').extract()[0]
        # 学历
        item['education'] = response.xpath('//dd[@class="job_request"]//span[4]/text()').extract()[0]
        # 工作地点
        item['location'] = response.xpath('//input[@name="positionAddress"]/@value').extract()[0]

        yield item

