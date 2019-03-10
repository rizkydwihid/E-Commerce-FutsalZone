import random
from flask_restful import fields # untuk fileds di database nya
from blueprint import db # import dari file app --> "challange-resfulll.py"

class Customers(db.Model):
    __tablename__="Customer" # nama tabel di database
    client_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)  # inisialisasi field
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    role = db.Column(db.String(25), nullable=False)
    
    response_fields = {
        'client_id': fields.Integer,
        'username': fields.String,
        'password': fields.String,
        'phone': fields.String,
        'email': fields.String,
        'role': fields.String
    }

    response_token = {
        'client_id': fields.Integer,
        'username': fields.String,
        'password': fields.String,
        'role': fields.String
    }

    def __init__(self, client_id, username, password, phone, email, role):
        self.client_id = client_id
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email 
        self.role = role
        
    def __repr__(self): #inisialisai awal untuk return value
        return '<Customer %r>' % self.client_id # terus nilai balikan dari 1 class ini dikembalikan datanya pake ini