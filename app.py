from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import Config
from databases.database import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Importa los modelos antes de registrar los blueprints
from models.user import User
from models.patient import Patient
from models.medic import Medic
from models.admin import Admin
from models.file import File

# Importa y registra los blueprints
from controllers.auth_controller import auth_blueprint
from controllers.user_controller import user_blueprint
from controllers.patient_controller import patient_blueprint
from controllers.medic_controller import medic_blueprint
from controllers.admin_controller import admin_blueprint
from controllers.file_controller import file_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(patient_blueprint, url_prefix='/patients')
app.register_blueprint(medic_blueprint, url_prefix='/medics')
app.register_blueprint(admin_blueprint, url_prefix='/admins')

app.register_blueprint(file_blueprint, url_prefix='/files')


if __name__ == '__main__':
    app.run(debug=True)