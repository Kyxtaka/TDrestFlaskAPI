from flask import jsonify,abort,make_response,request, url_for
from ...app import app, db
from ...models.tasks.models import tasks
from ...models.quiz.CRUD import CRUDquiz as CRUD
from ...models.quiz.object import Question, Questionnaire


@app.route('/todo/api/v1.0/quiz', methods=['GET'])
def get_all_questionnaire():
    listQuestionnaire = [q.to_json() for q in CRUD.get_all_questionnaires()]
    print(listQuestionnaire) 
    return jsonify(questionnaires = listQuestionnaire), 200

@app.route('/todo/api/v1.0/quiz/<int:id>', methods=['GET'])
def get_questionnaire(id):
    questionnaire = CRUD.get_questionnaire_by_id(id)
    if not questionnaire:
        abort(404)
    return jsonify(questionnaire.to_json()), 200

@app.route('/todo/api/v1.0/quiz',methods=['POST'])
def create_questionnaire():
    if not request.json or not 'name' in request.json:
        abort(400)
    questionnaire = Questionnaire(name=request.json["name"])
    CRUD.create_questionnaire(questionnaire)
    return jsonify(questionnaires = [q.to_json() for q in CRUD.get_all_questionnaires()]),201  

@app.route('/todo/api/v1.0/quiz/<int:id>',methods=['PUT'])
def update_questionnaire(id):
    questionnaire = CRUD.get_questionnaire_by_id(id)
    if not questionnaire: abort(404)
    if not request.json: abort(400)
    if not 'name' in request.json: abort(400)
    questionnaire.name = request.json.get('name', questionnaire.name)
    CRUD.update_questionnaire(questionnaire)
    return jsonify(questionnaires = [q.to_json() for q in CRUD.get_all_questionnaires()]),200

@app.route('/todo/api/v1.0/quiz/<int:id>', methods=['DELETE'])
def delete_questionnaire(id):
    questionnaire = CRUD.get_questionnaire_by_id(id)
    if not questionnaire:
        abort(404)
    CRUD.delete_questionnaire(questionnaire)
    return jsonify(questionnaires = [q.to_json() for q in CRUD.get_all_questionnaires()]),200