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
    def get_quiz_questions(id):
        return db.session.query(Question).filter(Question.questionnaire_id==id).all()

    @staticmethod
    def create_question(quesstion: Question):
        try:
            db.session.add(quesstion)
            db.session.commit()
            return quesstion
        except Exception as e:
            db.session.rollback()
            print(e)
            return None

    @staticmethod
    def delete_question(question: Question):
        try:
            db.session.delete(question)
            db.session.commit()
            return question
        except Exception as e:
            db.session.rollback()
            print(e)
            return None
    
    @staticmethod
    def get_question_by_id(id: int):
        return db.session.query(Question).filter(Question.id==id).first()

    @staticmethod
    def update_question(question):
        try:
            db.session.commit()
            return question
        except Exception as e:
            db.session.rollback()
            print(e)
            return None
    
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
            db.session.rollback()
            print(e)
            return None    
        
    @staticmethod
    def delete_questionnaire(questionnaire: Questionnaire):
        try:
            for question in CRUDQUIZ.get_quiz_questions(questionnaire.id):
                db.session.delete(question)
            db.session.delete(questionnaire)
            db.session.commit()
            return questionnaire
        except Exception as e:
            db.session.rollback()
            print(e)
            return None
            
    @staticmethod
    def get_questionnaire_by_id(id: int):
        return db.session.query(Questionnaire).filter(Questionnaire.id==id).first()
        
    @staticmethod
    def update_questionnaire(questionnaire: Questionnaire):
        try:
            db.session.commit()
            return questionnaire
        except Exception as e:
            db.session.rollback()
            print(e)
            return None