from flask import render_template, request
from portfolio import app 

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/data-science')
def data_science():
    return render_template('data_science.html', title="Data Science")

@app.route('/nlp')
def nlp():
    return render_template('nlp.html', title="NLP")

@app.route('/kaggle')
def kaggle():
    return render_template('kaggle.html', title='Kaggle')

@app.route('/javascript')
def javascript():
    return render_template('javascript.html', title='JavaScript')

@app.route('/flask')
def flask():
    return render_template('flask.html', title='Flask')

@app.route('/unity')
def unity():
    return render_template('unity.html', title='Unity')
