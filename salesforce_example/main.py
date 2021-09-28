import json
import pandas as pd
from simple_salesforce import Salesforce
from simple_salesforce.api import SFType
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
sf = Salesforce(instance=instance, session_id=session_d)
# print(sf)

# for element in dir(sf):
#     if not element.startswith('__'):
#         if isinstance(getattr(sf, element), str):
#             print(f'Property name: {element}: value: {getattr(sf, element)}')

# print(sf.session_id)
# example = sf.Contact.create({'LastName':'Smith','Email':'example@example.com'})
# print(example)

# metadata_org = sf.describe()
# print(metadata_org)
# print(type(metadata_org))
# print(metadata_org.keys())
# print(metadata_org['sobjects'])
# df_sobjects = pd.DataFrame(metadata_org['sobjects'])
# print(df_sobjects.head())
# df_sobjects.to_csv('org_metadata_sobjects.csv', index=False)
# os principais que ele olha nesse CSV são os campos name e label

# Metodo 1
# account = sf.account
# print(account)
# print(type(account))
# account_metadata = account.describe()
# print(account_metadata.keys())
# df_metadata_fields = pd.DataFrame(account_metadata.get('fields'))
# print(df_metadata_fields)

# method 1
# project__c = sf.Project__c
# metadata_project = project__c.metadata()
# df_project_metadata = pd.DataFrame(metadata_project.get('objectDescribe'))
# df_project_metadata.to_csv('project metadata.csv', index=False)


# method 2
# account = SFType('account', session_id, instance)
# account_metadata = account.metadata()
# df_account_metadata = pd.DataFrame(account_metadata.get('objectDescribe'))
# df_account_metadata.to_csv('account metadata.csv', index=False)