from flask import Flask, session, render_template, request, redirect
import random, datetime
app = Flask(__name__)

app.secret_key = 'NinjaGold'

@app.route('/')
def index_default():
    if 'mytotalgold' not in session:
        session['mytotalgold'] = 0
        session['player_activity_log'] = []
        session['attempts_counter'] = 0
    return render_template('index.html')

def current_timestamp():
    current_date = datetime.datetime.now()
    return current_date.strftime("%Y/%m/%d %I:%M %p")

@app.route('/process_money', methods=["POST"])
def process_money():
    session['attempts_counter'] += 1
    current_outcome = []
    color = "green"

    if (request.form['which_button'] == 'farm') or (request.form['which_button'] == 'cave') or (request.form['which_button'] == 'house'):
        if request.form['which_button'] == 'farm':
            gold_value = random.randint(10,20)
        elif request.form['which_button'] == 'cave': 
            gold_value = random.randint(5,10)
        elif request.form['which_button'] == 'house':
            gold_value = random.randint(2,5)

        session['mytotalgold'] += gold_value
        current_outcome.append({"log":f"Earned {gold_value} golds from the {request.form['which_button']}! {current_timestamp()}","color":color})

    if request.form['which_button'] == 'casino':
        casino_choice = random.choice(['earn', 'give'])
        gold_value = random.randint(0,50)

        if casino_choice == 'earn':
            session['mytotalgold'] += gold_value
            current_outcome.append({"log":f"Entered a Casino and Earned {gold_value} golds....Yeahhhh {current_timestamp()}","color":color})
        else:
            session['mytotalgold'] -= gold_value
            current_outcome.append({"log":f"Entered a Casino and Lost {gold_value} golds....Ouch  {current_timestamp()}","color":"red"})
    current_outcome.extend(session['player_activity_log'])
    session['player_activity_log']=current_outcome

    return redirect('/')

@app.route('/replay')
def replay():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)