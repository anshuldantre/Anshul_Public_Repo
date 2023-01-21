from flask import Flask, render_template
app=Flask(__name__)

@app.route('/<int:num>/<string:name>')
def print_name(num, name):
    return render_template('index.html', num=num, name=name)

if __name__ == "__main__":
    app.run(debug=True)