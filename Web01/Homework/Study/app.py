from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def about_me():
    return render_template("index.html")

@app.route('/school')
def school():
    return redirect(url_for()'http://techkids.vn'))

if __name__ == '__main__':
  app.run(debug=True)
