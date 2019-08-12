from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)

  app.config['SECRET_KEY'] = 'thisisasecretdonotcopy'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

  db.init_app(app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  # Can't be imported at top b/c db is not yet initialized at that point
  from .models import User

  # Necessary to find user with current active session

  @login_manager.user_loader
  def load_user(user_id):
    # Loads user associated with current cookie
    return User.query.get(int(user_id))

  # Blueprint for authenticated areas

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  # Blueprint for non-authenticated areas

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app
