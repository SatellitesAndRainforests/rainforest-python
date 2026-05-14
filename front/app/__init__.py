from flask import Flask
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-only-secret-key"

app.config["NASA_GIBS_PREVIEW_WIDTH"] = 300
app.config["NASA_GIBS_PREVIEW_HEIGHT"] = 300
app.config["NASA_GIBS_EXPORT_WIDTH"] = 2000
app.config["NASA_GIBS_EXPORT_HEIGHT"] = 2000
app.config["NASA_GIBS_HALF_DEGREE"] = 10.0



# # 1. Best default: natural satellite image
app.config["NASA_GIBS_WMS_ENDPOINT"] = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
app.config["NASA_GIBS_DEFAULT_LAYER"] = "VIIRS_SNPP_CorrectedReflectance_TrueColor"

# # 2. Newer NOAA-20 true colour
#app.config["NASA_GIBS_WMS_ENDPOINT"] = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
#app.config["NASA_GIBS_DEFAULT_LAYER"] = "VIIRS_NOAA20_CorrectedReflectance_TrueColor"

# # 3. MODIS Terra true colour
#app.config["NASA_GIBS_WMS_ENDPOINT"] = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
#app.config["NASA_GIBS_DEFAULT_LAYER"] = "MODIS_Terra_CorrectedReflectance_TrueColor"

# # 4. False colour: vegetation/water/burn/cloud contrast
# app.config["NASA_GIBS_WMS_ENDPOINT"] = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
# app.config["NASA_GIBS_DEFAULT_LAYER"] = "VIIRS_SNPP_CorrectedReflectance_BandsM11-I2-I1"

# # 5. Alternative false colour
# app.config["NASA_GIBS_WMS_ENDPOINT"] = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
# app.config["NASA_GIBS_DEFAULT_LAYER"] = "VIIRS_SNPP_CorrectedReflectance_BandsM3-I3-M11"

# # 6. Vegetation greenness
# app.config["NASA_GIBS_WMS_ENDPOINT"] = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
# app.config["NASA_GIBS_DEFAULT_LAYER"] = "VIIRS_SNPP_NDVI_8Day"

# # 7. Land surface temperature
# app.config["NASA_GIBS_WMS_ENDPOINT"] = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
# app.config["NASA_GIBS_DEFAULT_LAYER"] = "VIIRS_SNPP_Land_Surface_Temp_Day"

# # 8. Fires / thermal anomalies
# app.config["NASA_GIBS_WMS_ENDPOINT"] = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
# app.config["NASA_GIBS_DEFAULT_LAYER"] = "VIIRS_SNPP_Thermal_Anomalies_375m_All"

# # 9. Aerosol / smoke / haze
# app.config["NASA_GIBS_WMS_ENDPOINT"] = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
# app.config["NASA_GIBS_DEFAULT_LAYER"] = "VIIRS_SNPP_AOD_Dark_Target_Land_Ocean"

# # 10. Rainfall / precipitation rate
# app.config["NASA_GIBS_WMS_ENDPOINT"] = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
# app.config["NASA_GIBS_DEFAULT_LAYER"] = "IMERG_Precipitation_Rate"






app.config["JAVA_CATALOGUE_BASE_URL"] = "http://localhost:8080"


app.jinja_loader = ChoiceLoader([
    PackageLoader("app"),
    PrefixLoader({
        "govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja"),
        "govuk_frontend_wtf": PackageLoader("govuk_frontend_wtf"),
    })
])



from app.routes  import register_routes

register_routes(app)

