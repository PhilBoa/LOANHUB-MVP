import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, DateTime


Base = declarative_base()


class Applicant(Base):
    '''Model for applicants'''
    __tablename__ = "applicants"

    id = Column(String(255), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    applicant_fullname = Column(String(255), nullable=False)
    applicant_email = Column(String(255), nullable=False)
    applicant_phone = Column(String(255), nullable=False)
    applicant_address = Column(String(255), nullable=False)
    applicant_location = Column(String(255), nullable=False)
    applicant_employment_status = Column(String(255), nullable=False)
    purpose_loan = Column(String(255), nullable=False)
    amount = Column(String(255), nullable=False)
    guanrantor_fullname = Column(String(255), nullable=False)
    guanrantor_email = Column(String(255), nullable=False)
    guanrantor_phone = Column(String(255), nullable=False)
    guanrantor_address = Column(String(255), nullable=False)
    guarantor_relationship_to_applicant = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, applicant_fullname, applicant_email, applicant_phone,
                 applicant_address, applicant_location, applicant_employment_status,
                 purpose_loan, amount, guanrantor_fullname, guanrantor_email, guanrantor_phone,
                 guanrantor_address, guarantor_relationship_to_applicant):
        self.applicant_fullname = applicant_fullname
        self.applicant_email = applicant_email
        self.applicant_phone = applicant_phone
        self.applicant_address = applicant_address
        self.applicant_location = applicant_location
        self.applicant_employment_status = applicant_employment_status
        self.purpose_loan = purpose_loan
        self.amount = amount
        self.guanrantor_fullname = guanrantor_fullname
        self.guanrantor_email = guanrantor_email
        self.guanrantor_phone = guanrantor_phone
        self.guanrantor_address = guanrantor_address
        self.guarantor_relationship_to_applicant = guarantor_relationship_to_applicant

    def __str__(self):
        return f'<Applicant {self.id} {self.applicant_fullname}>'

    def __repr__(self):
        return f'''Applicant(id={self.id}, applicant_fullname={self.applicant_fullname},
    applicant_email={self.applicant_email}, applicant_phone={self.applicant_phone},
    applicant_address={self.applicant_address}, applicant_location={self.applicant_location},
    applicant_employment_status={self.applicant_employment_status}, purpose_loan={self.purpose_loan},
    amount={self.amount}, guanrantor_fullname={self.guanrantor_fullname}, guanrantor_email={self.guanrantor_email},
    guanrantor_phone={self.guanrantor_phone}, guanrantor_address={self.guanrantor_address},
    guarantor_relationship_to_applicant={self.guarantor_relationship_to_applicant})'''
