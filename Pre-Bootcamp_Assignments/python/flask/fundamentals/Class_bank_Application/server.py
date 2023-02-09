from flask import Flask, render_template, request, redirect, session
from bank_model import Bank

app=Flask(__name__)
app.secret_jey = "i love coding"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("create_bank", methods=["POST"])
def create_bank():
    print(request.form)
    data = {
        'name' : request.form['name'],
        'address' : request.form['address'],
        'phone' : request.form['phone']
    }
    Bank.save(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)