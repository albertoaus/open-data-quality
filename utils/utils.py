import requests
import json


class CKAN_Utils():

	api_version = "/api/3/action/"
	get_resource_status_show = "resource_status_show";
	get_resource_show = "resource_show"
	param_id = "?id="


	def getResourceDetails(self, ckan_portal, resource_id):
		r = requests.get(ckan_portal + self.api_version + self.get_resource_show + self.param_id + resource_id)
		if (r.status_code == requests.codes.ok):
			parsed = json.loads(r.content)
			return parsed

		return False


	def getResourceStatusDetails(self,ckan_portal,resource_id):
		r = requests.get(ckan_portal + self.api_version + self.get_resource_status_show + self.param_id + resource_id)
		if (r.status_code == requests.codes.ok):
			parsed = json.loads(r.content)
			return parsed

		return False

	def isResourceInPortal(self, ckan_portal, resource_id):
		r = requests.get(ckan_portal + self.api_version + self.get_resource_show + self.param_id + resource_id)
		if (r.status_code == requests.codes.ok):
			parsed = json.loads(r.content)
			return parsed['success']

		return False


	def get_ckan_data_quality(self, ckan_portal, resource_id):
		
		results = self.getResourceStatusDetails(ckan_portal, resource_id)['result']
		result_qa_type = []
		result_qa_errors = []
		result_qa_values = []
		json_result = {}

		if (results != False):	
			#Filtrar las task con "task_type": "qa" y "key": "status"
			for res in results :
				if(res['task_type'] == "qa" and res['key'] == "status") :
					result_qa_type.append(res)

			
			for qa_results in result_qa_type :
				 result_qa_values.append(int(qa_results['value']))
				 result_qa_errors.append(qa_results['error'])

			#Print the json result
			if result_qa_type != []:
				json_result["success"] = True
				json_result["opennes_value"] = result_qa_values
				json_result["info"] =  result_qa_errors
			else:
				json_result["success"] = False
				json_result["info"] = "Score doesn't found"

			return json_result

		return False