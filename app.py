## https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc
# https://github.com/dushan14/books-store
# PostGre
# user: kelu
# table db_res

# Creating postgre from csv
# https://www.dataquest.io/blog/loading-data-into-postgres/

import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import *

@app.route("/")
def hello():
    return "Coucou World!"

@app.route("/get/<depcom_>")
def get_by_id(depcom_):
    try:
        population=PopCSV.query.filter_by(depcom=depcom_).first()
        return jsonify(population.serialize())
    except Exception as e:
	    return(str(e))

@app.route("/add/form",methods=['GET', 'POST'])
def add_pop_form():
    if request.method == 'POST':
        code=request.form.get('code')
        nom=request.form.get('nom')
        population=request.form.get('population')
        try:
            pop=Population(
                code=code,
                nom=nom,
                population=population
            )
            db.session.add(pop)
            db.session.commit()
            return "Pop added. ID ={}".format(pop.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")

if __name__ == '__main__':
    app.run()
