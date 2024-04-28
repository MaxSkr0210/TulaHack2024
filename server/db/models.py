from main import db

class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  login = db.Column(db.VARCHAR(255), nullable=False, unique=True)
  password = db.Column(db.VARCHAR(255), nullable=False)
  coins = db.Column(db.Integer, nullable=False) 
  first_name = db.Column(db.VARCHAR(50), nullable=False) 
  last_name = db.Column(db.VARCHAR(50), nullable=False) 
  role = db.Column(db.VARCHAR(5), nullable=False) 
  avatar_path = db.Column(db.TEXT, nullable=False) 
  scors = db.relationship('Score', backref='user', lazy=True)

class Characteristic(db.Model):
  __tablename__ = 'characteristic'
   
  id = db.Column(db.Integer, primary_key=True)  
  name = db.Column(db.VARCHAR(255), nullable=False, unique=True)
  scors = db.relationship('Score', backref='characteristic', lazy=True)
  answers = db.relationship('Answer', backref='characteristic_a', lazy=True)
  Lessons = db.relationship('Lesson', backref='characteristic_l', lazy=True)
class Score(db.Model):
  __tablename__ = 'score'
    
  id = db.Column(db.Integer, primary_key=True)  
  score_amount = db.Column(db.Integer, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  characteristic_id = db.Column(db.Integer, db.ForeignKey('characteristic.id'), nullable=False)

class Test(db.Model):
  __tablename__ = 'test'

  id = db.Column(db.Integer, primary_key=True)  
  title = db.Column(db.VARCHAR(255), nullable=False)
  description = db.Column(db.Text, nullable=False)  
  questions = db.relationship('Question', backref='test', lazy=True)

class Question(db.Model):
  __tablename__ = 'question'

  id = db.Column(db.Integer, primary_key=True)  
  content = db.Column(db.Text, nullable=False)
  answers = db.relationship('Answer', backref='question', lazy=True)
  test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)  

class Answer(db.Model):
  __tablename__ = 'answer'

  id = db.Column(db.Integer, primary_key=True)  
  content = db.Column(db.Text, nullable=False)
  points = db.Column(db.Integer, nullable=False)
  question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)  
  characteristic_id = db.Column(db.Integer, db.ForeignKey('characteristic.id'), nullable=False)  

class Lesson(db.Model):
  __tablename__ = 'lesson'

  id = db.Column(db.Integer, primary_key=True)  
  title = db.Column(db.VARCHAR(60), nullable=False)
  description = db.Column(db.VARCHAR(60), nullable=False)
  content = db.Column(db.Text, nullable=False)
  img_path = db.Column(db.TEXT, nullable=False) 
  min_point = db.Column(db.Integer, nullable=False)
  characteristic_id = db.Column(db.Integer, db.ForeignKey('characteristic.id'), nullable=False)  