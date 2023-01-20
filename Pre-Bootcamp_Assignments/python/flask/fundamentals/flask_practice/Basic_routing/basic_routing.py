from flask import Flask
app = Flask(__name__)

# routing to default port i.e. 5000
@app.route('/')
def default_route():
    return "This is the default route for a HTTP port i.e. 80. For https the default port is 443."

# Routing to a specific method
@app.route('/hello')
def hello():
    return "Hello, Welcome to Flask Demo !"

# Routing with an input, by default every input is a string
@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello {name}, You are now learning Flask"

# options if we want to pass some input as an integer
@app.route('/hello_num/<int:num>')
def hello_num(num):
    return f"You have provided a number input, i.e. {num}."

# How to pass more than one input
@app.route('/repeat_hello/<string:name>/<int:num>')
def hello_repeat(name,num):
    return f" Hello {name} !" * num

if __name__ == "__main__":
    app.run(debug=True)

        # app.run(debug=True, port=5001) 
            # This is how we change the PORT configuration. Default port in 5000. Below mentioned is how the logs looks
            # PS E:\Dojo\Pre-Bootcamp_Public\Pre-Bootcamp_Assignments\python\flask\fundamentals\flask_practice\Basic_routing> python basic_routing.py
            #  * Serving Flask app 'basic_routing'
            #  * Debug mode: on
            # WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
            #  * Running on http://127.0.0.1:5001
            # Press CTRL+C to quit
            #  * Restarting with stat
            #  * Debugger is active!
            #  * Debugger PIN: 118-286-123
            # 127.0.0.1 - - [19/Jan/2023 07:13:42] "GET / HTTP/1.1" 200 -

