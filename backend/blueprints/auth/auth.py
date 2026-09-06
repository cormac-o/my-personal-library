from flask import Blueprint, jsonify, make_response, request
from database import db
from sqlalchemy import text
import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/v1.0/login', methods=['GET'])
def login():
    auth = request.authorization

    #Verify that user has provided credentials
    if not auth or not auth.username or not auth.password:
        return make_response(jsonify({'message': 'Missing credentials'}), 401)

    #Find user in database
    if auth.username:
        user = db.session.execute(text("SELECT * FROM users WHERE username = :username;"), {'username': auth.username}).fetchone()

    if not user:
        return make_response(jsonify({'message': 'User not found'}), 401)

    #Check if password is correct.
    elif bcrypt.checkpw(auth.password.encode('utf-8'), user.passhash.encode('utf-8')):
        return make_response(jsonify({'message': 'Login successful'}), 200)

    else:
        return make_response(jsonify({'message': 'Wrong password'}), 401)

@auth_bp.route('/api/v1.0/logout', methods=['GET'])
def logout():
    return make_response(jsonify({'message': 'Logout route'}), 200)

@auth_bp.route('/api/v1.0/register', methods=['POST'])
def register():
    #Snippet to generate passhash:
    #passhash = bcrypt.hashpw((<plaintext password>.encode("utf-8")), bcrypt.gensalt()).decode("utf-8")
    return make_response(jsonify({'message': 'Register route'}), 200)