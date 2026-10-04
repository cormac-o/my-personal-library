from flask import Blueprint, jsonify, make_response, request
from database import db
from sqlalchemy import text
import bcrypt
import re
import uuid

auth_bp = Blueprint('auth', __name__)

USERNAME_REGEX = r'^[a-zA-Z0-9_]{3,}$'  # Minimum three characters, alphanumeric and underscores only
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' 
PASSWORD_REGEX = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'  # Minimum eight characters, at least one letter and one number


@auth_bp.route('/api/v1.0/login', methods=['POST'])
def login():
    auth = request.get_json()  # Expecting JSON payload with "username" and "password"

    #Verify that user has provided credentials
    if not auth or not auth.get("username") or not auth.get("password"):
        return make_response(jsonify({'message': 'Missing credentials'}), 401)

    username = auth.get("username")
    password = auth.get("password")

    #Find user in database
    if username:
        user = db.session.execute(text("SELECT * FROM users WHERE username = :username;"), {'username': username}).fetchone()

    if not user:
        return make_response(jsonify({'message': 'User not found'}), 401)

    #Check if password is correct.
    if bcrypt.checkpw(password.encode('utf-8'), user.passhash.encode('utf-8')):
        return make_response(jsonify({'message': 'Login successful'}), 200)
    else:
        return make_response(jsonify({'message': 'Wrong password'}), 401)

@auth_bp.route('/api/v1.0/logout', methods=['POST'])
def logout():
    return make_response(jsonify({'message': 'Logout route'}), 200)

@auth_bp.route('/api/v1.0/register', methods=['POST'])
def register():
    #Snippet to generate passhash:
    #passhash = bcrypt.hashpw((<plaintext password>.encode("utf-8")), bcrypt.gensalt()).decode("utf-8")
    
    if ( request.form and 
        'username' in request.form and
        'email' in request.form and
        'password' in request.form):

        #data:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not re.match(EMAIL_REGEX, email):
            return make_response(jsonify({'message': 'Invalid email format'}), 400)

        if not re.match(PASSWORD_REGEX, password):
            return make_response(jsonify({'message': 'Invalid password format'}), 400)

        if not re.match(USERNAME_REGEX, username):
            return make_response(jsonify({'message': 'Invalid username format'}), 400)

        user_id = str(uuid.uuid4())  # Generate a unique user ID
        passhash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


        result = db.session.execute(text("INSERT INTO users (user_id,username, email, passhash)" \
        "VALUES (:user_id, :username, :email, :passhash) RETURNING user_id;"), 
        { 'user_id': user_id, 'username': username, 'email': email, 'passhash': passhash })

        db.session.commit()

        return make_response(jsonify({'message': 'User registered successfully'}), 201)