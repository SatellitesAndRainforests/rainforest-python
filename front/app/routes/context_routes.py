from flask import Blueprint, current_app,  render_template, request

from app.clients.geoserver_client import check_geoserver_connection, publish_context_package_stub
from app.clients.java_api_client import create_context_package, update_context_package_status
from app.forms.context_forms import LocationContextForm
from app.services.context_service import ( build_context_import_request, build_context_request )



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


@context_bp.route("/import", methods=["POST"])
def import_context():

    context_import = build_context_import_request(
        latitude = float(request.form["latitude"]),
        longitude = float(request.form["longitude"]),
        layer = request.form["layer"],
        image_date = request.form["image_date"],
    )

    java_response = create_context_package(
        base_url=current_app.config["JAVA_CATALOGUE_BASE_URL"],
        payload=context_import["java_payload"],
    )

    publish_response = publish_context_package_stub(
        workspace=current_app.config["GEOSERVER_WORKSPACE"],
        context_package_id=java_response["contextPackageId"],
        layer=context_import["layer"],
    )

    java_response = update_context_package_status(
        base_url=current_app.config["JAVA_CATALOGUE_BASE_URL"],
        context_package_id=java_response["contextPackageId"],
        payload=publish_response,
    )

    return render_template(
            "context_import_status.html",
            context_import = context_import,
            java_response = java_response
    )



@context_bp.route("/geoserver/check")
def check_geoserver():
    result = check_geoserver_connection(
        base_url=current_app.config["GEOSERVER_BASE_URL"],
        username=current_app.config["GEOSERVER_USER"],
        password=current_app.config["GEOSERVER_PASSWORD"],
    )

    return result





