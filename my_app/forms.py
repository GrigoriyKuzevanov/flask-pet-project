from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import (BooleanField, DateField, DateTimeField, FloatField,
                     PasswordField, SelectField, StringField, SubmitField)
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Optional, ValidationError)
from wtforms.widgets import DateInput, MonthInput

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

    def __init__(self, original_username, original_email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError("Данный логин уже используется в системе")

    def validate_email(self, email):
        if email.data != self.original_email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError(
                    "Данный почтовый адрес уже используется в системе"
                )


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
    hot_water_volume = FloatField(
        "ГВС теплоноситель (руб/м.куб)", validators=[Optional()]
    )
    hot_water_energy = FloatField(
        "ГВС тепловая энергия (руб/Гкал)", validators=[Optional()]
    )
    cold_water = FloatField("ХВС (руб/м.куб)", validators=[Optional()])
    drainage = FloatField("Водоотведение (руб/м.куб)", validators=[Optional()])
    electricity = FloatField("Электроэнергия (кВт.ч)", validators=[Optional()])
    gas = FloatField("Газоснабжение (руб/м.куб)", validators=[Optional()])
    renovation = FloatField("Взнос на кап. ремонт (руб/м.кв)", validators=[Optional()])
    submit = SubmitField("Отправить", validators=[Optional()])


class ConsumptionForm(FlaskForm):
    invoice_date = DateField("Дата платежа", validators=[DataRequired()])
    tko = FloatField("Обращение с ТКО (м.куб)", validators=[Optional()])
    maintenance_common = FloatField("Содержание жилья (м.кв)", validators=[Optional()])
    drainage_common = FloatField(
        "Водоотведение (общее) (м.куб)", validators=[Optional()]
    )
    cold_water_common = FloatField("ХВС (общее) (м.куб)", validators=[Optional()])
    hot_water_volume_common = FloatField(
        "ГВС теплоноситель (общее) (м.куб)", validators=[Optional()]
    )
    hot_water_energy_common = FloatField(
        "ГВС тепловая энергия (общее) (Гкал)", validators=[Optional()]
    )
    electricity_common = FloatField(
        "Электроэнергия (общее) (кВт.ч)", validators=[Optional()]
    )
    heating = FloatField("Отопление (Гкал)", validators=[Optional()])
    hot_water_volume = FloatField("ГВС теплоноситель (м.куб)", validators=[Optional()])
    hot_water_energy = FloatField(
        "ГВС тепловая энергия (Гкал)", validators=[Optional()]
    )
    cold_water = FloatField("ХВС (м.куб)", validators=[Optional()])
    drainage = FloatField("Водоотведение (м.куб)", validators=[Optional()])
    electricity = FloatField("Электроэнергия (кВт.ч)", validators=[Optional()])
    gas = FloatField("Газоснабжение (м.куб)", validators=[Optional()])
    renovation = FloatField("Взнос на кап. ремонт (м.кв)", validators=[Optional()])
    recalculation = FloatField("Перерасчет (руб.)", validators=[Optional()])
    submit = SubmitField("Отправить", validators=[Optional()])
