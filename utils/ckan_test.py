import random
import unittest
import json
from utils import CKAN_Utils

class TestSequenceFunctions(unittest.TestCase):

    ckan = CKAN_Utils()
    # PORTALES
    portal_UK_url = "http://data.gov.uk"
    portal_EEUU_url= "http://catalog.data.gov"
    portal_AU_url = "http://data.gov.au/"


    def setUp(self):
        self.seq = range(10)
        print ("Setting Up ")

        self.portal_url = self.portal_UK_url
        self.resource_id_with_qa = "ea05ccea-543c-433b-a082-16f73cbf90e3"
        self.resource_id_without_qa = "d55bb6a8-ba15-4bba-8896-218bd1bfacf6"

        print ("Using API from portal " + self.portal_url)
        print ("Using API version '" + self.ckan.api_version +"'")
        

    def test_resource_in_portal(self):
        # Makes sure the resource is in the portal
        self.assertTrue(self.ckan.isResourceInPortal(self.portal_url, self.resource_id_with_qa))

    def test_resource_details(self):
        # Makes sure the response from the call getResourceDetails using the CKAN API is succesful
        json_details = self.ckan.getResourceDetails(self.portal_url, self.resource_id_with_qa);
        print ""
        print json.dumps(json_details, indent=4, sort_keys=True)
        self.assertTrue(json_details['success'])

    def test_resource_status_details(self):
        # Makes sure the response from the call getResourceDetails using the CKAN API is succesful
        print ("")
        json_status_details = self.ckan.getResourceStatusDetails(self.portal_url, self.resource_id_with_qa);
        print json.dumps(json_status_details, indent=4, sort_keys=True)
        self.assertTrue(json_status_details['success'])

    def test_valid_ckan_data_quality(self):
        # Makes sure the response from the call get_ckan_data_quality for resource with QA using the CKAN API is succesful
        print ("")
        json_ckan_quality = self.ckan.get_ckan_data_quality(self.portal_url, self.resource_id_with_qa);
        print json.dumps(json_ckan_quality, indent=4, sort_keys=True)
        self.assertTrue(json_ckan_quality['success'])
    
    def test_invalid_ckan_data_quality(self):
        # Makes sure the response from the call get_ckan_data_quality for a resource without using the CKAN API is succesful
        print ("")
        json_ckan_quality = self.ckan.get_ckan_data_quality(self.portal_url, self.resource_id_without_qa);
        print json.dumps(json_ckan_quality, indent=4, sort_keys=True)
        self.assertFalse(json_ckan_quality['success'])
    
    
class develop(unittest.TestCase):

    ckan = CKAN_Utils()
    # PORTALES
    portal_UK_url = "http://data.gov.uk"
    portal_EEUU_url= "http://catalog.data.gov"
    portal_AU_url = "http://data.gov.au/"


    def setUp(self):
        self.seq = range(10)
        print ("Setting Up ")

        self.portal_url = self.portal_UK_url
        self.resource_id_with_qa = "ea05ccea-543c-433b-a082-16f73cbf90e3"
        self.resource_id_without_qa = "d55bb6a8-ba15-4bba-8896-218bd1bfacf6"

        print ("Using API from portal " + self.portal_url)
        print ("Using API version '" + self.ckan.api_version +"'")

    def test_invalid_ckan_data_quality(self):
        # Makes sure the response from the call get_ckan_data_quality for a resource without using the CKAN API is succesful
        print ("")
        json_ckan_quality = self.ckan.get_ckan_data_quality(self.portal_url, self.resource_id_without_qa);
        print json.dumps(json_ckan_quality, indent=4, sort_keys=True)
        self.assertFalse(json_ckan_quality['success'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #suite = unittest.TestSuite()
    #suite.addTest(WidgetTestCase('test_invalid_ckan_data_quality')
    #unittest.TextTestRunner(verbosity=2).run(suite)