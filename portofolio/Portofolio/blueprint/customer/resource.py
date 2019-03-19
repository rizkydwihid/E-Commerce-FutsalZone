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
    def get(self, client_id=None):
        
            if client_id == None:
                if get_jwt_claims()['role'].lower() == 'pelapak': # get data by role pelapak (admin)
                    parser = reqparse.RequestParser()
                    parser.add_argument('p', type=int, location='args', default=1)
                    parser.add_argument('rp', type=int, location='args', default=5)

                    args = parser.parse_args()

                    # pagination
                    offset = (args['p'] * args['rp']) - args['rp'] 
                    qry = Customers.query
                    list_cust = []
                    for row in qry.limit(args['rp']).offset(offset).all(): # iterasi data satu per satu
                        list_cust.append(marshal(row, Customers.response_fields))
                    return {'message':'Data all customer..','list cust':list_cust } ,  200, {'Content-Type': 'application/json'}
                return {'status': 'UNAUTHORIZED', 'message': 'Only admin can opened data!!'}, 401

            else:
                if get_jwt_claims()['role'].lower() == 'pelapak': #get data by role pelapak
                    qry = Customers.query.get(client_id) 
                    if qry is not None:
                        return marshal(qry, Customers.response_fields), 200, {'message':'Data customer by id..','Content-Type': 'application/json'} # langsung di ambil 1 data by id
                    else:
                        return "Data Not Found", 200, {'Content-Type': 'application/json'}


                elif get_jwt_claims()['role'].lower() == 'customer': #get data by role customer
                    qry = Customers.query.get(client_id) 
                    if qry is not None:
                        return marshal(qry, Customers.response_fields), 200, {'message':'Data customer by id..','Content-Type': 'application/json'}# langsung di ambil 1 data by id
                    else:
                        return "Data Not Found", 200, {'Content-Type': 'application/json'}



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

            return marshal(customers, Customers.response_fields), 200, {'message':'New data entered..','Content-Type': 'application/json'}
    
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
        return {'message':'Update data success..', 'input': marshal(qry, Customers.response_fields)}, 200, {'Content-Type': 'application/json'}

    @jwt_required
    def delete(self):#, usernamePenbeli):
        if get_jwt_claims()['role'].lower() == 'pelapak':
            customer = get_jwt_claims()
            qry = Customers.query.get(customer['client_id'])

            db.session.delete(qry)
            db.session.commit()
            return {'message':'Delete data success..',}, 200, {'Content-Type': 'application/json'}
        
        elif get_jwt_claims()['role'].lower() == 'customer':
            customer = get_jwt_claims()
            qry = Customers.query.get(customer['client_id'])

            db.session.delete(qry)
            db.session.commit()
            return {'message':'Delete data success..',}, 200, {'Content-Type': 'application/json'}



api.add_resource(CustomerResource, '/customer', '/customer/<int:client_id>')