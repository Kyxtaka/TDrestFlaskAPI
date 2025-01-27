import click
from ..app import app, db
from ..models.quiz.CRUD import CRUDQUIZ
from ..models.quiz.object import Question, Questionnaire


#Commande de creation de table
@app.cli.command()
def syncdb():
    db.create_all()