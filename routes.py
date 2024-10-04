from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/setupD')
def setupD():
    return render_template('setupD.html')

@app.route('/setupH')
def setupH():
    return render_template('setupH.html')

@app.route('/setupP')
def setupP():
    return render_template('setupP.html')