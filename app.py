# coding: utf-8

# Imports needed by the application
from flask import Flask, render_template, flash
import json
from json2html import *

# Personal import
import slimpay

# Const parameter used in the json2html.convert in order to beautify the render
beautify = "class=\"table table-bordered table-hover\""

app = Flask(__name__)

'''The following @app.route('/*') defines the urls handled by the application
Every url that doesnt appear in the following list will be considered as a 404 and be redirect to this page
'''


@app.route('/')
def index():
    bearer = slimpay.get_bearer()
    return render_template('index.html')


@app.route('/get_orders')
def web_get_orders():
    python_data = slimpay.get_orders()
    validjson = json2html.convert(json=python_data, table_attributes=beautify)
    return render_template('get_orders.html', data=validjson)


@app.route('/get_card_transactions')
def web_get_card_transactions():
    python_data = slimpay.get_card_transactions()
    validjson = json2html.convert(json=python_data, table_attributes=beautify)
    return render_template('get_card_transactions.html', data=validjson)


@app.route('/get_card_aliases')
def web_get_card_aliases():
    python_data = slimpay.get_card_aliases()
    validjson = json2html.convert(json=python_data, table_attributes=beautify)
    return render_template('get_card_aliases.html', data=validjson)


@app.route('/create_orders')
def web_create_orders():
    python_data = slimpay.create_orders()
    validjson = json2html.convert(json=python_data, table_attributes=beautify)
    return render_template('create_orders.html', data=validjson)


# Handle the 404 - Not Found error
@app.errorhandler(404)
def web_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
