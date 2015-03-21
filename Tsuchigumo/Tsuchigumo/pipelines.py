# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import re
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
from logic.Targets import Targets
class TsuchigumoPipeline(object):
    
    def __init__(self):
    	connection = pymongo.Connection(settings['MONGODB_SERVER'],settings['MONGODB_PORT'])
    	db = connection[settings['MONGODB_DB']]
    	self.collection = db[settings['MONGODB_COLLECTION']] 
    	if(self.collection):
    		self.collection.drop()
    
    def process_item(self, item, spider):
    	oTarget = Targets()
        name = item['name'][0].split('-')[0].strip()
    	contact = ''
    	if item['direction'][7].strip() != '':
    		contact  = item['direction'][7]
    	
    	item['direction'] = item['direction'][2].split(':')[1].strip()
    	


    	
    	
        category = oTarget.remove_accents(item['category'][0].split(':')[1].strip().split(' ')[1].lower().unicode(''))
        

        
      	
      		


        for course in item['courses']:
            self.collection.save({'name':name,'contact':contact,'category':category,'course':course})
    

