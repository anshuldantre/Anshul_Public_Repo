import random
from flask import Flask, render_template, redirect, session, request
app=Flask(__name__)

app.secret_key = ("GreatNumberSession")

@app.route('/')
def index():
    if 'RandomNum' not in session:
        session['RandomNum'] = random.randint(1,100)
        session['noofattempt'] = 1
    # print(session['RandomNum'])
    return render_template("index.html")

@app.route('/userform', methods=['POST'])
def userinput():
    print(request.form)
    print(int(request.form['numinput']))
    session['numinput'] = int(request.form['numinput'])
    session['noofattempt'] += 1
    print('--------------------------------------------------')
    # if session['RandomNum'] > int(request.form['numinput']):
    #     session['msg']='Too Low'
    #     session['col']=1
    # elif session['RandomNum'] < int(request.form['numinput']):
    #     session['msg']='Too High'
    #     session['col']=2
    # else:
    #     session['msg']= f'{request.form["numinput"]} Was the number'
    #     session['col']=3
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__== '__main__':
    app.run(debug=True)