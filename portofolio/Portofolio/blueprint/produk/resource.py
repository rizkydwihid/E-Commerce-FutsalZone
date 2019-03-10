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
    # def get(self, id=None):
    def get(self):
        produk = get_jwt_claims()

        qry = Produk.query.get(produk['produk_id'])
        result = marshal(qry, Produk.response_fields)
        return result, 200, {'Content-Type': 'application/json'}
        

    @jwt_required
    def post(self):
        if get_jwt_claims()['role'].lower() == 'pelapak':
            parse = reqparse.RequestParser()
            
            parse.add_argument('nama_produk', location='json', required=True)
            parse.add_argument('kategori', location='json', required=True)
            parse.add_argument('harga', location='json', required=True)
            parse.add_argument('deskripsi', location='json', required=True)
            # parse.add_argument('role', location='json', default='customer')

            args = parse.parse_args()

            produks = Produk(None, args['nama_produk'],args['kategori'], args['harga'], args['deskripsi'])
            db.session.add(produks)
            db.session.commit()

            return marshal(produks, Produk.response_fields), 200, {'Content-Type': 'application/json'}
        # return {'status': 'UNAUTHORIZED', 'message': 'invalid role'}, 401
    
    @jwt_required
    def put(self):
        produks = get_jwt_claims()

        parse =reqparse.RequestParser()
        parse.add_argument('nama_produk', location='json', required=True)
        parse.add_argument('kategori', location='json', required=True)
        parse.add_argument('harga', location='json', required=True)
        parse.add_argument('deskripsi', location='json', required=True)

        args = parse.parse_args()


        qry = Produk.query.get(customer['produk_id'])

        qry.nama_produk = args['nama_produk']
        qry.kategori = args['kategori']
        qry.harga = args['harga']
        qry.deskripsi = args['deskripsi']
        db.session.commit()
        return {'message': 'Data diperbarui...', 'input': marshal(qry, Produk.response_fields)}, 200, {'Content-Type': 'application/json'}

    @jwt_required
    def delete(self):#, usernamePenbeli):
        produks = get_jwt_claims()
        qry = Produk.query.get(produks['produk_id'])

        db.session.delete(qry)
        db.session.commit()
        return {'message': 'Data sudah dihapus...'}, 200, {'Content-Type': 'application/json'}


api.add_resource(ProdukResource, '/produk')