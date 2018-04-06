import smtplib
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")




@app.route("/send", methods = ['POST', 'GET'])
def sendMail():
    if request.method == 'POST':
        print("khuch aya")
        result = request.form
        print(result)
        fromaddr = 'aphometutionsno1@gmail.com'
        toaddrs = 'aphometutionsno1@gmail.com'

        msg = "\r\n".join([
            "From: aphometutionsno1@gmail.com",
            "To: aphometutionsno1@gmail.com",
            "Subject: AP Home Tuyion",
            "",str(result)
        ])

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('aphometutionsno1@gmail.com', 'Prateek@12')
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        return "1"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug = True)

