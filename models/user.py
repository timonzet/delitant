from .database import db
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))
