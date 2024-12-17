import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-padrao'
    CSV_PATH = os.environ.get('CSV_PATH') or 'data/hospitais.csv'
    DEBUG = os.environ.get('FLASK_DEBUG') or False