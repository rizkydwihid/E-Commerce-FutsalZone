import random
from flask_restful import fields # untuk fileds di database nya
from blueprint import db # import dari file app --> "challange-resfulll.py"

class Cart(db.Model):
    __tablename__="Cart" # nama tabel di database
    cart_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)  # inisialisasi field
    produk_id = db.Column(db.Integer, nullable=False)
    cust_id = db.Column(db.Integer, nullable=False)
    nama_cust = db.Column(db.String(100), nullable=False)
    nama_barang = db.Column(db.String(100), nullable=False)
    kategori = db.Column(db.String(100), nullable=False)
    qty = db.Column(db.Float, nullable=False)
    total_byr = db.Column(db.Float, nullable=False)
    transaksi_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    gambar = db.Column(db.String(255), nullable=False)
    
    response_fields = {
        'cart_id': fields.Integer,
        'produk_id': fields.Integer,
        'cust_id': fields.Integer,
        'nama_cust': fields.String,
        'nama_barang': fields.String,
        'kategori': fields.String,
        'qty': fields.Float,
        'total_byr': fields.Float,
        'transaksi_id': fields.Integer,
        'status': fields.String,
        'gambar': fields.String
    }
    response_cart= {
        'cart_id': fields.Integer,
        'nama_cust': fields.String,
        'nama_barang': fields.String,
        'kategori': fields.String,
        'transaksi_id': fields.Integer,
        'gambar': fields.String,
        'qty': fields.Float,
        'total_byr': fields.Float,
        'status': fields.String
    }

    def __init__(self, cart_id, produk_id, cust_id, nama_cust, nama_barang, kategori, qty, total_byr, transaksi_id, status, gambar):
        self.cart_id = cart_id
        self.produk_id = produk_id
        self.cust_id = cust_id
        self.nama_cust = nama_cust
        self.nama_barang = nama_barang
        self.kategori = kategori
        self.qty = qty
        self.total_byr = total_byr
        self.transaksi_id = transaksi_id
        self.status = status
        self.gambar = gambar

    def __repr__(self): 
        return '<cart %r>' % self.cart_id 