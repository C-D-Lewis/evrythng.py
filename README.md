# evrythng.py
Concept Python SDK for the EVRYTHNG API. Inspired by the chainable aspects of [`evrythng.js`](https://github.com/evrythng/evrythng.js/).


## Import

```python
import evrythng
```


## Authenticate

```python
# Truncated Operator API Key from the EVRYTHNG Dashboard
OPERATOR_API_KEY = 'hGCKwlGBRPAE1BY6Ba7zxhdiapcg...'

operator = evrythng.Operator(OPERATOR_API_KEY)
```


## Use Resources

For example, to CRUD a Thng:

```python
thngs = operator.thng().read()

print('Read ' + str(len(thngs)) + ' Thngs')
```

```python
new_thng = { 'name': 'Thng from evrythng.py' }
created_thng = operator.thng().create(new_thng)

print('Created Thng ' + created_thng['id'])
```

```python
update_thng = operator.thng(created_thng['id']).update({ 'tags': [] })

print('Updated Thng ' + update_thng['id'])
```

```python
operator.thng(updated_thng['id']).delete()

print('Deleted Thng ' + update_thng['id'])
```
