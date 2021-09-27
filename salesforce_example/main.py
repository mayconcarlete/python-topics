import json
from simple_salesforce import Salesforce

login_info = json.load(open('configs.json'))
username = login_info['username']
password = login_info['password']
security_token = login_info['security_token']

sf = Salesforce(username=username, password=password, security_token=security_token)

print(sf)

