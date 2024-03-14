from flask import Flask
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return "index.html"
@app.route("/ams_page")
def ams_page():
    return subprocess.run['python','AMS_Run.py']