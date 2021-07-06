from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def root():
    return "Hi, this is the root address"


@app.route("/bot", methods=["POST"])
def botWebHook():
    msg = request.values.get("Body", "")
    return "bot"


if __name__ == "__main__":
    app.run(host="localhost", port="5000", debug=True)
