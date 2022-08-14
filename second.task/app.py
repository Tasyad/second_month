from flask import Flask, render_template, request, redirect
from peewee import *
from models import Country

app = Flask(__name__)

@app.route('/') 
def mike():
    all_countries = Country.select()
    return render_template("index.html", countries=all_countries)



if __name__=="__main__":
    app.run(debug=True)
