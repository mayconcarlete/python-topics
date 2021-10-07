import json
import pandas as pd
from simple_salesforce import Salesforce
from simple_salesforce.api import SFType
from simple_salesforce.login import SalesforceLogin


from pagarme_account_client import AccountPagarmeClient

login_info = json.load(open('configs.json'))
username = login_info['username']
password = login_info['password']
security_token = login_info['security_token']
domain = login_info['domain']

session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token)

sf = Salesforce(session_id=session_id, instance=instance)


# Example
new_client = AccountPagarmeClient(
    Name="Maykerosps",
    ParentId='0035f000004htxNAAQ',
    RecordTypeId="0125f000000cW7iAAE",
    AffiliationId__c="abc_12234",
    BillingStreet__c="rua jair coelho",
    BillingCity__c="sao mateus",
    BillingState__c="ES",
    BillingPostalCode__c="29933640",
    BillingCountry__c= "Brasil",
    Phone="33218600",
    cnpj__c="13857167700",
    cpf_cnpj__c="10000111/1000",
    ClientStatus__c="Active",
    AccountStatus__c="Active",
    legal_name__c="Maykerops",
    Razao_Social__c="Maykerops SA",
    BankAccountBankName__c="201",
    BankAccountType__c="any",
    BankAccountAgencyNumber__c= "0717",
    BankAccountAgencyDigit__c="023",
    BankAccountNumber__c="004122",
    BankAccountDigit__c="8",
    sales_channel_name__c="foo"
)

response = sf.Account.create(new_client.to_dict())

# O que um insert retorna
print(response)

# fazendo uma query para buscar os dados

# query = f"""
#         SELECT "Id", "cnpj__c", "ParentId" from "Account"
#         where
#         "AffiliationId__c" = '{new_client.AffiliationId__c}' and
#         "RecordTypeId" = '{new_client.RecordTypeId}'
#         """


# Pega os campos
# account_model = sf.Account.describe()

# fields = account_model.get('fields')
# for field in fields:
#     field_name = field.get('name')
#     print(field_name)
