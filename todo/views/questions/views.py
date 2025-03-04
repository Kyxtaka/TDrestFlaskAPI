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
    if not request.json: abort(400)
    if not 'title' in request.json or not 'questionType' in request.json or not 'questionnaire_id' in request.json: abort(400)
    quesiton = Question(title=request.json["title"], questionType=request.json["questionType"], questionnaire_id=request.json["questionnaire_id"])
    CRUDQUIZ.create_question(quesiton)
    return jsonify(questionnaires = [q.to_json() for q in CRUDQUIZ.get_all_questions()]),201  

@app.route('/todo/api/v1.0/question/<int:id>', methods=['PUT'])
def update_question(id):
    question = CRUDQUIZ.get_question_by_id(id)
    if not question: abort(404)
    if not request.json: abort(400)
    if not 'title' in request.json or not 'questionType' in request.json or not 'questionnaire_id' in request.json: abort(400)
    question.title = request.json.get('title', question.title)
    question.questionType = request.json.get('questionType', question.questionType)
    question.questionnaire_id = request.json.get('questionnaire_id', question.questionnaire_id)
    CRUDQUIZ.update_questionnaire(question)
    return jsonify(questionnaires = [q.to_json() for q in CRUDQUIZ.get_all_questions()]),200

@app.route('/todo/api/v1.0/question/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = CRUDQUIZ.get_question_by_id(id)
    if not question: abort(404)
    CRUDQUIZ.delete_questionnaire(question)
    return jsonify(questionnaires = [q.to_json() for q in CRUDQUIZ.get_all_questions()]),200