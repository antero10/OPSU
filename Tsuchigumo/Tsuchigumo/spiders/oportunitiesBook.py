# -*- coding: utf-8 -*-
import scrapy

from Tsuchigumo.items import TsuchigumoItem

from ..logic.Targets import Targets

class OportunitiesbookSpider(scrapy.Spider):
    name = "oportunitiesBook"
    allowed_domains = ["oeu.opsu.gob.ve"]
    start_urls = []

    def __init__(self):
    	oTarget = Targets()
    	self.start_urls = oTarget.getListOfTargets()


    def parse(self, response):
    	item = TsuchigumoItem()
        item['name']= response.selector.xpath('//span[@class="texgris"]/text()').extract()
        item['courses'] =response.selector.xpath('//table[@bgcolor="#C0C0C0" and @width="100%" and @border="0" and @cellpadding ="5" and @cellspacing="1"]/tbody/tr/td/table/tbody/tr[@class = "tb_celda_impar" or @class = "tb_celda_par"]/td[2]/a/text()').extract()
        item['category'] = response.selector.xpath('//span[@class="texrojo"]/text()').extract()
        item['direction'] = response.selector.xpath('//table[@id = "tabla_contenido"]/tbody/tr[5]/td/table/tbody/tr[1]/td/text()').extract()
        return item
 

