from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import (JWTManager, jwt_required, 
                                jwt_refresh_token_required, 
                                jwt_optional, fresh_jwt_required, 
                                get_raw_jwt, get_jwt_identity,
                                create_access_token, create_refresh_token, 
                                set_access_cookies, set_refresh_cookies, 
                                unset_jwt_cookies,unset_access_cookies)


db = SQLAlchemy()
jwt = None

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:test@localhost:3306/skillsUp"
  app.config['BASE_URL'] = 'http://127.0.0.1:5000'  #Running on localhost
  app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
  app.config['JWT_TOKEN_LOCATION'] = ['cookies']
  app.config['JWT_COOKIE_CSRF_PROTECT'] = True
  app.config['JWT_CSRF_CHECK_FORM'] = True
  jwt = JWTManager(app) 

  db.init_app(app)
  
  from flask.routes import register_routes
  register_routes(app, db)

  migrate = Migrate(app, db)

  return app