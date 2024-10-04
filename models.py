from app import app
from config import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Account(db.Model):
    mail = db.Column(db.String(64), nullable=False, unique=True, primary_key = True)
    password = db.Column(db.String(256), nullable=False)
    type = db.Column(db.String(32), nullable=False, default='PATIENT')

    r_users = db.Relationship('Patient', backref='account')
    r_hospitals = db.Relationship('Hospital', backref='account')
    r_doctors = db.Relationship('Doctor', backref='account')
    r_admins = db.Relationship('Admin', backref='account')

class Patient(db.Model):
    mail = db.Column(db.String(64), db.ForeignKey('account.mail'), nullable=False)
    id = db.Column(db.String(32), nullable=False, unique=True, primary_key= True)
    name = db.Column(db.String(256))
    age = db.Column(db.Integer, db.CheckConstraint('age > 0 AND age < 100'), nullable=False)
    gender = db.Column(db.String(1), nullable=False)

    r_patients = db.Relationship('Case', backref='patient')

class Doctor(db.Model):
    mail = db.Column(db.String(64), db.ForeignKey('account.mail'), nullable=False)
    id = db.Column(db.String(32), nullable=False, unique=True, primary_key= True)
    name = db.Column(db.String(512), nullable=False)
    specialty = db.Column(db.String(256), nullable=False, default='General')

    r_special = db.Relationship('Disease', backref='doctor')
    r_sched = db.Relationship('Schedule', backref='doctor')

class Admin(db.Model):
    mail = db.Column(db.String(64), db.ForeignKey('account.mail'), nullable=False)
    id = db.Column(db.String(32), nullable=False, unique=True, primary_key= True)
    name = db.Column(db.String(512), nullable=False)

class Hospital(db.Model):
    mail = db.Column(db.String(64), db.ForeignKey('account.mail'), nullable=False)
    name = db.Column(db.String(512), nullable=False)
    id = db.Column(db.String(32), nullable=False, unique=True, primary_key= True)
    address = db.Column(db.Text)
    phone = db.Column(db.String(10))

    r_schedtime = db.Relationship('Schedule', backref='hospital')

class Schedule(db.Model):
    id = db.Column(db.String(32), nullable=False, unique=True, primary_key= True)
    doctor = db.Column(db.String(32), db.ForeignKey('doctor.id'), nullable=False)
    hospital = db.Column(db.String(32), db.ForeignKey('hospital.id'), nullable=False)
    sunstart = db.Column(db.DateTime)
    sunstop = db.Column(db.DateTime)
    monstart = db.Column(db.DateTime)
    monstop = db.Column(db.DateTime)
    tuestart = db.Column(db.DateTime)
    tuestop = db.Column(db.DateTime)
    wedstart = db.Column(db.DateTime)
    wedstop = db.Column(db.DateTime)
    thurstart = db.Column(db.DateTime)
    thurstop = db.Column(db.DateTime)
    fristart = db.Column(db.DateTime)
    fristop = db.Column(db.DateTime)
    satstart = db.Column(db.DateTime)
    satstop = db.Column(db.DateTime)

    r_schedule = db.Relationship('Appointment', backref='schedule')

class Disease(db.Model):
    id = db.Column(db.String(32), nullable=False, unique=True, primary_key= True)
    name = db.Column(db.String(512), nullable=False)
    specialty = db.Column(db.String(256), db.ForeignKey('doctor.specialty'), nullable=False, default='General')
    description = db.Column(db.Text)
    f1 = db.Column(db.String(256))
    f2 = db.Column(db.String(256))
    f3 = db.Column(db.String(256))
    f4 = db.Column(db.String(256))

    r_disease = db.Relationship('Case', backref='disease')

class Case(db.Model):
    id = db.Column(db.String(32), nullable=False, unique=True, primary_key= True)
    patient = db.Column(db.String(32), db.ForeignKey('patient.id'), nullable=False)
    disease = db.Column(db.String(32), db.ForeignKey('disease.id'), nullable=False)
    severity = db.Column(db.Float)
    detail = db.Column(db.DateTime, nullable=True)

    r_case = db.Relationship('Appointment', backref='case')

class Appointment(db.Model):
    id = db.Column(db.String(32), nullable=False, unique=True, primary_key= True)
    case = db.Column(db.String(32), db.ForeignKey('case.id'), nullable=False)
    schedule = db.Column(db.String(32), db.ForeignKey('schedule.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

with app.app_context():
    db.create_all()