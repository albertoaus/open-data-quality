import requests
import json


class CKAN_Utils():

	# PORTALES
	portal_UK_url = "http://data.gov.uk"
	portal_EEUU_url= "http://catalog.data.gov"
	portal_AU_url = "http://data.gov.au/"

	portal_url = portal_UK_url
	api_version = "/api/3/action/"
	get_resource_status_show = "resource_status_show";
	get_resource_show = "resource_show"
	param_id = "?id="


	def getResourceDetails(self, ckan_portal, resource_id):
		r = requests.get(ckan_portal + self.api_version + self.get_resource_show + self.param_id + resource_id)

		parsed = json.loads(r.content)

		return parsed

	def getResourceStatusDetails(self,ckan_portal,resource_id):
		r = requests.get(ckan_portal + self.api_version + self.get_resource_status_show + self.param_id + resource_id)
		#print r.status_code
		#print r.headers

		parsed = json.loads(r.content)

		#print json.dumps(parsed, indent=4, sort_keys=True)

		return parsed

	def isResourceInPortal(self, ckan_portal, resource_id):
		r = requests.get(ckan_portal + self.api_version + self.get_resource_show + self.param_id + resource_id)

		parsed = json.loads(r.content)

		return parsed['success']


	def ckan_data_quality(self, ckan_portal, resource_id):
		
		#Anadir antes resource_show --> openness_score:   ,openness_score_reason   Si existe devolver este, 
		# sino devolver el de la task
		# sino existe el otro devolver No hay datos
		
		results = self.getResourceStatusDetails(ckan_portal, resource_id)['result']
		result_qa_type = []
		json_values = []

		#Filtrar las task con "task_type": "qa" y "key": "status"
		for res in results :
			if(res['task_type'] == "qa" and res['key'] == "status") :
				#print json.dumps(res, indent=4, sort_keys=True)
				result_qa_type.append(res)

		#Imprimir el value del opennes del recurso
		for qa_results in result_qa_type :
			json_values.append({"Opennes value": int(qa_results['value'])})
			json_values.append({"Info": qa_results['error']})

        #Si el retornos es vacio --> No ha encontrado el score

		return json_values

		



#test = Utils()
#resource_id = "ea05ccea-543c-433b-a082-16f73cbf90e3"
#print ("Using API from portal " + test.portal_url)
#print ("Using API version '" + test.api_version +"'")
#resource_id = (raw_input('What is the resource id? '))

#print test.ckan_data_quality(test.portal_url,resource_id)

#print "FIN"