import hashlib
from db.models import User
from main import db

def find_user_by_login(login):
  return User.query.filter(User.login == login).all()

def create_user(login, password):
  hash = hashlib.md5(password).hexdigest()
  user = User(login=login, password=hash)

  db.session.add(user)
  db.session.commit()