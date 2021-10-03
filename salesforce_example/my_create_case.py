from typing import Type
from models.case_requirements import CaseRequirements
from application.validations.check_field_instance import CheckFieldInstance


def create_case_in_salesforce_account(case_requirements: CaseRequirements):
    validate_case_title = CheckFieldInstance(str)
    case_requirements.case_title = case_requirements.case_title if validate_case_title.validate(case_requirements) else None
    # case_requirements.record_type_case_name = check_field_instance(case_requirements.record_type_case_name, str)

    # VERIFY COMPANY IN API ADMIN
    # verify


def check_field_instance(field: str, type: Type):
    if isinstance(field, type):
        return field
    return None



if __name__ == '__main__':
    payload = {
        'teste': 'a'
    }
    response = check_field_instance(payload['teste'], str)
    print(response)
