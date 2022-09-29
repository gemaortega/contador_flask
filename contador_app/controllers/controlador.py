from contador_app import app
from flask import render_template, session, redirect

@app.route('/')
def home():
    if 'counter' in session:
        counter=session["counter"]
        counter = counter +1
        session["counter"]= counter
    else:
        session["counter"]=1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()		
    #session.pop("counter")		
    return redirect('/')



