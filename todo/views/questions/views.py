from flask import jsonify,abort,make_response,request, url_for
from ...app import app, db
from ...models.tasks.models import tasks
from ...models.quiz.CRUD import CRUDquestion as CRUD
from ...models.quiz.object import Question, Questionnaire, QuestionChoixMultiple, QuestionOpen


@app.route('/todo/api/v1.0/question', methods=['GET'])
def get_all_question():
    questions = [q.to_json() for q in CRUD.get_all_questions()]
    print(questions) 
    return jsonify(questions = questions), 200

@app.route('/todo/api/v1.0/question/<int:id>', methods=['GET'])
def get_question(id):
    question = CRUD.get_question_by_id(id)
    if not question:
        abort(404)
    return jsonify(question.to_json()), 200

@app.route('/todo/api/v1.0/question/byquiz/<int:id>', methods=['GET'])
def get_question_by_quiz(id):
    questions = [q.to_json() for q in CRUD.get_quiz_questions(id)]
    print(questions) 
    return jsonify(questions = questions), 200


@app.route('/todo/api/v1.0/question', methods=['POST'])
def create_question():
    if not request.json or not 'title' in request.json or not 'questionType' in request.json or not 'questionnaire_id' in request.json:
        abort(400)
    data = request.get_json()
    match data['questionType']:
        case 'open':
            question =  QuestionOpen(title=data['title'], questionType=data['questionType'], questionnaire_id=data['questionnaire_id'], reponse=data['reponse'])
        case 'multiple':
            question =  QuestionChoixMultiple(
                title=data['title'], 
                questionType=data['questionType'], 
                questionnaire_id=data['questionnaire_id'], 
                choix1=data['choix1'], 
                choix2=data['choix2'], 
                choix3=data['choix3'],
                choix4=data['choix4'], 
                reponse=data['reponse']
            )
        case _:
            abort(400)
    CRUD.create_question(question)
    return jsonify(questionnaires = [q.to_json() for q in CRUD.get_all_questions()]),201

@app.route('/todo/api/v1.0/question/<int:id>', methods=['PUT'])
def update_question(id):
    question = CRUD.get_question_by_id(id)
    if not question: abort(404)
    if not request.json: abort(400)
    if not 'title' in request.json or not 'questionType' in request.json or not 'questionnaire_id' in request.json: abort(400)
    match question.questionType:
        case 'open':
            question.title = request.json.get('title', question.title)
            question.questionType = request.json.get('questionType', question.questionType)
            question.questionnaire_id = request.json.get('questionnaire_id', question.questionnaire_id)
            question.reponse = request.json.get('reponse', question.reponse)
        case 'multiple':
            question.title = request.json.get('title', question.title)
            question.questionType = request.json.get('questionType', question.questionType)
            question.questionnaire_id = request.json.get('questionnaire_id', question.questionnaire_id)
            question.choix1 = request.json.get('choix1', question.choix1)
            question.choix2 = request.json.get('choix2', question.choix2)
            question.choix3 = request.json.get('choix3', question.choix3)
            question.choix4 = request.json.get('choix4', question.choix4)
            question.reponse = request.json.get('reponse', question.reponse)
        case _:
            abort(400)
    # question.title = request.json.get('title', question.title)
    # question.questionType = request.json.get('questionType', question.questionType)
    # question.questionnaire_id = request.json.get('questionnaire_id', question.questionnaire_id)
    CRUD.update_question(question)
    return jsonify(questionnaires = [q.to_json() for q in CRUD.get_all_questions()]),200

@app.route('/todo/api/v1.0/question/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = CRUD.get_question_by_id(id)
    if not question: abort(404)
    CRUD.delete_question(question)
    return jsonify(questionnaires = [q.to_json() for q in CRUD.get_all_questions()]),200