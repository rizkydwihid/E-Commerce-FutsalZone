import json, logging
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal
from . import *
from blueprint import db
from blueprint.produk import Produk
from blueprint.customer import Customers
from blueprint.cart import Cart
# from blueprint.transaksi import Transaksi
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_cart = Blueprint('cart', __name__)
api = Api(bp_cart)

class CartResource(Resource):
    def __init__(self):
        pass

    @jwt_required
    def get(self,id_cart=None):
        customer = get_jwt_claims()

        if id_cart == None:
            qry_cart = Cart.query.filter_by(cust_id=customer['cust_id']).all()

            keranjang = []
            for row in qry_cart:
                cart = marshal(row, Cart.response_cart)
                keranjang.append(cart)
            return {'status':'OK', 'message':'List of items in your cart', 'cart':keranjang}, 200, {'Content-Type': 'application/jason'}

        else:
            qry_cart = Cart.query.filter_by(cust_id=customer['cust_id']).filter_by(id=cart_id).first()
            if qry_cart is not None:
                cart2 = marshal(qry_cart, Cart.response_cart)
                return {'status':'OK','message':'Get a cart', 'cart':keranjang}, 200, {'Content-Type': 'application/jason'}
            else:
                return {'status':'Not Found!', 'message': 'Data not found'}, 404, {'Content-Type': 'application/json'}

        
    @jwt_required
    def post(self):
        customer = get_jwt_claims()
        parse = reqparse.RequestParser()
        parse.add_argument('produk_id', location='json', type=int,required=True)
        parse.add_argument('qty', location='json', type=int,  required=True)
        
        args = parse.parse_args()
        qry_produk = Produk.query.get(args['produk_id'])
        produk = marshal(qry_produk, Produk.response_fields)

        if qry_produk.stok < args ['qty']:
            return {"status": "Failed", "message": "Item not enough!!", 'cart': marshal(cart_plus, Cart.response_cart)}, 401, {'Content-Type': 'application/json'}

        total_byr = int(produk['harga_bandrol'] * args['qty'])
        status = 'Belum di bayar'
        trans_id = 0
        sisa_barang = int(produk['stok'] - args['qty'])

        qry_produk.stok = sisa_barang
        db.session.commit()
        
        cart_plus = Cart(None, produk['produk_id'], customer['cust_id'], customer['username'], produk['nama_produk'], produk['kategori'], args['qty'],  total_byr, trans_id, status, produk['gambar'])
    
        db.session.add(cart_plus)
        db.session.commit()               

        return {"status": "Created", "message": "Your cart has been created", 'cart': marshal(cart_plus, Cart.response_fields)}, 201, {'Content-Type': 'application/json'}
    
    @jwt_required
    def delete(self, id_cart):
        customer = get_jwt_claims()
        if customer['role'] != 'customer':
            return {"status": "Unauthorized", "message": "Access denied!!"}, 401, {'Content-Type': 'application/json'}

        qry_cart = Cart.query.filter_by(cust_id = customer['cust_id']).filter_by(cart_id = id_cart).first()
        keranjang = marshal(qry_cart, Cart.response_fields)
        keranjang2 = marshal(qry_cart, Cart.response_cart)
        qry_produk = Produk.query.get(keranjang['produk_id'])
        produk = marshal(qry_produk, Produk.response_fields)

        if qry_cart is not None:
            stok_skrg = (qry_produk.stok + qry_cart.qty)
            qry_produk.stok = stok_skrg
            db.session.delete(qry_cart)
            db.session.commit()
            return {'status':'OK', 'cart': keranjang, 'message': 'Delete data success'}, 200, {'Content-Type': 'application/json'}

        else:
            return {'status':'Not Found!', 'message': 'Data not found'}, 404, {'Content-Type': 'application/json'}



api.add_resource(CartResource, '/cart', '/cart/<int:id_cart>')