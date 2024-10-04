from app import app

app.config['FLASK_DEBUG'] = True
app.config['SECRET_KEY'] = "IntelGenAI"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 