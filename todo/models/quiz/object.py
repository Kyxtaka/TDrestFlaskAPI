from ...app import db

class Questionnaire(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    
    def __init__(self,name):
        self.id=Questionnaire.get_next_id()
        self.name=name
    
    def __repr__(self):
        return"<Questionnaire(%d)%s>"%(self.id,self.name)
    
    def to_json(self):
        json={
        'id':self.id,
        'name':self.name
        }
        return json
    
    @staticmethod
    def get_next_id():
        q=db.session.query(Questionnaire).order_by(Questionnaire.id.desc()).first()
        if q:
            return q.id+1
        else:
            return 1
    
class Question(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(120))
    questionType=db.Column(db.String(120))
    questionnaire_id=db.Column(db.Integer,db.ForeignKey('questionnaire.id'))
    questionnaire=db.relationship("Questionnaire",backref=db.backref("questions",lazy="dynamic"))

    def __init__(self, title, questionType, questionnaire_id):
        self.id=Question.get_next_id()
        self.title=title
        self.questionType=questionType
        self.questionnaire_id=questionnaire_id

    @staticmethod
    def get_next_id():
        q=db.session.query(Question).order_by(Question.id.desc()).first()
        if q:
            return q.id+1
        else:
            return 1