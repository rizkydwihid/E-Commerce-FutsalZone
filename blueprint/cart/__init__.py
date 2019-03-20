import random
from flask_restful import fields # untuk fileds di database nya
from blueprint import db # import dari file app --> "challange-resfulll.py"

class Cart(db.Model):
    __tablename__="Cart" # nama tabel di database
    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)  # inisialisasi field
    produk_id = db.Column(db.Integer, nullable=False)
    nama_cust = db.Column(db.String(100), nullable=False)
    kategori = db.Column(db.String(50), nullable=False)
    jml_qty = db.Column(db.Float, nullable=False)
    total_byr = db.Column(db.Float, nullable=False)
    ukuran = db.Column(db.Integer,nullable=False)
    deskripsi = db.Column(db.Text)
    # role = db.Column(db.String(25), nullable=False)
    
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
        return '<cart %r>' % self.cart_id 