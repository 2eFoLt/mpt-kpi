# Config
from os import environ
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from flask_login import UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from itsdangerous import URLSafeTimedSerializer

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

@app.route('/api/', methods=['GET', 'POST', 'PATCH'])
def api():
    return {'status': 'OK'}

class Users(UserMixin):
    def __init__(self, User_ID, User_name, User_surname, User_patronymic, Role_ID, User_phone, User_email,
                 User_passhash, is_admin):
        self.id = User_ID
        self.name = User_name
        self.surname = User_surname
        self.patronymic = User_patronymic
        self.position_id = Role_ID
        self.phone = User_phone
        self.email = User_email
        self.password_hash = User_passhash
        self.is_admin = is_admin
    def __repr__(self):
        return f'<User {self.email}>'

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

def generate_reset_token(user_id):
    serializer = URLSafeTimedSerializer(app.secret_key)
    return serializer.dumps(user_id, salt='password-reset')

def verify_reset_token(token, expiration=3600): # 1 час
    serializer = URLSafeTimedSerializer(app.secret_key)
    try:
        user_id = serializer.loads(token, salt='password-reset', max_age=expiration)
        return user_id
    except Exception:
        return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = _get_db_cursor()
        if cursor:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            cursor.close()
            if user and Users(*user).check_password(password):
                login_user(Users(*user))
                return redirect(url_for('protected'))
            else:
                return "Неверный email или пароль"
        else:
            return "Ошибка подключения к базе данных"
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/create_user', methods=['POST'])
@login_required
def create_user():
    if not current_user.is_admin:
        return jsonify({'message': 'Доступ запрещен'}), 403

    data = request.get_json()
    try:
        cursor = _get_db_cursor()
        if cursor:
            cursor.execute("INSERT INTO users (name, surname, patronymic, position_id, phone, email, "
                           "is_admin) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (data['name'], data['surname'], data['patronymic'], data['position_id'],
                            data['phone'], data['email'], False))
            user_id = cursor.lastrowid
            cursor.connection.commit()
            cursor.close()
            token = generate_reset_token(user_id)
            reset_url = url_for('reset_password', token=token, _external=True)
            return jsonify({'reset_url': reset_url}), 201
        else:
            return jsonify({'message': 'Ошибка подключения к базе данных'}), 500
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user_id = verify_reset_token(token)
    if user_id is None:
        return "Недействительная или просроченная ссылка"

    if request.method == 'POST':
        new_password = request.form['password']
        hashed_password = generate_password_hash(new_password)
        cursor = _get_db_cursor()
        if cursor:
            cursor.execute("UPDATE users SET password_hash = %s WHERE id = %s",
                           (hashed_password, user_id))
            cursor.connection.commit()
            cursor.close()
            return "Пароль успешно изменен"
        else:
            return "Ошибка подключения к базе данных"

    return render_template('reset_password.html')

app.run(extra_files=[], debug=DEBUG, host='0.0.0.0', port=PORT)
