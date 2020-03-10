from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Not Found", 404, {'X-hello':'world'}

@app.route('/xml/')
def xml():
    return "<use name='Jonathan'/>", {'Content-type':'application/xml'}
