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
from controllers.file_controller import file_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(file_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)