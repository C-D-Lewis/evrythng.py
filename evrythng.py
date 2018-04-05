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

  def thng(self, id=None):
    return build_evrythng_resource(self, 'thngs', id)

  def product(self, id=None):
    return build_evrythng_resource(self, 'products', id)


class Resource():
  def __init__(self, parent_scope, resource_path, id=None):
    self.parent_scope = parent_scope
    self.resource_path = resource_path
    if id is not None:
      self.id = id

  def create(self, payload):
    return build_evrythng_request(self, 'post', payload)

  def read(self):
    return build_evrythng_request(self, 'get')

  def update(self, payload):
    return build_evrythng_request(self, 'put', payload)

  def delete(self):
    return build_evrythng_resource(self, 'delete')


def build_evrythng_resource(parent_scope, resource_path, id=None):
  if id is not None:
    return Resource(parent_scope, resource_path, id)
  else:
    return Resource(parent_scope, resource_path)


def build_evrythng_request(resource, method, body={}):
  headers = { 'Authorization': resource.parent_scope.api_key }
  full_url = resource.parent_scope.api_url + '/' + resource.resource_path

  if method == 'post':
    headers['Content-Type'] = 'application/json'
    result = requests.post(full_url, headers=headers, data=json.dumps(body)).json()
  if method == 'get':
    result = requests.get(full_url, headers=headers).json()
  if method == 'put':
    if not resource.id:
      raise Exception('ID must be supplied for update')

    headers['Content-Type'] = 'application/json'
    result = requests.put(full_url + '/' + resource.id, headers=headers, data=json.dumps(body)).json()
  if method == 'delete':
    if not resource.id:
      raise Exception('ID must be supplied for delete')

    result = requests.delete(full_url + '/' + resource.id, headers=headers)
    
  if 'errors' in result:
    raise EvrythngError(result)

  return result