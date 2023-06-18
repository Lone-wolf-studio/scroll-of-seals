from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import Settings 
from models import db
import os 
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '\x16\x12Tzo\x1a\r\xc9\xe1\x8bOY2\xfc\x8a\xc5\xda\x97}\xf6\xd6F\x11\x1b') 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'postgresql://postgres:optimus@lcoalhost:5432/flask_jwt_token') 

db.init_app(app)

# token required decorator 
def token_required(f):
	@wraps(f):
	def docorated(*args, **kwargs):
		token = None 

		if 'x-access-token' in request.headers:
			token = request.header['x-access-token']

		if not token:
			return jsonify({"message" : "Token not found in request payload"})

		try:
			request_data = jwt.decode(token, app.config['SECRET_KEY'])		
			logged_in_user = User.query.filter_by(id=data['id']).first()
		except:
			return jsonify({"message" : "Invalid Token"})

		return f(logged_in_user, *args, **kwargs)		


@app.route('/normal-login', methods=['GET'])
def normal_login():
	return jsonify({'message' : 'This is a normal login'})

@app.route('/jwt-login', methods=['GET'])
@token_required
def jwt_login():
	return jsonify({'message' : "This wont work without token"})	
