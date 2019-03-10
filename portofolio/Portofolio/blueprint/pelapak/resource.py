import json, logging
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal
from . import *
from blueprint import db
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_pelapak = Blueprint('pelapak', __name__)
api = Api(bp_pelapak)

class PelapakResource(Resource):
    def __init__(self):
        pass

    @jwt_required
    # def get(self, id=None):
    def get(self):
        pelapak = get_jwt_claims()

        qry = Pelapaks.query.get(pelapak['id'])
        result = marshal(qry, Pelapaks.response_token)
        return result, 200, {'Content-Type': 'application/json'}
        

    # @jwt_required
    def post(self):
        # if get_jwt_claims()['role'].lower() == 'admin':
            parse = reqparse.RequestParser()
            
            parse.add_argument('username', location='json', required=True)
            parse.add_argument('password', location='json', required=True)
            parse.add_argument('email', location='json', required=True)
            parse.add_argument('phone', location='json', required=True)
            parse.add_argument('role', location='json', default='pelapak')

            args = parse.parse_args()

            pelapaks = Pelapaks(None, args['username'], args['password'], args['email'], args['phone'], args['role'])
            db.session.add(pelapaks)
            db.session.commit()

            return marshal(pelapaks, Pelapaks.response_fields), 200, {'Content-Type': 'application/json'}
        # return {'status': 'UNAUTHORIZED', 'message': 'invalid role'}, 401
    
    @jwt_required
    def put(self):
        pelapak = get_jwt_claims()

        parse =reqparse.RequestParser()
        parse.add_argument('username', location='json', required=True)
        parse.add_argument('password', location='json', required=True)
        parse.add_argument('email', location='json', required=True)
        parse.add_argument('phone', location='json', required=True)

        args = parse.parse_args()


        qry = Pelapaks.query.get(pelapak['id'])

        qry.username = args['username']
        qry.password = args['password']
        qry.email = args['email']
        qry.phone = args['phone']
        db.session.commit()
        return {'message': 'Data diperbarui...', 'input': marshal(qry, Pelapaks.response_fields)}, 200, {'Content-Type': 'application/json'}

    @jwt_required
    def delete(self):#, usernamePenbeli):
        pelapak = get_jwt_claims()
        qry = Pelapaks.query.get(pelapak['id'])

        db.session.delete(qry)
        db.session.commit()
        return {'message': 'Data sudah dihapus...'}, 200, {'Content-Type': 'application/json'}


api.add_resource(PelapakResource, '/pelapak')