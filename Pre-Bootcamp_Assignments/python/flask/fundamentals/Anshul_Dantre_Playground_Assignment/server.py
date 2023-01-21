from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def base_page():
    return "This is a base route page"

# @app.route('/play')
# def level1():
#     return render_template("index1.html")

# @app.route('/play/<int:num>')
# def level2(num):
#     return render_template('index2.html', no_of_boxes=num)

# @app.route('/play/<int:num>/<string:colour>')
# def level3(num, colour):
#     return render_template('index3.html', no_of_boxes=num, box_color=colour)

@app.route('/play')
def level1():
    return render_template("index4.html", no_of_boxes=3, box_color="blue")

@app.route('/play/<int:num>')
def level2(num):
    return render_template('index4.html', no_of_boxes=num, box_color="green")

@app.route('/play/<int:num>/<string:colour>')
def level3(num, colour):
    return render_template('index4.html', no_of_boxes=num, box_color=colour)

if __name__ == "__main__":
    app.run(debug=True)