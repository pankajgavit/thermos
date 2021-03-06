from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension
from .config import config_by_name

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'auth.login'

toolbar = DebugToolbarExtension()

moment = Moment()


def createapp(configname):
    app = Flask(__name__)
    app.config.from_object(config_by_name[configname])
    db.init_app(app)
    toolbar.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .bookmarks import bookmarks as bookmarks_blueprint
    app.register_blueprint(bookmarks_blueprint, url_prefix='/bookmarks')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app
