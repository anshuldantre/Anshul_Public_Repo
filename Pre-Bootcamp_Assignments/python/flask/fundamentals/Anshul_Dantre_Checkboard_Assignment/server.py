from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html',a=8,b=8)

@app.route('/<int:x_axis>')
def checkerboard_x(x_axis):
    return render_template('index.html',a=x_axis,b=x_axis)

@app.route('/<int:x_axis>/<int:y_axis>')
def checkerboard_x_y(x_axis,y_axis):
    return render_template('index.html',a=x_axis,b=y_axis)

@app.route('/<int:x_axis>/<int:y_axis>/<string:color1>/<string:color2>')
def checkerboard_x_y_color(x_axis,y_axis,color1,color2):
    return render_template('index.html', a=x_axis, b=y_axis, col1=color1, col2=color2)

if __name__=="__main__":
    app.run(debug=True)