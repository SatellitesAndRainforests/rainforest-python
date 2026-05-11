from flask import Blueprint, render_template

from app.forms.context_forms import LocationContextForm
from app.services.context_service import build_context_request

context_bp = Blueprint("context", __name__, url_prefix="/context")


@context_bp.route("/new", methods=["GET", "POST"])
def new_context():

    form = LocationContextForm()

    if form.validate_on_submit():
        context_request = build_context_request(
            latitude=float(form.latitude.data),
            longitude=float(form.longitude.data)
        )

        return render_template(
            "context_result.html",
            context_request=context_request
        )

    return render_template("context_form.html", form=form)