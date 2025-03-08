from ...app import db
from flask_sqlalchemy import SQLAlchemy 
from .object import Question, QuestionChoixMultiple, QuestionOpen, Questionnaire


## Questions
class CRUDquestion: 
    ###### Questions
    @staticmethod
    def get_all_questions() -> list[Question]:
        return db.session.query(Question).all()

    @staticmethod
    def get_quiz_questions(id) -> list[Question] | None:
        return db.session.query(Question).filter(Question.questionnaire_id==id).all()
    
    @staticmethod
    def get_question_by_id(id: int) -> Question | None:
        return db.session.query(Question).get(id)
    

    @staticmethod
    def create_question(quesstion: Question) -> list[Question] | None:
        try:
            db.session.add(quesstion)
            db.session.commit()
            return quesstion
        except Exception as e:
            db.session.rollback()
            print(e)
            return None

    @staticmethod
    def delete_question(question: Question) -> bool:
        try:
            db.session.delete(question)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(e)
            return False

    @staticmethod
    def update_question(question) -> None:
        try:
            db.session.commit()
            return question
        except Exception as e:
            db.session.rollback()
            print(e)
            return None
    

##Questionnaire
class CRUDquiz:
    @staticmethod
    def get_all_questionnaires() -> list[Questionnaire]:
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
    def delete_questionnaire(questionnaire: Questionnaire) ->  bool:
        try:
            for question in CRUDquestion.get_quiz_questions(questionnaire.id):
                db.session.delete(question)
            db.session.delete(questionnaire)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(e)
            return False
            
    @staticmethod
    def get_questionnaire_by_id(id: int) -> Questionnaire | None:
        return db.session.query(Questionnaire).get(id)
        
    @staticmethod
    def update_questionnaire(questionnaire: Questionnaire) -> None:
        try:
            db.session.commit()
            return questionnaire
        except Exception as e:
            db.session.rollback()
            print(e)
            return None
        