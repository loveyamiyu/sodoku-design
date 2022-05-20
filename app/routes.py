
from crypt import methods
from unicodedata import name
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from .models import User
from . import db
from app.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from urllib.parse import urlparse
 

@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return redirect("home.html", username=current_user.username)

@app.route("/rules/")
def rules():
    return render_template("rules.html")

@app.route("/stats/")
def stats():
    return render_template("stats.html")

@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for user {}, remeember_me={}'.format(form.email.data,
        form.remember_me.data))
        
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)

    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if check_password_hash(user.password, form.password.data): 
            login_user(user)

        user = User.query.filter_by(email=form.email.data).first()
        ext_url = request.args.get("next")
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
        else:
            login_user(user, remember=form.remember_me.data)
            if next_url:
                return redirect(next_url) 
            return redirect(url_for('home'))
    else: 
        return render_template('login.html', title='Log in', form=form) """






"""
        if user:
            if user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash('Invalid username or password')
        else:

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        next_url = request.args.get("next")
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
        else:
            login_user(user, remember=form.remember_me.data)
            if next_url:
                return redirect(next_url) 
            return redirect(url_for('home'))
    else: 
        return render_template('login.html', title='Log in', form=form) """

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign up', form=form)


if __name__ == '__main__':
   app.run(debug = True)