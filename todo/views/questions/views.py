from flask import jsonify,abort,make_response,request, url_for
from ...app import app, db
from ...models.tasks.models import tasks
from ...models.quiz.CRUD import CRUDQUIZ
from ...models.quiz.object import Question, Questionnaire


@app.route('/todo/api/v1.0/question', methods=['GET'])
def get_all_question():
    questions = [q.to_json() for q in CRUDQUIZ.get_all_questions()]
    print(questions) 
    return jsonify(questions = questions), 200

@app.route('/todo/api/v1.0/question/<int:id>', methods=['GET'])
def get_question(id):
    question = CRUDQUIZ.get_question_by_id(id)
    if not question:
        abort(404)
    return jsonify(question.to_json()), 200

@app.route('/todo/api/v1.0/question/byquiz/<int:id>', methods=['GET'])
def get_question_by_quiz(id):
    questions = [q.to_json() for q in CRUDQUIZ.get_quiz_questions(id)]
    print(questions) 
    return jsonify(questions = questions), 200



@app.route('/todo/api/v1.0/question', methods=['POST'])
def create_question():
    if not request.json or not 'name' in request.json:
        abort(400)
    quesiton = Question(name=request.json["name"], questionType=request.json["questionType"], questionnaire_id=request.json["questionnaire_id"])
    CRUDQUIZ.create_question(questionnaire)
    return jsonify(questionnaires = [q.to_json() for q in CRUDQUIZ.get_all_questions()]),201  

@app.route('/todo/api/v1.0/question/<int:id>', methods=['PUT'])
def update_question(id):
    questionnaire = CRUDQUIZ.get_question_by_id(id)
    if not questionnaire:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    questionnaire.name = request.json.get_all_questions('name', questionnaire.name)
    CRUDQUIZ.update_questionnaire(questionnaire)
    return jsonify(questionnaires = [q.to_json() for q in CRUDQUIZ.get_all_questions()]),200

@app.route('/todo/api/v1.0/question/<int:id>', methods=['DELETE'])
def delete_question(id):
    questionnaire = CRUDQUIZ.get_questionnaire_by_id(id)
    if not questionnaire:
        abort(404)
    CRUDQUIZ.delete_questionnaire(questionnaire)
    return jsonify(questionnaires = [q.to_json() for q in CRUDQUIZ.get_all_questions()]),200