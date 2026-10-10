from flask import Flask, make_response
from flask_cors import CORS
from database import db
from dotenv import load_dotenv
import os

# Import Blueprints
from blueprints.users.users import users_bp
from blueprints.auth.auth import auth_bp
from blueprints.media.__init__ import media_bp


app = Flask(__name__)
CORS(app)

# Load secret key from environment variable
app.config['SECRET_KEY'] = os.getenv('secret_key')

# Register Blueprints
app.register_blueprint(users_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(media_bp)

load_dotenv()  # Load environment variables from .env file
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('db_user')}:{os.getenv('db_password')}"
    f"@{os.getenv('db_host')}:{os.getenv('db_port')}/{os.getenv('db_name')}"
)

db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    return make_response("<h1>Welcome to My Personal Media Library!</h1>", 200)

if __name__ == '__main__':
    app.run(debug=True) #Port can be specified here if needed, e.g., app.run(debug=True, port=5000)