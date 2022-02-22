# Worked with Joe Onghena 
from flask import render_template, Flask, request

app = Flask(__name__)
names_organizations = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    name = request.form.get('name', 'Nothing')
    organization = request.form.get('organization', 'Nothing')
    names_organizations[name] = organization
    return render_template('submit.html', names_organizations=names_organizations)
