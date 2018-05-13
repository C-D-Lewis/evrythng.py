import sys
import evrythng

operator = evrythng.Operator(sys.argv[1])

def run_all():
    test_operator_scope()
    test_device_scope()

    test_projects()
    test_thngs()
    test_products()
    test_collections()
    test_places()
    test_action_types()
    test_application_users()

def test_operator_scope():
    expect(operator.api_key, 'Operator to have api_key')
    expect(operator.api_url, 'Operator to have api_url')

def test_device_scope():
    thngs = operator.thng().read()
    if len(thngs) == 0:
        thng = operator.thng().create({'name': 'Test Thng'})
    else:
        thng = thngs[0]

    thng_auth = operator.thng(thng['id']).auth()
    device = evrythng.Device(thng['id'], thng_auth['thngApiKey'])
    expect(device.api_key, 'Device to have api_key')
    expect(device.api_url, 'Device to have api_url')
    expect(len(device.api_key) == 80, 'Device API Key to have length 80')

def test_projects():
    payload = {'name': 'Test Project'}
    result = operator.project().create(payload)
    project_id = result['id']
    expect(isinstance(result, dict), 'project().create() to be a dict')
    expect(isinstance(result['id'], str), 'project().create() to have \'id\'')

    result = operator.project().read()
    expect(isinstance(result, list), 'project().read() to be a list')

    result = operator.project(project_id).read()
    expect(isinstance(result, dict), 'project(id).read() to be a dict')
    expect(isinstance(result['id'], str), 'project(id).read() to have \'id\'')
    
    payload = {'tags': []}
    result = operator.project(project_id).update(payload)
    expect(isinstance(result, dict), 'project(id).update() to be a dict')
    expect(isinstance(result['tags'], list), 'project(id).update()[\'tags\'] to be a list')
    
    result = operator.project(project_id).delete()
    expect(result.status_code == 200, 'project(id).delete() status_code to be 200')

def test_thngs():
    payload = {'name': 'Test Thng'}
    result = operator.thng().create(payload)
    thng_id = result['id']
    expect(isinstance(result, dict), 'thng().create() to be a dict')
    expect(isinstance(result['id'], str), 'thng().create() to have \'id\'')

    result = operator.thng().read()
    expect(isinstance(result, list), 'thng().read() to be a list')

    result = operator.thng(thng_id).read()
    expect(isinstance(result, dict), 'thng(id).read() to be a dict')
    expect(isinstance(result['id'], str), 'thng(id).read() to have \'id\'')
    
    payload = {'tags': []}
    result = operator.thng(thng_id).update(payload)
    expect(isinstance(result, dict), 'thng(id).update() to be a dict')
    expect(isinstance(result['tags'], list), 'thng(id).update()[\'tags\'] to be a list')
    
    result = operator.thng(thng_id).delete()
    expect(result.status_code == 200, 'thng(id).delete() status_code to be 200')

def test_products():
    payload = {'name': 'Test Product'}
    result = operator.product().create(payload)
    product_id = result['id']
    expect(isinstance(result, dict), 'product().create() to be a dict')
    expect(isinstance(result['id'], str), 'product().create() to have \'id\'')
    
    result = operator.product().read()
    expect(isinstance(result, list), 'product().read() to be a list')

    result = operator.product(product_id).read()
    expect(isinstance(result, dict), 'product(id).read() to be a dict')
    expect(isinstance(result['id'], str), 'product(id).read() to have \'id\'')
    
    payload = {'tags': []}
    result = operator.product(product_id).update(payload)
    expect(isinstance(result, dict), 'product(id).update() to be a dict')
    expect(isinstance(result['tags'], list), 'product(id).update()[\'tags\'] to be a list')
    
    result = operator.product(product_id).delete()
    expect(result.status_code == 200, 'product(id).delete() status_code to be 200')

def test_collections():
    payload = {'name': 'Test Collection'}
    result = operator.collection().create(payload)
    collection_id = result['id']
    expect(isinstance(result, dict), 'collection().create() to be a dict')
    expect(isinstance(result['id'], str), 'collection().create() to have \'id\'')

    result = operator.collection().read()
    expect(isinstance(result, list), 'collection().read() to be a list')

    result = operator.collection(collection_id).read()
    expect(isinstance(result, dict), 'collection(id).read() to be a dict')
    expect(isinstance(result['id'], str), 'collection(id).read() to have \'id\'')
    
    payload = {'tags': []}
    result = operator.collection(collection_id).update(payload)
    expect(isinstance(result, dict), 'collection(id).update() to be a dict')
    expect(isinstance(result['tags'], list), 'collection(id).update()[\'tags\'] to be a list')
    
    result = operator.collection(collection_id).delete()
    expect(result.status_code == 200, 'collection(id).delete() status_code to be 200')

def test_places():
    payload = {'name': 'Test Place'}
    result = operator.place().create(payload)
    place_id = result['id']
    expect(isinstance(result, dict), 'place().create() to be a dict')
    expect(isinstance(result['id'], str), 'place().create() to have \'id\'')

    result = operator.place().read()
    expect(isinstance(result, list), 'place().read() to be a list')

    result = operator.place(place_id).read()
    expect(isinstance(result, dict), 'place(id).read() to be a dict')
    expect(isinstance(result['id'], str), 'place(id).read() to have \'id\'')
    
    payload = {'tags': []}
    result = operator.place(place_id).update(payload)
    expect(isinstance(result, dict), 'place(id).update() to be a dict')
    expect(isinstance(result['tags'], list), 'place(id).update()[\'tags\'] to be a list')
    
    result = operator.place(place_id).delete()
    expect(result.status_code == 200, 'place(id).delete() status_code to be 200')

def test_action_types():
    payload = {'name': '_TestActionType'}
    result = operator.action_type().create(payload)
    action_type_name = result['name']
    expect(isinstance(result, dict), 'action_type().create() to be a dict')
    expect(isinstance(result['id'], str), 'action_type().create() to have \'id\'')

    result = operator.action_type().read()
    expect(isinstance(result, list), 'action_type().read() to be a list')

    result = operator.action_type(action_type_name).read()
    expect(isinstance(result, list), 'action_type(name).read() to be a list')
    
    payload = {'tags': []}
    result = operator.action_type(action_type_name).update(payload)
    expect(isinstance(result, dict), 'action_type(name).update() to be a dict')
    expect(isinstance(result['tags'], list), 'action_type(name).update()[\'tags\'] to be a list')
    
    result = operator.action_type(action_type_name).delete()
    expect(result.status_code == 200, 'action_type(name).delete() status_code to be 200')

def test_application_users():
    result = operator.application_user().read()
    expect(isinstance(result, list), 'application_user().read() to be a list')

    if len(result) == 0:
        print('No users available to test')
        return
    
    result = result[0]
    payload = {'tags': []}
    result = operator.application_user(result['id']).update(payload)
    expect(isinstance(result, dict), 'application_user().update() to be a dict')
    expect(isinstance(result['tags'], list), 'application_user().update()[\'tags\'] to be a list')
    
    result = operator.application_user(result['id']).delete()
    expect(result.status_code == 200, 'application_user().delete() status_code to be 200')


# ---------------------------------- Test Bed ----------------------------------

test_results = {
    'total': 0,
    'pass': 0
}

def expect(condition, label):
    test_results['total'] += 1
    if not condition:
        print('fail: Expect', label)
    else:
        print('pass: Expect', label)
        test_results['pass'] += 1

def print_test_results():
    failed = (test_results['total'] - test_results['pass'])
    print('\nResults:', test_results['pass'], 'pass,', failed, 'fail')

if '__main__' in __name__:
    run_all()
    print_test_results()