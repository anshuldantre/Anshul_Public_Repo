from flask import Flask, render_template
chap = Flask(__name__)

@chap.route('/<string:name>/<int:num>')
def hello_world(name, num):
    return render_template('hello.html', var1=name, var2=num)

if __name__ == "__main__":
    chap.run(debug=True)