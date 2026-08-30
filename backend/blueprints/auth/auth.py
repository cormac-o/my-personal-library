from flask import Blueprint, jsonify, make_response

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/v1.0/login', methods=['GET'])
def login():
    return make_response(jsonify({'message': 'Login route'}), 200)

@auth_bp.route('/api/v1.0/logout', methods=['GET'])
def logout():
    return make_response(jsonify({'message': 'Logout route'}), 200)