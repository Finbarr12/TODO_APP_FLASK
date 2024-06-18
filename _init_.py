from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SECRET_KEY'] = "catty"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"

db=SQLAlchemy(app)


from views.UserController import user_bp
app.register_blueprint(user_bp)

