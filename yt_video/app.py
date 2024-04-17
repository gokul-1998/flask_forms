from flask import Flask
from flask import (Flask, flash, redirect, render_template, request,
                   session, abort,redirect,url_for,send_file)

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import DateField, StringField, PasswordField, BooleanField,RadioField,DateTimeField,SelectField, SubmitField,TextAreaField

from wtforms.validators import InputRequired, Email, Length,DataRequired

app=Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'

# we need to use secret key whenever you use wtf forms

class Widget(FlaskForm):
    FirstName=StringField(label="First Name",validators=[DataRequired()])
    LastName=StringField(label="Last Name")
    rating=SelectField(label="How would you rate yourself on a scale of 5 in Python",choices=[
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5")
    ])

    comments=TextAreaField(label="Enter your comments")
    choice=RadioField(label="What do you like the most in python",choices=[
        ("Web Scraping","Web Scraping"),
        ("Machine Learning","MAchine Learning"),
        ("Data Science","Data Science"),
        ("Web apps","Web apps"),
    ])
    birthday=DateField(label="Enter your Birthday",format="%Y-%m-%d")
    submit=SubmitField(label="Submit")


@app.route("/",methods=["GET","POST"])
def home():
    form=Widget()
    return render_template("home.html",form=form)


if __name__=="__main__":
    app.run(debug=True)