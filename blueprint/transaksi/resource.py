import json, logging
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from . import *
from blueprint import db
from blueprint.customer import Customers
from blueprint.cart import Cart
from blueprint.transaksi import Transaksis
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_trans = Blueprint('Transaksi', __name__)
api = Api(bp_trans)

class Transaksi(Resource):

    @jwt_required
    def post(self):
        customer = get_jwt_claims()
        if customer['role'] != 'customer':
            return {"status": "Unauthorized", "message": "Access Denied"}, 401, {'Content-Type': 'application/json'}

        qry_cart = Cart.query.filter_by(cust_id=customer['cust_id']).filter_by(status='Belum di bayar').filter_by(transaksi_id=0)
        total_bayar = 0
        if qry_cart.first() is None:
            return {"status": "Bad Request", "message": "You haven't any unpaid cart"}, 400, {'Content-Type': 'application/json'}

        else:
            for temp in qry_cart.all():
                total_bayar = total_bayar + temp.total_byr
            # print(total_bayar)
            tr = Transaksis(None, customer['cust_id'], customer['username'], total_bayar)
            db.session.add(tr)
            db.session.commit()
            
            cartList = []
            for cart in qry_cart:
                cart.transaksi_id = tr.id
                cart.status = "Sudah bayar"
                cart = marshal(cart, Cart.response_cart)
                cartList.append(cart)
            db.session.commit()

            transaksi = marshal(tr, Transaksis.response_fields)
            return {"status": "Accepted", "message": "Your transaction is success", 'transaction': transaksi, 'carts': cartList}, 202, {'Content-Type': 'application/json'}
    
    @jwt_required
    def get(self, transaksi_id=None):
        customer = get_jwt_claims()
        if customer['role'] != 'customer':
            return {"status": "Unauthorized", "message": "Access Denied"}, 401, {'Content-Type': 'application/json'}
        
        if transaksi_id == None:
            qry_transaksi = Transaksis.query.filter_by(cust_id=customer['cust_id']).all()
            
            transaksi = []
            cartList = []
            for row in qry_transaksi:
                qry_cart = Cart.query.filter_by(transaksi_id=row.id).all()
                
                for cart in qry_cart:
                    tempCart = marshal(cart, Cart.response_cart)
                    cartList.append(tempCart)
                
                temp = marshal(row, Transaksis.response_fields)
                temp['details'] = cartList
                transaksi.append(temp)
                cartList = []
            
            return {'status':'OK', 'message':'Your All Transactions', 'transactions': transaksi}, 200, {'Content-Type': 'application/jason'}
        
        else:
            qry_transaksi = Transaksis.query.filter_by(cust_id=customer['cust_id']).filter_by(id=transaksi_id).first()
            if qry_transaksi is not None:
                temp = marshal(qry_transaksi, Transaksis.response_fields)
                return {'status':'OK', 'message':'Your Transaction', 'transaction': temp}, 200, {'Content-Type': 'application/jason'}

            else:
                return {'status':'Not Found!', 'message': 'DATA_NOT_FOUND'}, 404, {'Content-Type': 'application/json'}

    ##### Endpoint Cart-Pembeli
api.add_resource(Transaksi, '/transaksi', '/transaksi/<int:transaksi_id>')