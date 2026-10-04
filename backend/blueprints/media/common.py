from flask import jsonify, make_response, request
from . import media_bp
from sqlalchemy import text
from database import db
import uuid

from .books import create_book

@media_bp.route('/api/v1.0/media', methods=['POST'])
def create_media():

    data = request.get_json()

    #Data contains more than these fields, but the rest are used in their respective media type tables.
    media_type = data.get('media_type')
    year = data.get('year')
    title = data.get('title')   

    if not media_type or not year or not title:
        return make_response(jsonify({'message': 'Missing required fields'}), 400)

    media_id = str(uuid.uuid4())

    row = db.session.execute(text(
        "INSERT INTO media (media_id, type, year, title) " \
        "VALUES (:media_id, :type, :year, :title) " \
        "RETURNING media_id;"),
        {'media_id': media_id, 'type': media_type, 'year': year, 'title': title}
    ).fetchone()

    db.session.commit()

    media_id = row[0]

    match media_type:
        case 'book':
            return create_book(media_id, data)
        case 'movie':
            # Implement movie creation logic here
            return make_response(jsonify({'message': 'Movie creation not implemented yet'}), 501)
        case _:
            return make_response(jsonify({'message': 'Unsupported media type'}), 400)

