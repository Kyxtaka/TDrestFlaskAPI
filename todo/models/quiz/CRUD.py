from ...app import db
from flask_sqlalchemy import SQLAlchemy 
from .object import Question
from .object import Questionnaire


## Questions
class CRUDQUIZ: 
    ###### Questions
    @staticmethod
    def get_all_questions():
        return db.session.query(Question).all()

    @staticmethod
    def create_question(quesstion: Question):
        db.session.add(quesstion)
        db.session.commit()
        return quesstion

    @staticmethod
    def delete_question(question: Question):
        db.session.delete(question)
        db.session.commit()
        return question
    
    @staticmethod
    def get_question_by_id(id: int):
        return db.session.query(Question).filter(Question.id==id).first()

    @staticmethod
    def update_question(question):
        db.session.commit()
        return question
    
    ##Questionnaire
    @staticmethod
    def get_all_questionnaires():
        return db.session.query(Questionnaire).all()

    @staticmethod
    def create_questionnaire(questionnaire: Questionnaire):
        try:
            db.session.add(questionnaire)
            db.session.commit()
            return questionnaire
        except Exception as e:
            print(e)
            return None    
    @staticmethod
    def delete_questionnaire(questionnaire: Questionnaire):
        db.session.delete(questionnaire)
        db.session.commit()
        return questionnaire
    
    @staticmethod
    def get_questionnaire_by_id(id: int):
        return db.session.query(Questionnaire).filter(Questionnaire.id==id).first()
    
    @staticmethod
    def update_questionnaire(questionnaire: Questionnaire):
        db.session.commit()
        return questionnaire