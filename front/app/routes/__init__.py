from app.routes.context_routes import context_bp
from app.routes.main_routes import main_bp


def register_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(context_bp)