from flask import Flask, render_template, request
from Asymmetric.Rsa import rsa_encrypt, rsa_decrypt
from Hashing.Md5 import md5_hash
from Hashing.Sha2 import sha2_hash
from Symmetric.Aes import aes_encrypt, aes_decrypt
from Symmetric.Des import des_encrypt, des_decrypt
from test import *
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    # First on launch page + refresh
    if request.method == "GET":
        return render_template("index.html")
    
    # After form selected
    else:
        way = request.form.get("type")

        if way == "RSA":
            txt = request.form.get("txt")
            p = request.form.get("p")
            q = request.form.get("q")
            answer = rsa_encrypt(txt, int(p), int(q))

        if way == "AES":
            key = request.form.get("key")
            txt = request.form.get("txt")
            answer = aes_encrypt(key, txt)

        if way == "DES":
            key = request.form.get("key")
            txt = request.form.get("txt")
            answer = des_encrypt(key, txt)

        if way == "MD5":
            txt = request.form.get("txt")
            answer = md5_hash(txt)

        if way == "SHA":
            txt = request.form.get("txt")
            answer = sha2_hash(txt)

        if way == "RSA-d":
            txt = request.form.get("txt")
            d = request.form.get("d")
            n = request.form.get("n")
            answer = rsa_decrypt(txt, int(d), int(n))

        if way == "AES-d":
            key = request.form.get("key")
            txt = request.form.get("txt")
            answer = aes_decrypt(key, txt)

        if way == "DES-d":
            key = request.form.get("key")
            txt = request.form.get("txt")
            answer = des_decrypt(key, txt)

        return render_template("index.html", txt = "Output: " + str(answer))

@app.route('/h')
def h():
    return bye(5, 4)

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == "GET":
        return render_template("encrypt.html")
    if request.method == "POST":
        # Gets information on type of cipher used
        way = request.form.get("type")

        if way == "RSA":
            txt = request.form.get("txt")
            p = request.form.get("p")
            q = request.form.get("q")
            answer = rsa_encrypt(txt, int(p), int(q))

        if way == "AES":
            key = request.form.get("key")
            txt = request.form.get("txt")
            answer = aes_encrypt(key, txt)

        if way == "DES":
            key = request.form.get("key")
            txt = request.form.get("txt")
            answer = des_encrypt(key, txt)

        if way == "MD5":
            txt = request.form.get("txt")
            answer = md5_hash(txt)

        if way == "SHA":
            txt = request.form.get("txt")
            answer = sha2_hash(txt)

        return render_template("index.html", txt = answer)

@app.route('/decrypt', methods = ["GET", "POST"])
def decrypt():
    if request.method == "GET":
        return render_template("decrypt.html")
    if request.method == "POST":
        # Gets information on type of cipher used
        way = request.form.get("type")

        if way == "RSA":
            txt = request.form.get("txt")
            d = request.form.get("d")
            n = request.form.get("n")
            answer = rsa_decrypt(txt, int(d), int(n))

        if way == "AES":
            key = request.form.get("key")
            txt = request.form.get("txt")
            answer = aes_decrypt(key, txt)

        if way == "DES":
            key = request.form.get("key")
            txt = request.form.get("txt")
            answer = des_decrypt(key, txt)

        return render_template("index.html", txt = answer)

if __name__ == "__main__":
    app.run(debug=True)
