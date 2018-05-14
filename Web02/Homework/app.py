from flask import Flask, render_template
from mongoengine import *
from Models.service import Service
import mlab

app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<id>')
def searchid(id):
    all_service = Service.objects(id=id)
    return render_template('searchid.html',all_service=all_service)

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g)
    return render_template('search.html', all_service=all_service)

@app.route('/customer/<c>')
def customer(c):
    all_service = Service.objects(contacted=c,gender=1)
    return render_template('customer.html',all_service=all_service)

if __name__ == '__main__':
  app.run(debug=True)
