from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

# I realize now that using flask wtforms was unnecessary. Shut up

class SearchStore(FlaskForm):
    search = StringField('search', id='search-bar')

class NewsletterForm(FlaskForm):
    email = StringField('email', validators=[Email(), DataRequired()], id='newsletter-email-box')
    submit = SubmitField('Get Updates', id='newsletter-submit-box')