# Config
from os import environ
from flask import Flask
from flask_cors import CORS
import mysql.connector

PORT = environ.get('BACKEND_PORT', 8000)
DEBUG = environ.get('DEBUG', True)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def _get_db_cursor():
    connection = mysql.connector.connect(
        host='db',
        port=environ.get('DATABASE_PORT', 3306),
        user=environ.get('DATABASE_USER', 'mpt-kpi'),
        database=environ.get('DATABASE_NAME', 'mpt-kpi'),
        password=environ.get('DATABASE_PASSWORD', 'mpt-kpi'),
    )

    return connection.cursor()

@app.route('/db/')
def test_database_connection():
    cursor = _get_db_cursor()
    cursor.execute('SHOW TABLES')

    return f'Тестируем подключение к базе данных.\n\n{cursor.fetchall()}'

@app.route('/')
def main():
    return 'Здесь когда-то будет backend.'

print(f'Widgets: port: {PORT}, debug: {DEBUG}')

app.run(extra_files=[], debug=DEBUG, host='0.0.0.0', port=PORT)
