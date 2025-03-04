from flask import jsonify,abort,make_response,request, url_for
from ...app import app, db
from ...models.tasks.models import tasks
from ...models.quiz.CRUD import CRUDQUIZ
from ...models.quiz.object import Question, Questionnaire


@app.route('/todo/api/v1.0/quiz', methods=['GET'])
def get_all_questionnaire():
    listQuestion = [q.to_json() for q in CRUDQUIZ.get_all_questionnaires()]
    print(listQuestion) 
    return jsonify(questionnaires = listQuestion), 200

@app.route('/todo/api/v1.0/quiz/<int:id>', methods=['GET'])
def get_questionnaire(id):
    questionnaire = CRUDQUIZ.get_questionnaire_by_id(id)
    if not questionnaire:
        abort(404)
    return jsonify(questionnaire.to_json()), 200


@app.route('/todo/api/v1.0/quiz',methods=['POST'])
def create_questionnaire():
    if not request.json or not 'name' in request.json:
        abort(400)
    questionnaire = Questionnaire(name=request.json["name"])
    CRUDQUIZ.create_questionnaire(questionnaire)
    return jsonify(questionnaires = [q.to_json() for q in CRUDQUIZ.get_all_questionnaires()]),201  

@app.route('/todo/api/v1.0/quiz/<int:id>',methods=['PUT'])
def update_questionnaire(id):
    questionnaire = CRUDQUIZ.get_questionnaire_by_id(id)
    if not questionnaire:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    questionnaire.name = request.json.get('name', questionnaire.name)
    CRUDQUIZ.update_questionnaire(questionnaire)
    return jsonify(questionnaires = [q.to_json() for q in CRUDQUIZ.get_all_questionnaires()]),200

@app.route('/todo/api/v1.0/quiz/<int:id>', methods=['DELETE'])
def delete_questionnaire(id):
    questionnaire = CRUDQUIZ.get_questionnaire_by_id(id)
    if not questionnaire:
        abort(404)
    CRUDQUIZ.delete_questionnaire(questionnaire)
    return jsonify(questionnaires = [q.to_json() for q in CRUDQUIZ.get_all_questionnaires()]),200