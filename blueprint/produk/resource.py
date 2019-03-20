import json, logging
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal
from . import *
from blueprint import db
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_produk = Blueprint('produk', __name__)
api = Api(bp_produk)

class ProdukResource(Resource):
    def __init__(self):
        pass

    # @jwt_required
    def get(self,produk_id=None):

        if produk_id == None:
            parser = reqparse.RequestParser()
            parser.add_argument('p', type=int, location='args', default=1)
            parser.add_argument('rp', type=int, location='args', default=5)
            
            args = parser.parse_args()

            # pagination
            offset = (args['p'] * args['rp']) - args['rp'] 
            qry = Produk.query
            list_produk = []
            for row in qry.limit(args['rp']).offset(offset).all(): # iterasi data satu per satu
                list_produk.append(marshal(row, Produk.response_fields))
            return {'message':'Data all product..','list produk':list_produk } ,  200, {'Content-Type': 'application/json'}

        else:

            qry = Produk.query.get(produk_id) # mirip dengan --> "select * from Users where id = id"
            if qry is not None:
                return marshal(qry, Produk.response_fields), 200, {'message':'Data product by id..','Content-Type': 'application/json'} # langsung di ambil 1 data by id
            else:
                return "Data Not Found", 200, {'Content-Type': 'application/json'}
        

    @jwt_required
    def post(self):
        if get_jwt_claims()['role'].lower() == 'pelapak':
            parse = reqparse.RequestParser()
            
            parse.add_argument('nama_produk', location='json', required=True)
            parse.add_argument('kategori', location='json', required=True)
            parse.add_argument('harga', location='json', required=True)
            parse.add_argument('warna', location='json', required=True)
            parse.add_argument('ukuran', location='json', required=True)
            parse.add_argument('deskripsi', location='json', required=True)

            args = parse.parse_args()

            produks = Produk(None, args['nama_produk'],args['kategori'], args['harga'], args['warna'], args['ukuran'], args['deskripsi'])
            db.session.add(produks)
            db.session.commit()

            return marshal(produks, Produk.response_fields), 200, {'message':'Submit data product, success!!','Content-Type': 'application/json'}
    
    @jwt_required
    def put(self, produk_id):
        produks = get_jwt_claims()

        parse =reqparse.RequestParser()
        parse.add_argument('nama_produk', location='json', required=True)
        parse.add_argument('kategori', location='json', required=True)
        parse.add_argument('harga', location='json', required=True)
        parse.add_argument('warna', location='json', required=True)
        parse.add_argument('ukuran', location='json', required=True)
        parse.add_argument('deskripsi', location='json', required=True)

        args = parse.parse_args()


        qry = Produk.query.get(produk_id)

        qry.nama_produk = args['nama_produk']
        qry.kategori = args['kategori']
        qry.harga = args['harga']
        qry.warna = args['warna']
        qry.ukuran = args['ukuran']
        qry.deskripsi = args['deskripsi']
        db.session.commit()
        return {'message': 'Update data success..', 'input': marshal(qry, Produk.response_fields)}, 200, {'Content-Type': 'application/json'}

    @jwt_required
    def delete(self, produk_id):
        produks = get_jwt_claims()
        qry = Produk.query.get(produk_id)

        db.session.delete(qry)
        db.session.commit()
        return {'message': 'Delete data success..'}, 200, {'Content-Type': 'application/json'}


api.add_resource(ProdukResource, '/produk', '/produk/<int:produk_id>')