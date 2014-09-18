import requests
import json


class Mas_alla_5_estrellas():

	fiveStarsToAvailavility = { 
		0 : 0, # available on the Web
		1 : 0.33, # structured data
		2 : 0.67, # non-proprietary formats
		3 : 1,
		4 : 1,
		5 : 1
	}

	fiveStarsToReuse = { 
		0 : 0, 
		1 : 0, 
		2 : 0, 
		3 : 0,
		4 : 0.5,
		5 : 1
	}


	def getAvailability(self, five_stars_Score):
		return ({'Mas_alla_5_estrellas_disponibilidad' : str(self.fiveStarsToAvailavility[five_stars_Score]), 'success' : True})

	def getReuse(self, five_stars_Score):
		return ({'Mas_alla_5_estrellas_reutilizacion' : str(self.fiveStarsToReuse[five_stars_Score]), 'success' : True})

	def getGranularity(self, number_of_levels, resource_level):
		return ({'Mas_alla_5_estrellas_granularidad' : (float(number_of_levels - resource_level + 1)  / number_of_levels), 'success' : True})
