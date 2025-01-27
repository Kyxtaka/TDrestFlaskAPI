from flask import jsonify,abort,make_response,request, url_for
from ...app import app, db
from ...models.tasks.models import tasks
from ...models.quiz.CRUD import CRUDQUIZ
from ...models.quiz.object import Question, Questionnaire


@app.route('/todo/api/v1.0/question/all', methods=['GET'])
def get_question():
    return jsonify(questions=[q for q in CRUDQUIZ.get_all_questions()])



@app.route('/todo/api/v1.0/question/add',methods=['POST'])
def create_questionnaire():
    if not request.json or not 'name' in request.json:
        abort(400)
    question = Question(name=request.json['name'])
    return jsonify({'question': CRUDQUIZ.create_question(question)}),201