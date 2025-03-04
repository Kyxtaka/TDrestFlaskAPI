import click
from ..app import app, db
from ..models.quiz.CRUD import CRUDQUIZ
from ..models.quiz.object import Question, Questionnaire


#Commande de creation de table
@app.cli.command()
def syncdb():
    db.create_all()

#Commande de creation de questionnaire
@app.cli.command()
@click.argument('name')
def create_questionnaire(name):
    try:
        q = Questionnaire(name=name)
        db.session.add(q)
        db.session.commit()
        print("Questionnaire created")
    except Exception as e:
        print("Error: ", e)
        db.session.rollback()

#Commande de creation de question
@app.cli.command()
@click.argument('questionnaire_id')
@click.argument('title')
@click.argument('open')
def create_question(questionnaire_id, title, open):
    try:
        q = Question(title=title, questionType=open, questionnaire_id=questionnaire_id)
        db.session.add(q)
        db.session.commit()
        print("Question created")
    except Exception as e:
        print("Error: ", e)
        db.session.rollback()