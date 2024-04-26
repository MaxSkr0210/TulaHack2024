from flask import request,make_response, jsonify
from db.models import User
from db.service import find_user_by_login, create_user, login_user
from flask_jwt_extended import JWTManager, create_access_token

def register_routes(app, db):
  app.config['BASE_URL'] = 'http://127.0.0.1:5000'  #Running on localhost
  app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
  app.config['JWT_TOKEN_LOCATION'] = ['cookies']
  app.config['JWT_COOKIE_CSRF_PROTECT'] = True
  app.config['JWT_CSRF_CHECK_FORM'] = True

  jwt = JWTManager(app) 

  @app.get("/ping")
  def ping_pong():
    return {"pong": "pong"}

  @app.get("/")
  def test():
    return User.query.all(),200 
  
  @app.post("/reg")
  def register():
    json = request.json
    login = json.get('login')
    users = find_user_by_login(login)

    if len(users) != 0:
      return {"error": "asdasd"}
    
    password = json.get('password')
    create_user(login, password)

    token = create_access_token(identity=login)
    res = make_response()
    res.set_cookie("jwt", token)

    return res
  
  @app.post("/login")
  def login():
    json = request.json
    login = json.get('login')
    users = find_user_by_login(login)

    if len(users) == 0:
      return {"error": "фывфыв"}
    
    password = json.get('password')

    user = login_user(login, password)

    if user:
      token = create_access_token(identity=login)
      res = make_response()
      res.set_cookie("jwt", token)
      return res
    
    return {"error": "фывфыв"}


