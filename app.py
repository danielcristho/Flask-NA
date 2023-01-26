from flask import Flask, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
