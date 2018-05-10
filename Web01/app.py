from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts= [
        {
            "title": "Thơ con cóc",
            "content": "Hello",
            "author": "Yen",
            "gender": 1
        },
        {
            "title": "Thơ con cóc",
            "content": "Hello",
            "author": "Yen",
            "gender": 0
        },
        {
            "title": "Thơ con cóc",
            "content": "Hello",
            "author": "Yen",
            "gender": 1
        }
        ]

    return render_template("index.html",posts=posts)

@app.route('/c4e')
def sayhi():
    return "Hi C4E 17"

@app.route('/sayhi/<name>/<age>')
def hi(name,age):
    return "Hi {0}, you are {1} yr olds".format(name,age)

@app.route('/sum/<int:a>/<int:b>')
def total(a,b):
    return str(a + b)


if __name__ == '__main__':
  app.run(debug=True)
