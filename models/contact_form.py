from dataclasses import dataclass


@dataclass
class ContactFormData:
    name: str
    email: str
    phone: str
    country: str
    company_name: str
    employees_count: str
    help_required: str
    incident_type: str
    incident_details: str
