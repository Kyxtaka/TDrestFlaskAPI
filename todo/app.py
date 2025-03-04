from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
def mkpath (p):
    return os.path.normpath(
        os.path.join(os.path.dirname(__file__ ),p)
    )

# app.config['SECRET_KEY'] = "1f371826-9114-495d-bde8-0fd605e6356d"
app.config['TESTING'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('./quizz.db')) #Fichier DB actuelle (solution fonctionnelle)
cors = CORS(app , resources ={r"/todo/api/v1.0/*": {"origins": "*" }})
# db = SQLAlchemy(app)
# if db: print('working on dbTD') #
db = SQLAlchemy(app)
