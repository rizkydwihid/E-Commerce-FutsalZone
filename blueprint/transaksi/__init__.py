import random, logging
from blueprint import db
from flask_restful import fields

class Transaksis(db.Model):
    __tablename__ = "Transaksis"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    cust_id = db.Column(db.Integer, nullable=False)
    nama_custom = db.Column(db.String(255), nullable=False)
    total_bayar= db.Column(db.Integer, nullable=False)

    response_fields = {
        'id' : fields.Integer,
        'cust_id' : fields.Integer,
        'nama_custom': fields.String,
        'total_bayar' : fields.Integer
    }

    def __init__(self, id, cust_id, nama_custom, total_bayar):
        self.id = id
        self.cust_id = cust_id
        self.nama_custom = nama_custom
        self.total_bayar = total_bayar

    def __repr__(self):
        return '<Transaksi %d>' % self.id