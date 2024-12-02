# Config
from os import environ
from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Api
from resources.basic_resource import BasicResource
from resources.pdf_resource import PDFResource
import mysql.connector

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

# PORT = environ.get('BACKEND_PORT', 8000)
# DEBUG = environ.get('DEBUG', True)
#
# app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # 5Мб кап по размеру файла, фласк автоматом вернёт 413, если больше
# api = Api(app)
#
# api.add_resource(BasicResource, '/api', '/api/<int:source_id>')
# api.add_resource(PDFResource, '/docs', '/docs/<string:filename>')
#
# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')
#
# def _get_db_cursor():
#     connection = mysql.connector.connect(
#         host='db',
#         port=environ.get('DATABASE_PORT', 3306),
#         user=environ.get('DATABASE_USER', 'mpt-kpi'),
#         database=environ.get('DATABASE_NAME', 'mpt-kpi'),
#         password=environ.get('DATABASE_PASSWORD', 'mpt-kpi'),
#     )
#     return connection.cursor()
#
# app.run(extra_files=[], debug=DEBUG, host='0.0.0.0', port=PORT)
