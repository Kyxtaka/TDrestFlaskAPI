from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
def mkpath (p):
    return os.path.normpath(
        os.path.join(os.path.dirname(__file__ ),p)
    )

app.config['TESTING'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('./quizz.db')) #Fichier DB actuelle (solution fonctionnelle)
cors = CORS(app , resources ={r"/todo/api/v1.0/*": {"origins": "*" }})
db = SQLAlchemy(app)
