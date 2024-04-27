import os
from werkzeug.utils import secure_filename
from flask import request,make_response, jsonify, send_from_directory
from db.models import User
from db.service import find_user_by_login, create_user, login_user, getCharacteristicsById, create_test, get_tests
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def register_routes(app, db):
  jwt = JWTManager(app)

  app.config['BASE_URL'] = 'http://localhost:5000'  #Running on localhost
  app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!


  @app.route('/img/<path:filename>')
  def get_image(filename):
    print(filename)
    return send_from_directory('static', 'img/' + filename)

  @app.get("/ping")
  def ping_pong():
    return {"pong": "pong"}

  @app.get("/")
  def test():
    return User.query.all(),200 
  
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
    avatar_path = filename

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
        "login": user.login, 
        "first_name": user.first_name, 
        "last_name":user.last_name, 
        "avatar_path": user.avatar_path, 
        "scores": scores
      }

      token = create_access_token(identity=obj)

      return jsonify({"access_token": token})
    
    return {"error": "фывфыв"}


  @app.get("/protected")
  @jwt_required()
  def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

  @app.get("/test")
  def get_test():
    test =  get_tests()
    return jsonify(test), 200
    

  @app.post("/test")
  def add_test():
    new_test = request.json
    title = new_test.get('title')
    description = new_test.get('description')
    questions = new_test.get('questions')

    create_test(title, description, questions)

    return jsonify({"test": "asd"}), 200
