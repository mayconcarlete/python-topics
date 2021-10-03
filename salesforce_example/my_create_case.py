from typing import Type
from models.case_requirements import CaseRequirements
from application.validations.check_field_instance import CheckFieldInstance


def create_case_in_salesforce_account(case_requirements: CaseRequirements):
    check_field_instance = CheckFieldInstance(str)
    case_requirements.case_title = case_requirements.case_title if check_field_instance.validate(case_requirements.case_title) else None
    case_requirements.record_type_case_name = case_requirements.record_type_case_name if check_field_instance.validate(case_requirements.record_type_case_name) else None

    # VERIFY COMPANY IN API ADMIN
    # verify
    return case_requirements.case_title

def check_field_instance(field: str, type: Type):
    if isinstance(field, type):
        return field
    return None



if __name__ == '__main__':
    salesforce_case = CaseRequirements(
        company_id='abc_123',
        document_number='3321',
        description='description',
        case_title='case_title',
        record_type_case_name='record_type_case_name'
    )
    response = create_case_in_salesforce_account(salesforce_case)
    print(response)
