import pytest
from salesforce_example.application.validations.check_field_instance import CheckFieldInstance
from salesforce_example.models.case_requirements import CaseRequirements


def test_it_should_return_true_if_type_value_checked_is_equal_from_expected():
    salesforce_case = CaseRequirements(
        company_id='abc_123',
        document_number='3321',
        description='description',
        case_title='case_title',
        record_type_case_name='record_type_case_name'
    )
    sut = CheckFieldInstance(str)
    result = sut.validate(salesforce_case.case_title)
    assert result is True


def test_it_should_return_false_if_type_value_checked_is_different_from_expected():
    salesforce_case = CaseRequirements(
        company_id='abc_123',
        document_number='3321',
        description='description',
        case_title='any_value',
        record_type_case_name='record_type_case_name'
    )
    sut = CheckFieldInstance(int)
    result = sut.validate(salesforce_case.case_title)
    assert result is False
