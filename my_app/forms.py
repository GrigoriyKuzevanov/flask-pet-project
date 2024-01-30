from flask_wtf import FlaskForm
from wtforms import (BooleanField, FloatField, PasswordField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from my_app.models import User


class LoginForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня", default=True)
    submit = SubmitField("Войти")


class RegistrationForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    email = StringField("Электронная почта", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password2 = PasswordField(
        "Повторите пароль", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Зарегистрироваться")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Данный логин уже используется в системе")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Данный почтовый адрес уже используется в системе")


class PriceForm(FlaskForm):
    tko = FloatField("Обращение с ТКО (руб/м.куб)")
    maintenance_common = FloatField("Содержание жилья (руб/м.кв)")
    drainage_common = FloatField("Водоотведение (общее) (руб/м.куб)")
    cold_water_common = FloatField("ХВС (общее) (руб/м.куб)")
    hot_water_volume_common = FloatField("ГВС теплоноситель (общее) (руб/м.куб)")
    hot_water_energy_common = FloatField("ГВС тепловая энергия (общее) (руб/Гкал)")
    electricity_common = FloatField("Электроэнергия (общее) (руб/кВт.ч)")
    heating = FloatField("Отопление (руб/Гкал)")
    cold_water = FloatField("ХВС (руб/м.куб)")
    hot_water_volume = FloatField("ГВС теплоноситель (руб/м.куб)")
    hot_water_energy = FloatField("ГВС тепловая энергия (руб/Гкал)")
    drainage = FloatField("Водоотведение (руб/м.куб)")
    gas = FloatField("Газоснабжение (руб/м.куб)")
    renovation = FloatField("Взнос на кап. ремонт (руб/м.кв)")
