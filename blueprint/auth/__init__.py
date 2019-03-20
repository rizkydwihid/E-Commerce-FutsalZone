import logging, json
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprint.customer import *
from blueprint.pelapak import *


bp_auth = Blueprint('auth', __name__)
api = Api(bp_auth)

# token untuk customer
class CreateTokenResources(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='args',required=True)
        parser.add_argument('password', location='args', required=True)
        args = parser.parse_args()

        qry = Customers.query.filter_by(username=args['username']).filter_by(
            password=args['password']).first()

        if qry is not None:
            token = create_access_token(identity=marshal(qry, Customers.response_fields))
        else:
            return {'status': 'UNAUTORIZED', 'message': 'invalid username or password'}, 401
        return {'message':'This is your token. Save and keep, thanks..','token': token}, 200

# token untuk pelapak (admin)
class TokenPelapakResources(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='args',required=True)
        parser.add_argument('password', location='args', required=True)
        args = parser.parse_args()

        qry = Pelapaks.query.filter_by(username=args['username']).filter_by(
            password=args['password']).first()

        if qry is not None:
            token = create_access_token(identity=marshal(qry, Pelapaks.response_fields))
        else:
            return {'status': 'UNAUTORIZED', 'message': 'invalid username or password'}, 401
        return {'message':'This is your token. Save and keep, thanks..','token': token}, 200

api.add_resource(CreateTokenResources, '/tokencustomer')
api.add_resource(TokenPelapakResources, '/tokenpelapak')