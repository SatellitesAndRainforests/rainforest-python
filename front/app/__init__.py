from flask import Flask
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-only-secret-key"
app.config["NASA_GIBS_WMS_ENDPOINT"] = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
app.config["NASA_GIBS_DEFAULT_LAYER"] = "VIIRS_SNPP_CorrectedReflectance_TrueColor"

app.jinja_loader = ChoiceLoader([
    PackageLoader("app"),
    PrefixLoader({
        "govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja"),
        "govuk_frontend_wtf": PackageLoader("govuk_frontend_wtf"),
    })
])



from app.routes  import register_routes

register_routes(app)

