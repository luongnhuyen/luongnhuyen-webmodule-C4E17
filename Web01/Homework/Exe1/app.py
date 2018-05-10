from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    kq=weight/(height/100*height/100)

# Cach 1
    if kq < 16:
        ketqua = "Severely underweight"
    elif kq < 18.5:
        ketqua = "Underweight"
    elif kq < 25:
        ketqua = "Normal"
    elif kq < 30:
        ketqua = "Overweight"
    else:
        ketqua = "Obese"
    return "{0} {1}".format(kq,ketqua)

#Cach 2
    # return render_template("index.html",kq=kq)

if __name__ == '__main__':
  app.run(debug=True)
