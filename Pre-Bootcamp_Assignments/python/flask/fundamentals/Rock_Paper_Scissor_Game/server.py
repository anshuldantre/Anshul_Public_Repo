from flask import Flask, render_template, redirect, session, request
import random
app=Flask(__name__)

app.secret_key=('Rock_Paper_Scissors')

@app.route('/')
def index():
    if 'draw' not in session:
        session['draw'] = 0
        session['win'] = 0
        session['loses'] = 0
    return render_template("index.html")

@app.route('/selection', methods=['POST'])
def selection():
    rand_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    session['our_choice'] = request.form['selection']
    session['oponnents_choice'] = rand_choice
    print(rand_choice)

# rock beats scissors
# paper beats rock
# scissors beat paper

    if session['our_choice'] == session['oponnents_choice']:
        session['draw'] += 1
        session['current_result'] = 'draw'
    elif session['our_choice'] == 'Rock' and session['oponnents_choice'] == 'Scissors':
        session['win'] += 1
        session['current_result'] = 'win'
    elif session['our_choice'] == 'Paper' and session['oponnents_choice'] == 'Rock':
        session['win'] += 1
        session['current_result'] = 'win'
    elif session['our_choice'] == 'Scissors' and session['oponnents_choice'] == 'Paper':
        session['win'] += 1
        session['current_result'] = 'win'
    else:
        session['loses'] += 1
        session['current_result'] = 'lose'
    return redirect('/')

@app.route('/clear_session')
def clear_Session():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True) 