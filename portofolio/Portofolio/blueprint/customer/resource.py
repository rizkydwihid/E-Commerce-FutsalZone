import json, logging
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal
from . import *
from blueprint import db
from flask_jwt_extended import jwt_required, get_jwt_claims

bp_customer = Blueprint('customer', __name__)
api = Api(bp_customer)

class CustomerResource(Resource):
    def __init__(self):
        pass

    @jwt_required
    # def get(self, id=None):
    def get(self):
        customer = get_jwt_claims()

        qry = Customers.query.get(customer['client_id'])
        result = marshal(qry, Customers.response_token)
        return result, 200, {'Content-Type': 'application/json'}
        

    # @jwt_required
    def post(self):
        # if get_jwt_claims()['role'].lower() == 'admin':
            parse = reqparse.RequestParser()
            
            parse.add_argument('username', location='json', required=True)
            parse.add_argument('password', location='json', required=True)
            parse.add_argument('email', location='json', required=True)
            parse.add_argument('phone', location='json', required=True)
            parse.add_argument('role', location='json', default='customer')

            args = parse.parse_args()

            customers = Customers(None, args['username'],args['password'], args['email'], args['phone'], args['role'])
            db.session.add(customers)
            db.session.commit()

            return marshal(customers, Customers.response_fields), 200, {'Content-Type': 'application/json'}
        # return {'status': 'UNAUTHORIZED', 'message': 'invalid role'}, 401
    
    @jwt_required
    def put(self):
        customer = get_jwt_claims()

        parse =reqparse.RequestParser()
        parse.add_argument('username', location='json', required=True)
        parse.add_argument('password', location='json', required=True)
        parse.add_argument('email', location='json', required=True)
        parse.add_argument('phone', location='json', required=True)

        args = parse.parse_args()


        qry = Customers.query.get(customer['client_id'])

        qry.username = args['username']
        qry.password = args['password']
        qry.email = args['email']
        qry.phone = args['phone']
        db.session.commit()
        return {'message': 'Data diperbarui...', 'input': marshal(qry, Customers.response_fields)}, 200, {'Content-Type': 'application/json'}

    @jwt_required
    def delete(self):#, usernamePenbeli):
        customer = get_jwt_claims()
        qry = Customers.query.get(customer['client_id'])

        db.session.delete(qry)
        db.session.commit()
        return {'message': 'Data sudah dihapus...'}, 200, {'Content-Type': 'application/json'}


api.add_resource(CustomerResource, '/customer')