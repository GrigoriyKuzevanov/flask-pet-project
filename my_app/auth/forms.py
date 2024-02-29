from flask_wtf import FlaskForm
from my_app.models import User
from wtforms import (BooleanField, DateTimeField, PasswordField, SelectField,
                     StringField, SubmitField)
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Optional, ValidationError)


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


class ResetPasswordRequestForm(FlaskForm):
    email = StringField("Электронная почта", validators=[DataRequired(), Email()])
    submit = SubmitField("Запросить смену пароля")


class ResetPasswordForm(FlaskForm):
    password = PasswordField("Новый пароль", validators=[DataRequired()])
    password2 = PasswordField(
        "Повторите новый пароль", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Сменить пароль")
