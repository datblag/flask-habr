from flask import Flask
from habr_microblog_config import Config
app = Flask(__name__)
app.config.from_object(Config)

from habr_microblog import routes


