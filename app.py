import os
from flask import Flask
from src.common.utils import ma, db, jwt, api
from src.routes.routes import Routes

app = Flask(__name__)

#app.config.from_object("settings.DeveloperConfig")


if os.environ["FLASK_ENV"] == "development":
    app.config.from_object("settings.DeveloperConfig")
elif os.environ["FLASK_ENV"] == "testing":
    app.config.from_object("settings.TestConfig")
else:
    app.config.from_object("settings.ProductionConfig")


#Se inicializa la api
api.init_app(app)

#Se inicializan las extensiones a utilizar
db.init_app(app)
ma.init_app(app)
jwt.init_app(app)

#Llamar a las rutas

Routes(api)