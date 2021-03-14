from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PersonaForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    surname = StringField('Apellido', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    send = SubmitField('Enviar')