from flask import Flask, render_template, redirect, session, request
app=Flask(__name__)

app.secret_key = ("GreatNumberSession")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/userform', methods=['POST'])
def userinput():
    print(request.form)
    return redirect('/')

if __name__== '__main__':
    app.run(debug=True)