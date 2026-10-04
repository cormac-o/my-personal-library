from flask import current_app, request, jsonify, make_response
import jwt
from functools import wraps

def token_required(func):
    @wraps(func)
    def token_required_wrapper(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({'message': 'Token is missing.'}), 401)

        try:
            data = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=["HS256"]
            )
            user_id = data['user_id']
        except jwt.ExpiredSignatureError:
            return make_response(jsonify({'message': 'Token has expired.'}), 401)
        except jwt.InvalidTokenError:
            return make_response(jsonify({'message': 'Invalid token.'}), 401)

        return func(user_id=user_id, *args, **kwargs)
    return token_required_wrapper