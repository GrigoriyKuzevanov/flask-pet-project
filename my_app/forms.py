from flask_wtf import FlaskForm
from wtforms import (BooleanField, DateTimeField, FloatField, PasswordField,
                     SelectField, StringField, SubmitField)
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Optional, ValidationError)

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


class ProfileForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    email = StringField("Электронная почта", validators=[DataRequired()])
    first_name = StringField("Имя")
    last_name = StringField("Фамилия")
    reg_at = DateTimeField("Дата регистрации", validators=[Optional()])
    company = SelectField(
        "Управляющая компания", coerce=int, validators=[InputRequired()]
    )
    submit = SubmitField("Изменить профиль", validators=[Optional()])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        print(username.data, user.username)
        if user is not None and username.data != user.username:
            raise ValidationError("Данный логин уже используется в системе")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        print(self.username.data, user.email)
        if user is not None and self.username.data != user.username:
            raise ValidationError("Данный почтовый адрес уже используется в системе")


class PriceForm(FlaskForm):
    tko = FloatField("Обращение с ТКО (руб/м.куб)", validators=[Optional()])
    maintenance_common = FloatField(
        "Содержание жилья (руб/м.кв)", validators=[Optional()]
    )
    drainage_common = FloatField(
        "Водоотведение (общее) (руб/м.куб)", validators=[Optional()]
    )
    cold_water_common = FloatField("ХВС (общее) (руб/м.куб)", validators=[Optional()])
    hot_water_volume_common = FloatField(
        "ГВС теплоноситель (общее) (руб/м.куб)", validators=[Optional()]
    )
    hot_water_energy_common = FloatField(
        "ГВС тепловая энергия (общее) (руб/Гкал)", validators=[Optional()]
    )
    electricity_common = FloatField(
        "Электроэнергия (общее) (руб/кВт.ч)", validators=[Optional()]
    )
    heating = FloatField("Отопление (руб/Гкал)", validators=[Optional()])
    cold_water = FloatField("ХВС (руб/м.куб)", validators=[Optional()])
    hot_water_volume = FloatField(
        "ГВС теплоноситель (руб/м.куб)", validators=[Optional()]
    )
    hot_water_energy = FloatField(
        "ГВС тепловая энергия (руб/Гкал)", validators=[Optional()]
    )
    drainage = FloatField("Водоотведение (руб/м.куб)", validators=[Optional()])
    gas = FloatField("Газоснабжение (руб/м.куб)", validators=[Optional()])
    renovation = FloatField("Взнос на кап. ремонт (руб/м.кв)", validators=[Optional()])
    submit = SubmitField("Отправить", validators=[Optional()])
