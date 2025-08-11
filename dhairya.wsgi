# wsgi.py
from flask import Flask
import reper

app = Flask(__name__)

@app.route('/')
def index():
    return "TelReper is loaded. Use CLI commands to operate."

if __name__ == "__main__":
    app.run()
