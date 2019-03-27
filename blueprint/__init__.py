from flask import Flask, request, url_for, Blueprint
from flask_restful import Resource, Api, reqparse #, abort
from time import strftime
from datetime import timedelta
import json, logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager



# initiate flask-restful instance
app = Flask(__name__)
# database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@3.1.96.237:3306/portofolio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'SFsieaaBsLEpecP675r243faM8oSB2hV'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return identity

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

api = Api(app, catch_all_404s=True)

@app.after_request
def after_request(response):
    if request.method == 'GET':
        app.logger.warning("REQUEST LOG\t%s", 
        json.dumps({
            'request': request.args.to_dict(),
            'response': json.loads(response.data.decode('utf-8'))
            })
        )
    else:
        app.logger.warning("REQUEST LOG\t%s",
        json.dumps({
            'request': request.get_json(),
            'response': json.loads(response.data.decode('utf-8'))
            })
        )
    return response

from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from . import *
from blueprint import db

# Call Blueprint
from blueprint.customer.resource import bp_customer
from blueprint.auth import bp_auth
from blueprint.pelapak.resource import bp_pelapak
from blueprint.produk.resource import bp_produk
from blueprint.cart.resource import bp_cart
from blueprint.transaksi.resource import bp_trans

app.register_blueprint(bp_customer)
app.register_blueprint(bp_auth)
app.register_blueprint(bp_pelapak)
app.register_blueprint(bp_produk)
app.register_blueprint(bp_cart)
app.register_blueprint(bp_trans)
# app.register_blueprint(bp_user, url_prefix='/user')
# app.register_blueprint(bp_rent, url_prefix='/rent')
# app.register_blueprint(bp_weather)
db.create_all()

@app.route('/')
def index():
    return "<h1> Hello : This main route </h1>"