#!flask/bin/python
from flask import Flask
from flask.ext.restplus import Api, Resource, fields
from utils.utils import CKAN_Utils

app = Flask(__name__)
api = Api(app, version='1.0', title='ODQ API',
    description='Open Data Quality API'
)

ns = api.namespace('api', description='Open Data Quality API')

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

#Portals with QA Extension Supported
SUPPORTED_PORTALS = {
    'uk' : {'url': 'http://data.gov.uk'}
}



todo_fields = api.model('Todo', {
    'task': fields.String(required=True, description='The task details')
})


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        api.abort(404, "Todo {} doesn't exist".format(todo_id))

def abort_if_portal_is_not_supported(portal_id):
    if portal_id not in SUPPORTED_PORTALS:
        api.abort(404, "The portal '{}' isn't on the supported list".format(portal_id))        

parser = api.parser()
parser.add_argument('task', type=str, required=True, help='The task details')


@ns.route('/<string:todo_id>')
@api.doc(responses={404: 'Todo not found'}, params={'todo_id': 'The Todo ID'})
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @api.doc(notes='todo_id should be in {0}'.format(', '.join(TODOS.keys())))
    @api.marshal_with(todo_fields)
    def get(self, todo_id):
        '''Fetch a given resource'''
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]




@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @api.marshal_with(todo_fields, as_list=True)
    def get(self):
        '''List all todos'''
        return TODOS


@ns.route('/ckan_data_quality/<string:ckan_portal>/<string:resource_id>')
@api.doc(responses={404: 'Resource not found'}, params={'ckan_portal': 'The ID of the ckan portal','resource_id': 'The id of the resource in the portal'})
class CkanDataQuality(Resource):
    '''Shows the ckan data quality score of resource'''
    def get(self,ckan_portal,resource_id):
        '''Score of a specific resource from CKAN QA Extension'''
        abort_if_portal_is_not_supported(ckan_portal)

        ckan = CKAN_Utils()
        if not ckan.isResourceInPortal(SUPPORTED_PORTALS[ckan_portal]['url'],resource_id):
            api.abort(404, "The resource {} does not exist on the portal".format(resource_id))       

        return ckan.ckan_data_quality(SUPPORTED_PORTALS[ckan_portal]['url'],resource_id)



if __name__ == '__main__':
    app.run(debug=True)