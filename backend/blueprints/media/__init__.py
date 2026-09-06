# This file is used to initialise the media items.
# This is the file registered for media items with endpoints imported.
# Endpoints will be implemented in their respective files (books.py, movies.py, etc.)

from flask import Blueprint

media_bp = Blueprint('media', __name__)

from .books import *
from .movies import *
from .common import *