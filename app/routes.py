from flask import Blueprint, render_template, request, flash, url_for, redirect
from .forms import ApplicantForm
from .db import session
from .models import Applicant


bp = Blueprint('index', __name__)


@bp.route('/', methods=['GET'], strict_slashes=True)
def index():
    return render_template('index.html')


@bp.route('/request-loan', methods=['GET'], strict_slashes=True)
def request_loan_form():
    form = ApplicantForm()
    return render_template('loan.html', form=form)


@bp.route('/request-loan', methods=['POST'], strict_slashes=True)
def request_loan():
    s = session()
    request_data = request.form.to_dict()
    form = ApplicantForm(**request_data)

    if form.validate_on_submit():
        del request_data['csrf_token']
        del request_data['submit']

        new_applicant = Applicant(**request_data)

        s.add(new_applicant)
        s.commit()
        flash(message='Request added successfully!', category='success')
        return redirect(url_for('index.index'))
    flash(message='Please check your form again.', category='error')
    return redirect(url_for('index.request_loan_form'))
