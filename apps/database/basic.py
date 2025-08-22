import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# __file__ is name of this file
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Puppy(db.Model):
    __tablename__ = "puppies"