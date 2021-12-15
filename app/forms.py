from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# I realize now that using flask wtforms was unnecessary. Shut up

class SearchStore(FlaskForm):
    search = StringField('search')