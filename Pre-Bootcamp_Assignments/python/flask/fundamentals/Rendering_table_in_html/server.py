from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def display_list():
    friends_info = [
        {"name":"Anshul", "age":38},
        {"name":"Shradha","age":36},
        {"name":"Rahul","age":35},
        {"name":"Komal","age":32},
        {"name":"Avinash","age":35},
        {"name":"Astha","age":33}
    ]
    return render_template('lists.html',friends=friends_info, random_numbers=[1,3,5,7,9])

if __name__== '__main__':
    app.run(debug=True)