from flask import jsonify, make_response
from sqlalchemy import text
from database import db
import uuid

def create_book(media_id, data):
    author = data.get('author')

    if not author:
        return make_response(jsonify({'message': 'Missing required fields'}), 400)

    book_id = str(uuid.uuid4())

    row = db.session.execute(text(
        "INSERT INTO books(book_id, media_id, author)"
        "VALUES (:book_id, :media_id, :author)"
        "RETURNING book_id;"),
        {'book_id': book_id, 'media_id': media_id, 'author': author}
    ).fetchone()

    db.session.commit()

    book_id = row[0]

    return make_response(jsonify({'message': 'Book created successfully', 'book_id': book_id}), 201)