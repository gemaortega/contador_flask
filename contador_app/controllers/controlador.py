from contador_app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    return render_template('index.html')



