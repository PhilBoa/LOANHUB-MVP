from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class ApplicantForm(FlaskForm):
    '''Applicant Form'''
    applicant_fullname = StringField('Full Name', render_kw={"placeholder": "Enter your full name"}, validators=[DataRequired()])
    applicant_email = StringField('Email', render_kw={"placeholder": "Enter your email"}, validators=[DataRequired(), Email()])
    applicant_phone = StringField('Phone Number', render_kw={"placeholder": "Enter your phone number"}, validators=[DataRequired()])
    applicant_address = StringField('Address', render_kw={"placeholder": "Enter your address"}, validators=[DataRequired()])
    applicant_location = StringField('Location', render_kw={"placeholder": "Enter your location"}, validators=[DataRequired()])
    applicant_employment_status = StringField('Employment Status', render_kw={"placeholder": "Enter your employment status"}, validators=[DataRequired()])
    purpose_loan = StringField('Loan Purpose', render_kw={"placeholder": "Enter the purpose of the loan"}, validators=[DataRequired()])
    amount = StringField('Loan Amount', render_kw={"placeholder": "Enter the loan amount"}, validators=[DataRequired()])
    guanrantor_fullname = StringField('Guarantor Full Name', render_kw={"placeholder": "Enter the guarantor's full name"}, validators=[DataRequired()])
    guanrantor_email = StringField('Guarantor Email', render_kw={"placeholder": "Enter the guarantor's email"}, validators=[DataRequired(), Email()])
    guanrantor_phone = StringField('Guarantor Phone Number', render_kw={"placeholder": "Enter the guarantor's phone number"}, validators=[DataRequired()])
    guanrantor_address = StringField('Guarantor Address', render_kw={"placeholder": "Enter the guarantor's address"}, validators=[DataRequired()])
    guarantor_relationship_to_applicant = StringField('Guarantor Relationship to Applicant', render_kw={"placeholder": "Enter the guarantor's relationship to the applicant"}, validators=[DataRequired()])
    submit = SubmitField('Submit')
