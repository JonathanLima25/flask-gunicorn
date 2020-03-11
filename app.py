from flask import Flask, jsonify, current_app

app = Flask(__name__)

@app.route('/')
def index():
    response = current_app.make_response("Hello")
    response.set_cookie('name', value='Jonathan')   
    return response

@app.route('/xml/')
def xml():
    return "<use name='Jonathan'/>", {'Content-type':'application/xml'}

@app.route('/json/')
def json():
    return jsonify(user={'name': 'Jonathan'})
