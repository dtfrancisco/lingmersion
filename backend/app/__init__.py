from flask import Flask
from config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

CORS(app, resources={r'/*': {'origins': '*'}})

from app import routes