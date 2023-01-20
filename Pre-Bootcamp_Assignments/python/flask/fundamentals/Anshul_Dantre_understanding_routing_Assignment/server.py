from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:num>/<string:text>')
def pattern(num,text):
    return f'{num * text}'

@app.errorhandler(404)
def page_not_found(e):
    return "Invalid Page, Please check the URL!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.