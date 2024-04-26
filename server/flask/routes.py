from flask import request,make_response
from db.models import User
from db.service import find_user_by_login, create_user

def register_routes(app, db):
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

    print(users)

    if len(users) != 0:
      return {"error": "asdasd"}
    
    password = json.get('password')

    create_user(login, password)

    return {"msg": "user created"}

