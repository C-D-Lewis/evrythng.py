import json
import requests

class EvrythngError(Exception):
    def __init__(self, message):
        self.message = message


class Scope():
    def __init__(self, api_key):
        self.api_url = 'https://api.evrythng.com'
        self.api_key = api_key


class Operator(Scope):
    def __init__(self, api_key):
        Scope.__init__(self, api_key)

    def project(self, id=None):
        return CRUDResource(self, 'projects', id)

        # TODO: applications

    def thng(self, id=None):
        return ThngResource(self, id)

        # TODO: properties

    def product(self, id=None):
        return CRUDResource(self, 'products', id)

        # TODO: properties

    def collection(self, id=None):
        return CRUDResource(self, 'collections', id)

    def place(self, id=None):
        return CRUDResource(self, 'places', id)

    def action_type(self, id=None):
        return CRUDResource(self, 'actions', id)

    # TODO: actions

    def application_user(self, id=None):
        return CRUDResource(self, 'users', id)


# TODO: application scope
    # Create application users


# TODO: trusted app scope


# TODO: application user scope


class Device(Scope):
    def __init__(self, id, api_key):
        Scope.__init__(self, api_key)
        self.parent_scope = self
        self.resource_path = 'thngs'
        self.id = id

    def read(self):
        return _evrythng_request(self, 'get')

    def update(self, payload):
        return _evrythng_request(self, 'put', payload)


class CRUDResource():
    def __init__(self, parent_scope, resource_path, id=None):
        self.parent_scope = parent_scope
        self.resource_path = resource_path
        if id is not None:
            self.id = id

    def create(self, payload):
        return _evrythng_request(self, 'post', payload)

    def read(self):
        return _evrythng_request(self, 'get')

    def update(self, payload):
        return _evrythng_request(self, 'put', payload)

    def delete(self):
        return _evrythng_request(self, 'delete')


class ThngResource(CRUDResource):
    def __init__(self, parent_scope, id=None):
        CRUDResource.__init__(self, parent_scope, 'thngs', id)

    def auth(self):
        if not self.id:
            raise Exception('ID must be supplied')
        self.resource_path = 'auth/evrythng/thngs'
        return _evrythng_request(self, 'post', { 'thngId': self.id })


def _evrythng_request(resource, method, body={}):
    headers = { 'Authorization': resource.parent_scope.api_key }
    full_url = resource.parent_scope.api_url + '/' + resource.resource_path

    if method == 'post':
        headers['Content-Type'] = 'application/json'
        result = requests.post(full_url, headers=headers, data=json.dumps(body)).json()
    if method == 'get':
        if hasattr(resource, 'id'):
            full_url = full_url + '/' + resource.id
        result = requests.get(full_url, headers=headers).json()
    if method == 'put':
        if not resource.id:
            raise Exception('ID must be supplied')
        headers['Content-Type'] = 'application/json'
        result = requests.put(full_url + '/' + resource.id, headers=headers, data=json.dumps(body)).json()
    if method == 'delete':
        if not resource.id:
            raise Exception('ID must be supplied')
        result = requests.delete(full_url + '/' + resource.id, headers=headers)

    if 'errors' in result:
        raise EvrythngError(result)

    return result