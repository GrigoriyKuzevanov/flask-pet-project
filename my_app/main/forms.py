from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, SubmitField
from wtforms.validators import DataRequired, Optional


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
