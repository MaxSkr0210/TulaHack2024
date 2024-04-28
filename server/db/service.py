import hashlib
from db.models import User, Characteristic, Score, Test, Question, Answer, Lesson
from main import db

def serialize(model):
    if isinstance(model, list):
        return [serialize(item) for item in model]
    elif hasattr(model, '__table__'):
        return {c.name: getattr(model, c.name) for c in model.__table__.columns}
    else:
        raise TypeError("Этот объект не является экземпляром модели SQLAlchemy")

def hash_pass(password):
  password_encoded = password.encode('utf-8')
  hash_object = hashlib.md5(password_encoded)
  hash = hash_object.hexdigest()
  return hash

def getCharacteristicsById(id):
  return Characteristic.query.filter(Characteristic.id == id).first()

def find_characteristic():
  return Characteristic.query.all()

def getCharacteristics():
  characteristics = Characteristic.query.all()
  return characteristics

def get_score_by_user_id(user_id, characteristic_id):
  return Score.query.filter_by(user_id=user_id, characteristic_id=characteristic_id).first()

def get_score_by_user_login(login, characteristic_id):
  user = find_user_by_login(login)[0]
  return Score.query.filter_by(user_id=user.id, characteristic_id=characteristic_id).first()

def creteScore(login):
  users = find_user_by_login(login)
  user = users[0]
  characteristics = getCharacteristics()
  for characteristic in characteristics:
    score = Score(score_amount=0, user=user, characteristic=characteristic)
    db.session.add(score)
    db.session.commit()

def find_user_by_id(id):
  return User.query.filter(User.id == id).all()


def find_user_by_login(login):
  return User.query.filter(User.login == login).all()

def create_user(login, password, first_name, last_name, avatar_path):
  hash = hash_pass(password)

  user = User(login=login, password=hash, avatar_path=avatar_path, first_name=first_name, last_name=last_name, coins=-1, role="user")

  db.session.add(user)
  db.session.commit()

  creteScore(login)

def login_user(login, password):
  users = find_user_by_login(login)
  if users:
    user = users[0]
    pas = user.password
    hash = hash_pass(password)

    if (hash == pas):
      return user
    
  return None
    
def find_test_by_tilte(title):
  return Test.query.filter(Test.title == title).first()

def create_answer(content, points, characteristic_id, question):
  characteristic = getCharacteristicsById(characteristic_id)
  new_answer = Answer(content=content, points=points, characteristic_a=characteristic, question=question)

  db.session.add(new_answer)
  db.session.commit()

def craete_question(content, answers, test):
  new_question = Question(content=content, test=test)

  db.session.add(new_question)
  db.session.commit()

  for answer in answers:
    create_answer(answer.get('content'), answer.get('points'), answer.get('characteristic_id'), new_question)

def create_test(title, description, questions):
  test = find_test_by_tilte(title)
  if test:
    return {"error": "asdasd"}
  
  new_test = Test(title=title, description=description)
  db.session.add(new_test)
  db.session.commit()

  for question in questions:
    craete_question(question.get('content'), question.get('answers'), new_test)  

def get_tests():
  tests = Test.query.all()
  return tests

def get_lesson_by_id(id):
  return Lesson.query.filter_by(id=id).first()

def create_lesson(title, description, content, sod, min_point, img_path):
  c = getCharacteristicsById(sod)
  new_lesson = Lesson(title=title, description=description, content=content, characteristic_l=c, min_point=min_point, img_path=img_path)
  db.session.add(new_lesson)
  db.session.commit()

def get_lessons():
  return Lesson.query.all()

def get_recomendation_lessons(characteristic_id, point):
  return Lesson.query.filter(Lesson.characteristic_id == characteristic_id, Lesson.min_point >= point).all()