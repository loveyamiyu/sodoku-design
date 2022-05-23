# Project Contributors
Student Name & Number: Fangting Yu 22391059
Student Name & Number: Yingying Liao 23166974

# Description
This sudoku game is created by Yingying and Fangting for a CITS5505 project assessment purpose. Involve the usage of HTML, JavaScript, CSS, AJAX and Flask.

# Virtual environment creation

## Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

## macOS
python3 -m venv .venv
source .venv/bin/activate

## Windows
py -3 -m venv .venv
.venv\scripts\activate

# Installation

pip install flask

## installation for __init__.py
pip install flask_sqlalchemy,flask_migrate,flask_login

## installation for forms.py
pip install wtforms,flask_wtf,sqlalchemy,asyncio.proactor_events,wtforms.validators 

## installation for routes.py
pip install cmath, crypt, flask, flask_login, werkzeug.urls

## installation for models.py
pip install datetime, typing_extensions, flask_login, werkzeug.security


# Run the app
python -m flask run