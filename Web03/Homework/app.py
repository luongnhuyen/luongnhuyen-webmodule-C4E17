from flask import *
from mongoengine import *
from Models.service import Service
import mlab

app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',all_service = all_service)

@app.route('/new-service',methods=['GET','POST'])
def creat():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        new_service = Service(name=name, yob=yob)
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/remove-all')
def remove_all():
    db.Service.remove({})
    return redirect(url_for('admin'))

@app.route('/service-page')
def service_page():
    all_service = Service.objects()
    return render_template('service-page.html',all_service = all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    all_service = Service.objects.with_id(service_id)
    return redirect(url_for('searchid',id=service_id))

@app.route('/<id>')
def searchid(id):
    all_service = Service.objects(id=id)
    return render_template('searchid.html',all_service=all_service)

@app.route('/gender')
def gender():
    return render_template('gender.html')



if __name__ == '__main__':
  app.run(debug=True)
