from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<username>')
def username(username):
    users = {
	   "quy" :      {
			             "name" : "Dinh Cong Quy",
			             "age" : 20
                    },
    "tuananh" :     {
			             "name" : "Huynh Tuan Anh",
			             "age" : 22
                    }
            }
    if username in users.keys():
        return render_template('index.html', users = users[username])
    else:
        return "User not found"



if __name__ == '__main__':
  app.run(debug=True)
