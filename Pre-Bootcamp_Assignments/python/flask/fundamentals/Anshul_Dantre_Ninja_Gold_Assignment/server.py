from flask import Flask, session, render_template, request, redirect
import random, datetime
app = Flask(__name__)

app.secret_key = 'NinjaGold'

@app.route('/')
def index_default():
    if 'mytotalgold' not in session:
        session['mytotalgold'] = 0
    # print(f'session[mytotalgold] = {session["mytotalgold"]}')
    # print(f'session[player_activity_log] = {session["player_activity_log"]}')
    return render_template('index.html')

def current_timestamp():
    current_date = datetime.datetime.now()
    return current_date.strftime("%Y/%m/%d %I:%M %p")

@app.route('/process_money', methods=["POST"])
def process_money():
    current_date = datetime.datetime.now()
    print(current_date.strftime("%Y/%m/%d %I:%M %p"))

    if 'player_activity_log' not in session:
        session['player_activity_log'] = []

    if request.form['which_button'] == 'farm':
        farm_gold_earned = random.randint(10,20)
        # print(f'Total gold earned in farm {farm_gold_earned}')
        session['mytotalgold'] += farm_gold_earned
        session['player_activity_log'].append({"log":f"Earned {farm_gold_earned} golds from the farm! {current_timestamp()}","color":"green"})

    if request.form['which_button'] == 'cave':
        cave_gold_earned = random.randint(5,10)
        # print(f'Total gold earned in cave {cave_gold_earned}')
        session['mytotalgold'] += cave_gold_earned
        session['player_activity_log'].append({"log":f"Earned {cave_gold_earned} golds from the Cave! {current_timestamp()}","color":"green"})

    if request.form['which_button'] == 'house':
        house_gold_earned = random.randint(2,5)
        # print(f'Total gold earned in house {house_gold_earned}')
        session['mytotalgold'] += house_gold_earned
        session['player_activity_log'].append({"log":f"Earned {house_gold_earned} golds from the house! {current_timestamp()}","color":"green"})

    if request.form['which_button'] == 'casino':
        casino_choice = random.choice(['earn', 'give'])
        casino_gold_value = random.randint(0,50)
        print(f'This time in casino, you {casino_choice} {casino_gold_value} gold')
        if casino_choice == 'earn':
            session['mytotalgold'] += casino_gold_value
            session['player_activity_log'].append({"log":f"Entered a Casino and Earned {casino_gold_value} golds....Yeahhhh {current_timestamp()}","color":"green"})
        else:
            session['mytotalgold'] -= casino_gold_value
            session['player_activity_log'].append({"log":f"Entered a Casino and Lost {casino_gold_value} golds....Ouch {current_timestamp()}","color":"red"})

    return redirect('/')

@app.route('/replay')
def replay():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)