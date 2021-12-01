import flask
import json
from flask import request, jsonify
from extract_data import extractData
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask


sched = BackgroundScheduler(daemon=True)
sched.add_job(extractData,'interval',hours=24)
sched.start()
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.before_request
def init_db_connection():
  extractData()


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to my ARCAFFE App</h1>
    <p> - GET /drinks - Returns the id, name, description and price of all drinks.</p>
    <p> - GET /drink/<id> - Returns id, name, description and price of a drink.</p>
    <p> - GET /pizzas - Returns the id, name, description and price of all pizzas.</p>
    <p> - GET /pizza/<id> - Returns id, name, description and price of a pizza.</p>
    <p> - GET /desserts - Returns the id, name, description and price of all desserts.</p>
    <p> - GET /dessert/<id> - Returns id, name, description and price of a desserts.</p>
    <p>Thank You</p> '''


@app.route('/drinks', methods=['GET'])
def apiGetDrinks():
    with open('drinks_data.json', 'r') as fdr:
        data = json.load(fdr)

    return jsonify(data)

@app.route('/drink/<id>', methods=['GET'])
def apiGetDrink(id):
    with open('drinks_data.json', 'r') as fdr:
        data = json.load(fdr)

        for dish in data:

            if str(dish["dishId"]) == id:
                return jsonify(dish)

    return '''<h1>Error: wrong id number</h1>'''

@app.route('/pizzas', methods=['GET'])
def apiGetPizzas():
    with open('pizzas_data.json', 'r') as fp:
        data = json.load(fp)

    return jsonify(data)

@app.route('/pizza/<id>', methods=['GET'])
def apiGetPizza(id):
    with open('pizzas_data.json', 'r') as fp:
        data = json.load(fp)

        for dish in data:

            if str(dish["dishId"]) == id:
                return jsonify(dish)

    return '''<h1>Error: wrong id number</h1>'''

@app.route('/desserts', methods=['GET'])
def apiGetDesserts():
    with open('desserts_data.json', 'r') as fde:
        data = json.load(fde)

    return jsonify(data)

@app.route('/dessert/<id>', methods=['GET'])
def apiGetDessert(id):
    with open('desserts_data.json', 'r') as fde:
        data = json.load(fde)

        for dish in data:

            if str(dish["dishId"]) == id:
                return jsonify(dish)

    return '''<h1>Error: wrong id number</h1>'''


app.run()