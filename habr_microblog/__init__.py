from flask import Flask

app = Flask(__name__)

from habr_microblog import routes