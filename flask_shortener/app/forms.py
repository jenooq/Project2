from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, URL


class URLform(FlaskForm):
    original_url = StringField('Вставьте ссылку',
                               validators=[DataRequired(message='Поле не должно быть пустым'),
                                           URL(message='Неверная ссылка')])
    submit = SubmitField('Получить короткую ссылку')
