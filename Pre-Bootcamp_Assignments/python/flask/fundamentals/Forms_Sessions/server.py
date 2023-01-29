from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['name']
    session['age'] = request.form['age']
    session['email'] = request.form['email']

    return redirect('/show')

@app.route('/show')
def show_user():
    print('Showing the user info from the form')
    return render_template("show.html", name_on_template=session['name'], age_on_template = session['age'], email_on_template = session['email'])

if __name__ == '__main__':
    app.run(debug=True)