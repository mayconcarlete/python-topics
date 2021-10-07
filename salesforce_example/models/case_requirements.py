from dataclasses import dataclass


@dataclass
class CaseRequirements:
    company_id: str
    document_number: str
    description: str
    case_title: str
    record_type_case_name: str


@dataclass
class PagarmeAccount:
    Name: str
    ParentId: str
    RecordTypeId: str
    AffiliationId__c: str
    BillingStreet: str
    BillingCity: str
    BillingState: str
    BillingPostalCode: str
    BillingCountry: str
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
