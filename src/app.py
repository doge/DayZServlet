from flask import Flask
from .utils import log

from .routes.lud0.routes import lud0
from .routes.world.routes import world

def create_app():
    app = Flask(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

    log("DayZServlet", "Servlet started!")

    app.register_blueprint(lud0)
    app.register_blueprint(world)

    return app
