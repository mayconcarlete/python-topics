import json
from dataclasses import dataclass, asdict

@dataclass
class AccountPagarmeClient:
    Name: str
    ParentId: str
    RecordTypeId: str
    AffiliationId__c: str
    BillingStreet: str
    BillingCity: str
    BillingState: str
    BillingPostalCode: str
    BillingCountry: "Brasil"
    Phone: str
    cnpj__c: str
    cpf_cnpj__c: str
    ClientStatus__c: "Active"
    AccountStatus__c: "Active"
    legal_name__c: str
    Razao_Social__c: str
    BankAccountBankName__c: str
    BankAccountType__c: str
    BankAccountAgencyNumber__c: str
    BankAccountAgencyDigit__c: str
    BankAccountNumber__c: str
    BankAccountDigit__c: str
    sales_channel_name__c: str

    def __str__(self):
        return asdict(self)
