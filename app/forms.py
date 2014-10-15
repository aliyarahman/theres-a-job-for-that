from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class NameForm(Form):
    username = StringField('username', validators=[DataRequired()])


class LocationForm(Form):
    city = StringField('city', validators=[DataRequired()])
    state = StringField('state', validators=[DataRequired()])