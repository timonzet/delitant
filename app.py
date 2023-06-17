from flask import Flask, render_template
from auth import auth as auth_blueprint
from main import main as main_blueprint
from models import db
from flask_migrate import Migrate
from flask_login import LoginManager
from models.user import User
from input_file import input_file


application = Flask(__name__)

application.config["SECRET_KEY"] = "cfd8a3921f67cbe8b3f7e2d31c9d5f4a"
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

db.init_app(application)

migrate = Migrate(app=application, db=db)

application.register_blueprint(auth_blueprint)

application.register_blueprint(main_blueprint)

application.register_blueprint(input_file)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(application)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)
