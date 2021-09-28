import json
from simple_salesforce import Salesforce
from simple_salesforce import login
from simple_salesforce.login import SalesforceLogin

login_info = json.load(open('configs.json'))
username = login_info['username']
password = login_info['password']
security_token = login_info['security_token']
domain = login_info['domain']


#get session token
session_d, instance  =  SalesforceLogin(username, password, security_token, domain)
print(session_d, instance)

# fazendo login com usuario e password (nao recomendado)
# sf = Salesforce(username=username, password=password, security_token=security_token)

# passando uma session como login (recomendado)
sf = Salesforce(instance_url=instance, session_id=session_d)
print(sf)

for element in dir(sf):
    if not element.startswith('__'):
        if isinstance(getattr(sf, element), str):
            print(f'Property name: {element}: value: {getattr(sf, element)}')

# print(sf.session_id)
# example = sf.Contact.create({'LastName':'Smith','Email':'example@example.com'})
# print(example)