
from cmath import log
from crypt import methods
from unicodedata import name
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from .models import User
from . import db
from app.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
 

@app.route('/home/')
@login_required
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('login')) # if the user is not authenticated: return to login page.
    return render_template("home.html", user=current_user)

@app.route("/rules/")
def rules():
    return render_template("rules.html")

@app.route("/stats/")
def stats():
    # 添加一个读取所有user_id和时间的variable，
    # 再把这个varaible添加到 stats.html里面去
    return render_template("stats.html")
    # order_by should be used

@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm() #现在这个login form里面是没有值的 因为我们的loginForm没有向database取值
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else: 
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('home')
                return redirect(next_page)
    return render_template('login.html', title='Log in', form=form)


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
        db.session.add(user) # Add latest registered user into the database model
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign up', form=form)


if __name__ == '__main__':
   app.run(debug = True)