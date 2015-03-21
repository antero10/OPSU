

BOT_NAME = 'Tsuchigumo'

SPIDER_MODULES = ['Tsuchigumo.spiders']
NEWSPIDER_MODULE = 'Tsuchigumo.spiders'
ITEM_PIPELINES = {
	'Tsuchigumo.pipelines.TsuchigumoPipeline':300
}
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'OPSUProject'
MONGODB_COLLECTION = 'data'
MAX_URL = 585