from flask import Flask, jsonify, request, url_for, redirect, session, render_template
import numpy as np
import pandas as pd


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'


@app.route('/', methods=['POST', 'GET'], defaults={'name' : 'Default'})
@app.route('/<string:name>', methods=['POST', 'GET'])
def index(name):
    session['name'] = name
    return render_template('index.html', name=name, tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/pag1', methods=['POST', 'GET'], defaults={'name' : 'Default'})
@app.route('/pag1/<string:name>', methods=['POST', 'GET'])
def pag1(name):
    session['name'] = name
    return render_template('pag1.html', name=name,)



@app.route('/simple', methods=["POST", "GET"])
def html_table():
    return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)


###################################################################################################

df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})


if __name__ == '__main__':
    app.run()