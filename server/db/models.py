from main import db

class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  login = db.Column(db.VARCHAR(255), nullable=False, unique=True)
  password = db.Column(db.VARCHAR(255), nullable=False)
