from backend.config import Config
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)

    # Добавляем обработчик для загрузки пользователя
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    # Настраиваем страницы перенаправления при неудачной авторизации
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to access this page."

    from .auth import auth_bp
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app
