from flask import Flask
from auth import auth as auth_blueprint
from main import main as main_blueprint
from models import db
from flask_migrate import Migrate
from flask_login import LoginManager
from models.user import User
from input_file import input_file

# init SQLAlchemy so we can use it later in our models


app = Flask(__name__)

app.config["SECRET_KEY"] = "cfd8a3921f67cbe8b3f7e2d31c9d5f4a"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

db.init_app(app)

migrate = Migrate(app=app, db=db)

app.register_blueprint(auth_blueprint)

app.register_blueprint(main_blueprint)

app.register_blueprint(input_file)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


if __name__ == "__main__":
    app.run(debug=True)
