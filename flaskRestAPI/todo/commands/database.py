import click
from ..app import app, db
from ..models.quiz.CRUD import CRUDquiz, CRUDquestion
from ..models.quiz.object import Question, Questionnaire, QuestionChoixMultiple, QuestionOpen


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
        print("Questionnaire created:", q)
    except Exception as e:
        print("Error: ", e)
        db.session.rollback()

#Commande de creation de question
@app.cli.command()
@click.argument('questionnaire_id')
@click.argument('title')
@click.argument('reponse')
def create_question_open(questionnaire_id, title, reponse):
    try:
        q = QuestionOpen(title=title, questionType="open", questionnaire_id=questionnaire_id, reponse=reponse)
        db.session.add(q)
        db.session.commit()
        print("Question created:", q)
    except Exception as e:
        print("Error: ", e)
        db.session.rollback()

#Commande de creation de question choix multiple
@app.cli.command()
@click.argument('questionnaire_id')
@click.argument('title')
@click.argument('choix1')
@click.argument('choix2')
@click.argument('choix3')
@click.argument('choix4')
@click.argument('reponse')
def create_question_multiple(questionnaire_id, title, choix1, choix2, choix3, choix4, reponse):
    try:
        q = QuestionChoixMultiple(title=title, questionType="multiple", questionnaire_id=questionnaire_id, choix1=choix1, choix2=choix2, choix3=choix3, choix4=choix4, reponse=reponse)
        db.session.add(q)
        db.session.commit()
        print("Question created:", q)
    except Exception as e:
        print("Error: ", e)
        db.session.rollback()

#Ccommande pour drop la bd
@app.cli.command()
def dropdb():
    db.drop_all()
    print("Database dropped")