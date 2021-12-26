from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

# I realize now that using flask wtforms was unnecessary. Shut up

class SearchStore(FlaskForm):
    search = StringField('search', id='search-bar')

class NewsletterForm(FlaskForm):
    email = StringField('email', validators=[Email(), DataRequired()], id='newsletter-email-box')
    submit = SubmitField('Get Updates', id='newsletter-submit-box')

class ContactForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')
