import os
from flask import Flask
from os import urandom

main_folder = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, instance_path=main_folder)
app.secret_key = urandom(24)

from . import routes
