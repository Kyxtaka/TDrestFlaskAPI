from flask import jsonify,abort,make_response,request, url_for
from ...app import app
from ...models.tasks.models import tasks

@app.errorhandler(404)
def not_found(error) :
    return make_response(jsonify({ 'error': 'Not found'}), 404)

@app.errorhandler (400)
def not_found(error ) :
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(405)
def not_found(error) :
    return make_response(jsonify({'error': 'Method not allowed'}), 405)

@app.errorhandler(401)
def not_found(error) :
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(409)
def not_found(error) :
    return make_response(jsonify({'error': 'Conflict'}), 409)

@app.errorhandler(500)
def not_found(error) :
    return make_response(jsonify({'error': 'Internal server error'}), 500)