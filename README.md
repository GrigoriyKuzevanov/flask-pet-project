# "Коммуналка"

Сервис "Коммуналка" для учета трат на коммунальные услуги. Сервис поддерживает
возможность регистрации пользователя. Пользователь может изменять тариф на коммунальные услуги, вносить объем потребления - сервис формирует общую стоимость, стоимость по каждой отдельной услуге, по группам услуг. Сервис предоставляет доступ к счетам пользователя и статистике его расходов.

## Используемые технологии
- Flask
- Flask-sqlalchemy
- Celery
- Redis
- Postgresql
- Bootstrap
- Alembic

## Конфигурация
Перед запуском вам следует создать файл `.env` в корневой директории проекта и установить следующие переменные в нем:

```
SECRET_KEY=
FLASK_DEBUG=

FLASK_APP=payments.py

#DB
DB_USER=
DB_PASSWORD=
DB_NAME=
DB_HOST=
DB_PORT=

# "postgresql://<username>:<password>@localhost/<database_name>"
SQLALCHEMY_DATABASE_URI=

# email
MAIL_SERVER=
MAIL_PORT=
MAIL_USE_TLS=
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_ADDRESS=

# Celery
CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=
CELERY_TASK_IGNORE_RESULT=
```

Конфигурация сервиса находится в файле config.py

## Запуск

Клонируйте данный репозиторий, например с помощью команды:
```
git clone git@github.com:GrigoriyKuzevanov/flask-pet-project.git
```

Необходимо создать базу данных Postgresql для работы сервиса
- [документация Postgresql](https://www.postgresql.org/docs/current/index.html)

Создание вирутального окружения и его активация:
```
python -m venv env
source env/bin/activate
```
Установка зависимостей проекта:
```
pip install -r requirements.txt
```
Создание таблиц базы данных:
```
flask db migrate
flask db upgrade
```
Запуск:
```
flask run
```
Запуск redis:
```
docker-compose -f docker-compose-local.yml up
```
Запуск celery:
```
celery -A payments.celery_app worker --loglevel INFO
```