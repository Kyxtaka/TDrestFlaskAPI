from ...app import db

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.id = Questionnaire.get_next_id()
        self.name = name

    def __repr__(self):
        return "<Questionnaire(%d)%s>" % (self.id, self.name)

    def to_json(self):
        json = {
            'id': self.id,
            'name': self.name
        }
        return json

    @staticmethod
    def get_next_id():
        q = db.session.query(Questionnaire).order_by(Questionnaire.id.desc()).first()
        if q:
            return q.id + 1
        else:
            return 1

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    questionType = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship("Questionnaire", backref=db.backref("questions", lazy="dynamic"))

    __mapper_args__ = {
        'polymorphic_identity': 'question',
        'with_polymorphic': '*',
        'polymorphic_on': questionType
    }

    def __init__(self, title, questionType, questionnaire_id):
        self.id = Question.get_next_id()
        self.title = title
        self.questionType = questionType
        self.questionnaire_id = questionnaire_id

    def get_question_type(self):
        return self.questionType

    @staticmethod
    def get_next_id():
        q = db.session.query(Question).order_by(Question.id.desc()).first()
        if q:
            return q.id + 1
        else:
            return 1

    def to_json(self):
        json = {
            'id': self.id,
            'title': self.title,
            'questionType': self.questionType,
            'questionnaire_id': self.questionnaire_id
        }
        return json

class QuestionChoixMultiple(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    choix1 = db.Column(db.String(120))
    choix2 = db.Column(db.String(120))
    choix3 = db.Column(db.String(120))
    choix4 = db.Column(db.String(120))
    reponse = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity': 'multiple',
        'polymorphic_load': 'inline'
    }

    def __init__(self, title, questionType, questionnaire_id, choix1, choix2, choix3, choix4, reponse):
        super().__init__(title, questionType, questionnaire_id)
        self.choix1 = choix1
        self.choix2 = choix2
        self.choix3 = choix3
        self.choix4 = choix4
        self.reponse = reponse

    def to_json(self):
        json = super().to_json()
        json.update({
            'choix1': self.choix1,
            'choix2': self.choix2,
            'choix3': self.choix3,
            'choix4': self.choix4,
            'reponse': self.reponse
        })
        return json

class QuestionOpen(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    reponse = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity': 'open',
        'polymorphic_load': 'inline'
    }

    def __init__(self, title, questionType, questionnaire_id, reponse):
        super().__init__(title, questionType, questionnaire_id)
        self.reponse = reponse

    def to_json(self):
        json = super().to_json()
        json['reponse'] = self.reponse
        return json