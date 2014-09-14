#!flask/bin/python
from flask import Flask
from flask.ext.restplus import Api, Resource
from utils.utils import CKAN_Utils

app = Flask(__name__)
api = Api(app, version='1.0', title='ODQ API',
    description='Open Data Quality API'
)

ns = api.namespace('api', description='Open Data Quality API')

OPERATIONS = {
    'avalible_operations' : [
    '/api/',
    '/api_ckan/resource_show/<string:ckan_portal>/<string:resource_id>',
    '/api_ckan/resource_status_show/<string:ckan_portal>/<string:resource_id>',
     '/ckan_data_quality/<string:ckan_portal>/<string:resource_id>'
    ]
}


#Portals with CKAN Supported
SUPPORTED_PORTALS = {
    'uk' : { 'url': 'http://data.gov.uk' },
    'eeuu' : { 'url' : 'http://catalog.data.gov' },
    'au' : { 'url' : 'http://data.gov.au'}
}

#Portals with QA Extension Supported
SUPPORTED_QA_EXTENSION_PORTALS = {
    'uk' : {'url': 'http://data.gov.uk'}
}



def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        api.abort(404, "Todo {} doesn't exist".format(todo_id))

def abort_if_portal_is_not_supported(portal_id):
    if portal_id not in SUPPORTED_PORTALS:
        api.abort(404, "The portal '{}' isn't on the supported list".format(portal_id))    

def abort_if_qa_extension_is_not_supported(portal_id):
    if portal_id not in SUPPORTED_QA_EXTENSION_PORTALS:
        api.abort(404, "The portal '{}' isn't on the supported portals with the qa extension".format(portal_id))    




@ns.route('/api_ckan/resource_show/<string:ckan_portal>/<string:resource_id>')
@api.doc(responses={404: 'Resource not found'}, params={'ckan_portal': 'The ID of the ckan portal','resource_id': 'The id of the resource in the portal'})
class API_CKAN_getResourceDetails(Resource):
    '''Shows the ckan data resource's details'''
    @api.doc(notes='Details of a specific resource from the CKAN API ')
    def get(self,ckan_portal,resource_id):
        '''Details of a specific resource from CKAN API '''
        abort_if_portal_is_not_supported(ckan_portal)

        ckan = CKAN_Utils()
        if not ckan.isResourceInPortal(SUPPORTED_PORTALS[ckan_portal]['url'],resource_id):
            api.abort(404, "The resource {} does not exist on the portal".format(resource_id))       

        return ckan.getResourceDetails(SUPPORTED_PORTALS[ckan_portal]['url'],resource_id)


@ns.route('/api_ckan/resource_status_show/<string:ckan_portal>/<string:resource_id>')
@api.doc(responses={404: 'Resource not found'}, params={'ckan_portal': 'The ID of the ckan portal','resource_id': 'The id of the resource in the portal'})
class API_CKAN_getResourceStatusDetails(Resource):
    '''Shows the ckan status data resource's details'''
    @api.doc(notes='Details of a status resource from the CKAN API ')
    def get(self,ckan_portal,resource_id):
        '''Details of a status resource from CKAN API '''
        abort_if_portal_is_not_supported(ckan_portal)

        ckan = CKAN_Utils()
        if not ckan.isResourceInPortal(SUPPORTED_PORTALS[ckan_portal]['url'],resource_id):
            api.abort(404, "The resource {} does not exist on the portal".format(resource_id))       

        return ckan.getResourceStatusDetails(SUPPORTED_PORTALS[ckan_portal]['url'],resource_id)

@ns.route('/')
class Operations(Resource):
    '''Shows a list of all operations, and lets you POST to add new'''
    @api.doc(notes='Available Operations of the API')
    def get(self):
        '''List all available Operations of the Open Data Quality API'''
        return OPERATIONS


@ns.route('/ckan_data_quality/<string:ckan_portal>/<string:resource_id>')
@api.doc(responses={404: 'Resource not found'}, params={'ckan_portal': 'The ID of the ckan portal','resource_id': 'The id of the resource in the portal'})
class CkanDataQuality(Resource):
    '''Shows the ckan data quality score of resource'''
    def get(self,ckan_portal,resource_id):
        '''Score of a specific resource from CKAN QA Extension'''
        abort_if_qa_extension_is_not_supported(ckan_portal)

        ckan = CKAN_Utils()
        if not ckan.isResourceInPortal(SUPPORTED_QA_EXTENSION_PORTALS[ckan_portal]['url'],resource_id):
            api.abort(404, "The resource {} does not exist on the portal".format(resource_id))       

        return ckan.get_ckan_data_quality(SUPPORTED_QA_EXTENSION_PORTALS[ckan_portal]['url'],resource_id)



if __name__ == '__main__':
    app.run(debug=True)