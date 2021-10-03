import json
from dataclasses import dataclass, asdict

    # ParentId: str

@dataclass
class AccountPagarmeClient:
    Name: str
    RecordTypeId: str
    AffiliationId__c: str
    BillingStreet__c: str
    BillingCity__c: str
    BillingState__c: str
    BillingPostalCode__c: str
    BillingCountry__c: str
    Phone: str
    cnpj__c: str
    cpf_cnpj__c: str
    ClientStatus__c: str
    AccountStatus__c: str
    legal_name__c: str
    Razao_Social__c: str
    BankAccountBankName__c: str
    BankAccountType__c: str
    BankAccountAgencyNumber__c: str
    BankAccountAgencyDigit__c: str
    BankAccountNumber__c: str
    BankAccountDigit__c: str
    sales_channel_name__c: str

    def to_dict(self):
        return asdict(self)
