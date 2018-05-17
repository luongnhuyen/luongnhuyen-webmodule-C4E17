from flask import *
from mongoengine import *
from Models.service import Service
import mlab

app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g, yob__lte=2000, address__icontains="Hà Nội")
    return render_template('search.html', all_service=all_service)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',all_service = all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"

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


if __name__ == '__main__':
  app.run(debug=True)
