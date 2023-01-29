from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    print(request.form['name'])
    return redirect('/show')

@app.route('/show')
def show_user():
    print('Showing the user info from the form')
    print(request.form)
    return render_template("show.html")


if __name__ == '__main__':
    app.run(debug=True)