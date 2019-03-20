import random
from flask_restful import fields # untuk fileds di database nya
from blueprint import db

class Produk(db.Model):
    __tablename__="Produk" # nama tabel di database
    produk_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)  # inisialisasi field
    nama_produk = db.Column(db.String(100), nullable=False)
    kategori = db.Column(db.String(50), nullable=False)
    harga = db.Column(db.Float, nullable=False)
    warna = db.Column(db.String(100), nullable=False)
    ukuran = db.Column(db.Integer,nullable=False)
    deskripsi = db.Column(db.Text)
    
    response_fields = {
        'produk_id': fields.Integer,
        'nama_produk': fields.String,
        'kategori': fields.String,
        'harga': fields.Float,
        'warna': fields.String,
        'ukuran': fields.Integer,
        'deskripsi': fields.String
        # 'role': fields.String
    }

    def __init__(self, produk_id, nama_produk, kategori, harga, warna, ukuran, deskripsi):
        self.produk_id = produk_id
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.harga = harga
        self.warna = warna
        self.ukuran = ukuran
        self.deskripsi = deskripsi 
        # # self.role = role
        
    def __repr__(self): 
        return '<Produk %r>' % self.produk_id 