import unittest
from rest-server.utils.utils import CKAN_Utils


test = CKAN_Utils()
resource_id = "ea05ccea-543c-433b-a082-16f73cbf90e3"
print ("Using API from portal " + test.portal_url)
print ("Using API version '" + test.api_version +"'")
#resource_id = (raw_input('What is the resource id? '))

assert(test.ckan_data_quality(test.portal_url,resource_id))

print "FIN"