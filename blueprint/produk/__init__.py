import random
from flask_restful import fields # untuk fileds di database nya
from blueprint import db

class Produk(db.Model):
    __tablename__="Produk" # nama tabel di database
    produk_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)  # inisialisasi field
    nama_produk = db.Column(db.String(100), nullable=False)
    kategori = db.Column(db.String(50), nullable=False)
    merk = db.Column(db.String(50), nullable=False)
    stok = db.Column(db.Integer, nullable=False)
    harga_distri = db.Column(db.Float, nullable=False)
    harga_bandrol = db.Column(db.Float, nullable=False)
    warna = db.Column(db.String(100), nullable=False)
    ukuran = db.Column(db.Integer,nullable=False)
    gambar = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.Text)
    
    response_fields = {
        'produk_id': fields.Integer,
        'nama_produk': fields.String,
        'kategori': fields.String,
        'merk': fields.String,
        'stok': fields.Integer,
        'harga_distri': fields.Float,
        'harga_bandrol': fields.Float,
        'warna': fields.String,
        'ukuran': fields.Integer,
        'gambar': fields.String,
        'deskripsi': fields.String
    }

    def __init__(self, produk_id, nama_produk, kategori, merk, stok, harga_distri, harga_bandrol, warna, ukuran, gambar, deskripsi):
        self.produk_id = produk_id
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.merk = merk
        self.stok = stok
        self.harga_distri = harga_distri
        self.harga_bandrol = harga_bandrol
        self.warna = warna
        self.ukuran = ukuran
        self.gambar = gambar
        self.deskripsi = deskripsi 
        
    def __repr__(self): 
        return '<Produk %r>' % self.produk_id 