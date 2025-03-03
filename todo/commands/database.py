import click
from ..app import app, db
from ..models.quiz.CRUD import CRUDQUIZ
from ..models.quiz.object import Question, Questionnaire


#Commande de creation de table
@app.cli.command()
def syncdb():
    db.create_all()

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

    @app.cli.commant()
    @click.argument('questionnaire_id')
    @click.argument('question')
    @click.argument('open 0 or 1')
    def create_question(questionnaire_id, question, open):
        try:
            q = Question(questionnaire_id=questionnaire_id, question=question, open=open)
            db.session.add(q)
            db.session.commit()
            print("Question created")
        except Exception as e:
            print("Error: ", e)
            db.session.rollback()