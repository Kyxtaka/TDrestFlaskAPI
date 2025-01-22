from flask import jsonify,abort,make_response,request, url_for
from ...app import app
from ...models import tasks

@app.errorhandler(404)
def not_found(error) :
    return make_response(jsonify({ 'error': 'Not found'}), 404)

@app.errorhandler (400)
def not_found(error ) :
    return make_response(jsonify({'error': 'Bad request'}), 400)