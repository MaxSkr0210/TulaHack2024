import hashlib
from db.models import User
from main import db

def hash_pass(password):
  password_encoded = password.encode('utf-8')
  hash_object = hashlib.md5(password_encoded)
  hash = hash_object.hexdigest()
  return hash

def find_user_by_login(login):
  return User.query.filter(User.login == login).all()

def create_user(login, password):
  hash = hash_pass(password)

  user = User(login=login, password=hash)

  db.session.add(user)
  db.session.commit()

def login_user(login, password):
  users = find_user_by_login(login)
  if users:
    user = users[0]
    pas = user.password
    hash = hash_pass(password)

    if (hash == pas):
      return user
    
  return None
    