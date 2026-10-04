from flask import jsonify, make_response, request
from . import media_bp
from sqlalchemy import text
from database import db
import uuid

from .books import create_book, get_book_by_media_id

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

@media_bp.route('/api/v1.0/media', methods=['GET'])
def get_all_media():

    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    offset = (page - 1) * limit

    result = db.session.execute(text("SELECT * FROM media " \
    "ORDER BY title " \
    "LIMIT :limit OFFSET :offset ;"),
    {'limit': limit, 'offset': offset}).mappings().all()
    
    media_items = [dict(row) for row in result]

    return make_response(jsonify(media_items), 200)

@media_bp.route('/api/v1.0/media/<media_id>', methods=['GET'])
def get_media_by_id(media_id):

    result = db.session.execute(text("SELECT * FROM media WHERE media_id = :media_id;"),
    {'media_id': media_id}).mappings().first()

    if not result:
        return make_response(jsonify({'message': 'Media item not found'}), 404)

    media_item = dict(result)

    match media_item['type']:
        case 'book':
            return get_book_by_media_id(media_id)
        case 'movie':
            # Implement movie creation logic here
            return make_response(jsonify({'message': 'Movie creation not implemented yet'}), 501)
        case _:
            return make_response(jsonify({'message': 'Unsupported media type'}), 400)

    return make_response(jsonify(media_item), 200)