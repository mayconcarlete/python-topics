from dataclasses import dataclass


@dataclass
class CaseRequirements:
    company_id: str
    document_number: str
    description: str
    case_title: str
    record_type_case_name: str
