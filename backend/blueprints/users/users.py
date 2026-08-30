from flask import Blueprint, jsonify, make_response

users_bp = Blueprint('users', __name__)

@users_bp.route('/api/v1.0/users', methods=['GET'])
def get_users():
    return make_response(jsonify({'message': 'User route'}), 200)