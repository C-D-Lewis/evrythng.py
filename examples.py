import evrythng

OPERATOR_API_KEY = ''

operator = evrythng.Operator(OPERATOR_API_KEY)
print(operator.api_key)

# Thngs
thngs = operator.thng().read()
print('Read ' + str(len(thngs)) + ' Thngs')

new_thng = { 'name': 'Thng from evrythng.py' }
created_thng = operator.thng().create(new_thng)
print(created_thng)

updated_thng = operator.thng(created_thng['id']).update({ 'tags': [] })
print(updated_thng)

operator.thng(updated_thng['id']).delete()
print('Deleted ' + updated_thng['id'])

# Products
products = operator.product().read()
print('Read ' + str(len(products)) + ' Products')

new_product = { 'name': 'Product from evrythng.py' }
created_product = operator.product().create(new_product)
print(created_product)

updated_product = operator.product(created_product['id']).update({ 'tags': [] })
print(updated_product)

operator.product(updated_product['id']).delete()
print('Deleted ' + updated_product['id'])