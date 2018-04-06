import smtplib
from flask import Flask, render_template, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return render_template("index.html")




@app.route("/send", methods = ['POST', 'GET'])
def sendMail():
    if request.method == 'POST':
        try:
            print("khuch aya")
            result = request.form
            print(result)
            a= open("demo", "w+")
            a.write(str(result)+"\n\n")
            return "it is working"
        except:
            print("exception")
            return "1"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug = True)

