import unicodedata
from scrapy.conf import settings
class Targets(object):

	
	target_list = []
	def __init__(self):
		
		self.createListOfRequest()

	def createListOfRequest(self):
		for i in range(1,settings['MAX_URL']):
			word = str(i) + ''
			if (len(word)< 10):
				for j in range(len(word),10):
					word = "0" + word
			self.target_list.append('http://loeu.opsu.gob.ve/vistas/instituciones/consultar.php?id='+word)

	def getListOfTargets(self):
		return self.target_list		


	def remove_accents(self,input_str):
		nkfd_form = unicodedata.normalize('NFKD', input_str)
		return "".join([c for c in nkfd_form if not unicodedata.combining(c)])