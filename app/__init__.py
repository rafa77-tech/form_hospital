from flask import Flask
from config import Config
from .utils import load_hospitals_data

app = Flask(__name__)
app.config.from_object(Config)

hospitals_data = load_hospitals_data()

from .routes import *
