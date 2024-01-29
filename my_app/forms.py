from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
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
