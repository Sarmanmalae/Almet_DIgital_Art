from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField, BooleanField
from wtforms.validators import DataRequired
from wtforms import FileField


class ShopsAddingForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    tg_name = StringField('Телеграм канал', validators=[DataRequired()])
    specific_gps = StringField('Местоположение', validators=[DataRequired()])
    which_map = IntegerField('Какая карта?', validators=[DataRequired()])
    color = StringField('Цвет для указателя', validators=[DataRequired()])
    submit = SubmitField('Добавить')
