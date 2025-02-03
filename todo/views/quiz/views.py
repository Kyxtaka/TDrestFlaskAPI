from flask import jsonify,abort,make_response,request, url_for
from ...app import app, db
from ...models.tasks.models import tasks
from ...models.quiz.CRUD import CRUDQUIZ
from ...models.quiz.object import Question, Questionnaire


@app.route('/todo/api/v1.0/quiz/all', methods=['GET'])
def get_question():
    listTask = [q.to_json() for q in CRUDQUIZ.get_all_questionnaires()]
    print(listTask) 
    return jsonify(listTask), 200


@app.route('/todo/api/v1.0/quiz/add',methods=['POST'])
def create_questionnaire():
    if not request.json or not 'name' in request.json:
        abort(400)
    questionnaire = Questionnaire(id=Questionnaire.get_next_id(), name=request.json['name'])
    CRUDQUIZ.create_questionnaire(questionnaire)
    return jsonify({'question': CRUDQUIZ.create_questionnaire(Questionnaire)}),201  