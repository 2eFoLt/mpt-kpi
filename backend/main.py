from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Api
from os import environ

from config import Config
from backend.extensions import db, migrate, login_manager, mail
from resources.basic_resource import BasicResource
from resources.pdf_resource import PDFResource

app = Flask(__name__)
app.config.from_object(Config)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB limit for uploads

api = Api(app)
api.add_resource(BasicResource, '/api', '/api/<int:source_id>')
api.add_resource(PDFResource, '/docs', '/docs/<string:filename>')

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)
mail.init_app(app)

# Set up login behavior
@login_manager.user_loader
def load_user(user_id):
    from backend.app.models import User
    return User.query.get(int(user_id))

login_manager.login_view = "auth.login"
login_manager.login_message = "Please log in to access this page."

# Register blueprints
from backend.app.auth import auth_bp
from backend.app.routes import bp as main_bp

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

PORT = environ.get('BACKEND_PORT', 8000)
DEBUG = environ.get('DEBUG', True)
app.run(extra_files=[], debug=DEBUG, host='0.0.0.0', port=PORT)
