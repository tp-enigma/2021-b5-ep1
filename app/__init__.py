import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def main_route():
    return jsonify({
        "message": "Hello World !"
    }), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))