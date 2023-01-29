from app import app
from app import db
from app.models import User
from app.forms import RegisterForm, LoginForm
from flask_bcrypt import Bcrypt
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required

@app.route('/', methods=["GET"])
def home():

    return render_template("dashboard.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hash_password = Bcrypt.generate_password_hash(form.password.data) # hash password
        new_user = User(username=form.username.data, password=hash_password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash(f"Account created successfully! you are now logged in as {new_user}")
        return redirect(url_for('login'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a User: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attemted_user = User.query.filter_by(username=form.username.data).first()
        if attemted_user and attemted_user.check_passwors_correction(
            attempted_password=form.password.data):

            login_user(attemted_user)
            flash(f"Success! You're logged in add {attemted_user.username}", category='success')
            return redirect(url_for('home'))

        else:
            flash('Username and Password are not match! Please try again', category='danger')