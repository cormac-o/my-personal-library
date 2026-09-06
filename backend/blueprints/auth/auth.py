from flask import Blueprint, jsonify, make_response

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/v1.0/login', methods=['GET'])
def login():
    auth = auth.request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response(jsonify({'message': 'Missing credentials'}), 401)

    return make_response(jsonify({'message': 'Login route'}), 200)

@auth_bp.route('/api/v1.0/logout', methods=['GET'])
def logout():
    return make_response(jsonify({'message': 'Logout route'}), 200)