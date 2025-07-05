from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/ping")
def ping():
    return jsonify(status="ok", service="2")


@app.route("/hello")
def hello():
    return jsonify(message="Hello from Service 2")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8002)
