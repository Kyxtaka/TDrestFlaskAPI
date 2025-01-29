from flask import jsonify,abort,make_response,request, url_for
from ...app import app, db
from ...models.tasks.models import tasks
from ...models.quiz.CRUD import CRUDQUIZ
from ...models.quiz.object import Question, Questionnaire


@app.route('/todo/api/v1.0/quiz/all', methods=['GET'])
def get_question():
    return jsonify(questionnaires=[q for q in CRUDQUIZ.get_all_questionnaires()]), 200


@app.route('/todo/api/v1.0/quiz/add',methods=['POST'])
def create_questionnaire():
    if not request.json or not 'name' in request.json:
        abort(400)
    questionnaire = CRUDQUIZ.create_questionnaire(Questionnaire(id=Questionnaire.get_next_id(), name=request.json['name']))
    return jsonify({'question': CRUDQUIZ.create_questionnaire(Questionnaire)}),201  