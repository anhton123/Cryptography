from flask import Flask, render_template
from Rsa import *
from test import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/h')
def h():
    return bye(5, 4)

@app.route('/encrypt')
def encrypt():
    # RSA: CHECK P AND Q NEED TO BE PRIME AND 23 97
    b = rsa_encrypt("sonny", 23, 97)
    d = str(b[1][0])
    n = str(b[1][1])
    c = str(b[0])
    w = ''
    for t in b[0]:
        w += t

    return render_template("encrypt.html", d=d, n=n, c=c, w=w)

@app.route('/decrypt')
def decrypt():
    return
if __name__ == "__main__":
    app.run(debug=True)
