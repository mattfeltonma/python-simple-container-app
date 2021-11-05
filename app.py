# Import standard libraries
import os

# Import other libraries
from flask import Flask, render_template, session, request, redirect, url_for

# Setup up a Flask instance
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

