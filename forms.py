from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    '''Form for adding pets.'''

    name = StringField('Pet Name', validators=[InputRequired(message='Please add a pet name')])

    species = SelectField('Pet Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])

    photo_url = StringField('Pet Photo(url)', validators=[Optional(), URL()])

    age = IntegerField('Pet Age', validators=[Optional(), NumberRange(min=0, max=30)])

    notes = TextAreaField('Pet Notes', validators=[Optional()])


class EditPetForm(FlaskForm):
    '''Edit pet information'''

    photo_url = StringField('Pet Photo(url)', validators=[Optional(), URL()])

    notes = TextAreaField('Pet Notes', validators=[Optional()])

    available = BooleanField('Available?')
