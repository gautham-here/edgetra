from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    mail = request.form.get('mail')
    password = request.form.get('password')

    if not username or not password:
        flash('Please fill out all fields')
        return redirect(url_for('login'))
    
    user = User.query.filter_by(username=username).first()
    
    if not user:
        flash('Username does not exist')
        return redirect(url_for('login'))
    
    if not check_password_hash(user.passhash, password):
        flash('Incorrect password')
        return redirect(url_for('login'))
    
    session['user_id'] = user.id
    flash('Login successful')
    return redirect(url_for('index'))

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

@app.route('/h_dash')
def h_dash():
    return render_template('h_dash.html')

@app.route('/d_dash')
def d_dash():
    return render_template('d_dash.html')

@app.route('/d_panel')
def d_panel():
    return render_template('d_panel.html')

@app.route('/h_add')
def h_add():
    return render_template('h_add.html')

