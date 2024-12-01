# Config
from os import environ
from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Api
from resources.basic_resource import BasicResource
from resources.pdf_resource import PDFResource
import mysql.connector

PORT = environ.get('BACKEND_PORT', 8000)
DEBUG = environ.get('DEBUG', True)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

api.add_resource(BasicResource, '/api', '/api/<int:source_id>')
api.add_resource(PDFResource, '/docs')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

def _get_db_cursor():
    connection = mysql.connector.connect(
        host='db',
        port=environ.get('DATABASE_PORT', 3306),
        user=environ.get('DATABASE_USER', 'mpt-kpi'),
        database=environ.get('DATABASE_NAME', 'mpt-kpi'),
        password=environ.get('DATABASE_PASSWORD', 'mpt-kpi'),
    )
    return connection.cursor()

app.run(extra_files=[], debug=DEBUG, host='0.0.0.0', port=PORT)
