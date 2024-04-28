import os
from werkzeug.utils import secure_filename
from flask import request,make_response, jsonify, send_from_directory
from db.models import User
from db.service import find_user_by_login, create_user, login_user, getCharacteristicsById, create_test, get_tests, serialize, create_lesson, get_lessons, find_user_by_id, get_score_by_user_id, get_lesson_by_id, get_recomendation_lessons,find_characteristic, get_score_by_user_login
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

def allowed_file(filename):
    print(filename)
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def register_routes(app, db):
  jwt = JWTManager(app)

  app.config['BASE_URL'] = 'http://localhost:5000'  #Running on localhost
  app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!


  @app.route('/img/<path:filename>')
  def get_image(filename):
    return send_from_directory('static', 'img/' + filename)

  @app.get("/ping")
  def ping_pong():
    return {"pong": "pong"}

  @app.get("/")
  def test():
    return User.query.all(),200 
  
  @app.get("/refresh_token")
  @jwt_required(refresh=True)
  def refresh_token():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)
          
  
  @app.post("/reg")
  def register():
    json = request.form
    login = json.get('login')
    users = find_user_by_login(login)

    if 'avatar_path' not in request.files:
      print('No file part')

    file = request.files['avatar_path']

    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file_path = os.path.join(app.static_folder, 'img', filename)
      file.save(file_path)

    if len(users) != 0:
      return {"error": "asdasd"}
    
    password = json.get('password')
    first_name = json.get('first_name')
    last_name = json.get('last_name')
    avatar_path = file.filename

    create_user(login, password, first_name, last_name, avatar_path)

    res = make_response()

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
      scors = user.scors

      scores = []

      for score in scors:
        ch = getCharacteristicsById(score.characteristic_id)
        scores.append({
          "id": score.id,
          "score_amount": score.score_amount,
          "characteristic": {
            "id": ch.id,
            "name": ch.name
          }
        })

      obj = {
        "id": user.id,
        "login": user.login, 
        "first_name": user.first_name, 
        "last_name":user.last_name, 
        "avatar_path": user.avatar_path, 
        "scores": scores,
        "role": user.role
      }

      access_token = create_access_token(identity=obj)
      refersh_token = create_refresh_token(user.id)

      res = make_response()
      res.set_cookie("jwt", refersh_token, domain="localhost")

      return jsonify({"access_token": access_token, "refresh_token": refersh_token})
    
    return {"error": "фывфыв"}


  @app.get("/protected")
  @jwt_required()
  def protected():
    current_user = get_jwt_identity()
    user = find_user_by_id(current_user)[0]
    scors = user.scors

    scores = []

    for score in scors:
      ch = getCharacteristicsById(score.characteristic_id)
      scores.append({
        "id": score.id,
        "score_amount": score.score_amount,
        "characteristic": {
          "id": ch.id,
          "name": ch.name
        }
      })
    obj = {
      "id": user.id,
      "login": user.login, 
      "first_name": user.first_name, 
      "last_name":user.last_name, 
      "avatar_path": user.avatar_path, 
      "scores": scores,
      "role": user.role
    }

    return jsonify(logged_in_as=obj), 200

  @app.get("/characteristic")
  def get_characteristic():

    ch = find_characteristic()

    chs = []

    for c in ch:
      obj = {
        "id": c.id,
        "name": c.name
      }
      chs.append(obj)

    return jsonify(chs)

  @app.get("/test")
  def get_test():
    test = get_tests()

    tests = serialize(test)

    return jsonify(tests), 200

  @app.post("/test")
  def add_test():
    new_test = request.json
    title = new_test.get('title')
    description = new_test.get('description')
    questions = new_test.get('questions')

    create_test(title, description, questions)

    return jsonify({"test": "asd"}), 200
  
  @app.put("/score/vr/<login>")
  def upgrade_score_vr(login):
    json = request.json
    results = json.get('results')
    for characteristic in results:
      score = get_score_by_user_login(login, characteristic.get('characteristics_id'))
      score.score_amount += characteristic['score']

    db.session.commit()

    return jsonify({"test": ""})

  @app.put("/score/<int:user_id>")
  def upgrade_score(user_id):
    json = request.json
    results = json.get('results')
    for characteristic in results:
      score = get_score_by_user_id(user_id, characteristic.get('characteristics_id'))
      score.score_amount += characteristic['score'] + 1

    db.session.commit()

    return jsonify({"test": ""})


  @app.get("/lesson")
  def find_lessons():
    les = get_lessons()

    print(les)

    lessons = []

    for lesson in les:
      obj = {
        "id": lesson.id,
        "title": lesson.title,
        "description": lesson.description,
        "content": lesson.content,
        "sod": lesson.characteristic_id,
        "min_point": lesson.min_point,
        "img_path": lesson.img_path
      }

      lessons.append(obj)

    return jsonify(lessons), 200

  @app.get("/lesson/<int:id>")
  def get_lesson(id):
    lesson = get_lesson_by_id(id)

    obj = {
      "id": lesson.id,
      "title": lesson.title,
      "description": lesson.description,
      "content": lesson.content,
      "sod": lesson.characteristic_id,
      "min_point": lesson.min_point,
      "img_path": lesson.img_path
    }
    return jsonify(obj)

  @app.post("/lesson")
  def add_lesson():
    new_test = request.form
    title = new_test.get('title')
    description = new_test.get('description')
    content = new_test.get('content')
    sod = int(new_test.get('sod')) 
    min_point = int(new_test.get('min_point'))

    if 'img_path' not in request.files:
      print('No file part')
      return jsonify(error="as"), 200

    file = request.files['img_path']

    print(file)

    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file_path = os.path.join(app.static_folder, 'img', filename)
      file.save(file_path)

    img_path = file.filename

    create_lesson(title, description, content, sod, min_point, img_path)

    return jsonify(new_test="asd"), 200

  @app.get("/lesson/recomenfation")
  def get_recomendation():
    characteristic_id = request.args.get('characteristic_id')
    point = request.args.get('point')
    les = get_recomendation_lessons(characteristic_id, point)

    lessons = []

    for lesson in les:

      obj = {
      "id": lesson.id,
      "title": lesson.title,
      "description": lesson.description,
      "content": lesson.content,
      "sod": lesson.characteristic_id,
      "min_point": lesson.min_point,
      "img_path": lesson.img_path,  
      }

      lessons.append(obj)

    return jsonify(lessons), 200