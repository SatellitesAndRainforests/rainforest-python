from flask_wtf import FlaskForm
from govuk_frontend_wtf.wtforms_widgets import GovTextInput
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired, NumberRange


class LocationContextForm(FlaskForm):
    latitude = DecimalField(
        "Latitude",
        widget=GovTextInput(),
        validators=[InputRequired(), NumberRange(min=-90, max=90)]
    )

    longitude = DecimalField(
        "Longitude",
        widget=GovTextInput(),
        validators=[InputRequired(), NumberRange(min=-180, max=180)]
    )

    submit = SubmitField("Get contextual data")

