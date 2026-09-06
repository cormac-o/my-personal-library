from flask import Blueprint, jsonify, make_response
from database import db
from sqlalchemy import text

users_bp = Blueprint('users', __name__)

@users_bp.route('/api/v1.0/users', methods=['GET'])
def get_users():
    result = db.session.execute(text("SELECT * FROM users;"))
    return make_response(result.fetchall(), 200)