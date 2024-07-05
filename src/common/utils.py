from  flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_restx import Api

#Se inicializa la Api con el prefix
api = Api(prefix="/api/store1.0")

#Se inicializan las extensiones
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
