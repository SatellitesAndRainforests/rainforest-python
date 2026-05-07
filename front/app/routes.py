from flask import jsonify, render_template

from app import app

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": "rainforest-python-front"
    })
