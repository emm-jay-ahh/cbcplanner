from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be longer than 3 characters", category='error')
        elif len(first_name) < 2:
            flash("First name must be longer than 1 characters", category='error')
        elif len(last_name) < 2:
            flash("Last name must be longer than 1 characters", category='error')
        elif password1 != password2:
            flash("Passwords do not match", category='error')
        elif len(password1) < 8:
            flash("Minimum password length is 8 characters", category='error')
        else:
            flash("Account created", category='success')

    return render_template("sign_up.html")
