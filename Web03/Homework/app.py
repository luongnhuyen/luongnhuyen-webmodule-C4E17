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

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"

@app.route('/remove-all')
def remove_all():
    all_service = Service.objects()
    all_service.delete()
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

@app.route('/gender',methods=['GET','POST'])
def gender():
    if request.method == "GET":
        return render_template('gender.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        if form['gender'] == "male":
            gender = 1
        elif form['gender']== "female":
            gender = 0
        new_service = Service(name=name, yob=yob, phone=phone, gender=gender)
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/update-service/<service_id>',methods=['GET','POST'])
def update_service(service_id):
    all_service = Service.objects.with_id(service_id)
    if request.method == "GET":
        return render_template('update-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']
        phone = form['phone']
        height = form['height']
        status = form['status']
        description = form['description']
        measurements = form['measurements']
        if form['gender'] == "male":
            gender = 1
        elif form['gender']== "female":
            gender = 0
        new_service = Service(name=name,
                              yob=yob,
                              address=address,
                              phone=phone,
                              height=height,
                              status=status,
                              description=description,
                              measurements=measurements,
                              gender=gender)
        new_service.save()
        return redirect(url_for('admin'))


if __name__ == '__main__':
  app.run(debug=True)
