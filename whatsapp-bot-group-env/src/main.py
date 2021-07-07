from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def root():
    return "Hi, this is the root address"


@app.route("/bot", methods=["POST"])
def botWebHook():
    msg = request.values.get("Body", "").lower()
    # check msg contains all keywords when setting up meeting
    keywords = ["tuesday", "sighthill", "power", "league"]
    lst = [...]
    if all((word in lst for word in keywords)):
        resp = MessagingResponse()
        body_resp = resp.message(
            body="in"
        )  # automatic response in case strings were found
        return "message received and a response has been sent"

    print("message received but a match could not be found")  # debug on console
    return "message received but a match could not be found"  # debug on browser


if __name__ == "__main__":
    app.run(host="localhost", port="5000", debug=True)
