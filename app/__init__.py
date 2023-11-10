import os
from dotenv import load_dotenv
from flask import Flask
from .models import Base
from .db import init_db

load_dotenv()


init_db(Base)

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from .routes import bp

app.register_blueprint(bp)
