from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

#Specifying location of db which will be of type sqlite and stored as a file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" 

#No need to track modifications in database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Create instance of database
db = SQLAlchemy(app)
