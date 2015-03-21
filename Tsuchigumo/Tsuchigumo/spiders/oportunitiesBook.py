# -*- coding: utf-8 -*-
import scrapy


class OportunitiesbookSpider(scrapy.Spider):
    name = "oportunitiesBook"
    allowed_domains = ["http://loeu.opsu.gob.ve/vistas/instituciones/busquedaRegiones.php"]
    start_urls = (
        'http://www.http://loeu.opsu.gob.ve/vistas/instituciones/busquedaRegiones.php/',
    )

    def parse(self, response):
        pass
