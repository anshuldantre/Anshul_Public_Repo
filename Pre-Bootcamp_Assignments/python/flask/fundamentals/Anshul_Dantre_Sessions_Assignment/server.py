from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = ('MySession')

@app.route('/')
def index():
    if 'click_count' not in session:
        session['click_count'] = 0
    session['click_count'] += 1
    return render_template('index.html')

@app.route('/userclick', methods=['POST'])
def userclick():
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/bytwo', methods=['POST'])
def addtwo():
    if 'click_count' in session:
        session['click_count'] += 1
    return redirect('/')

@app.route('/userincrement', methods=['POST'])
def userincrement():
    if 'click_count' in session:
        session['click_count'] += int(request.form['user_num']) -1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)