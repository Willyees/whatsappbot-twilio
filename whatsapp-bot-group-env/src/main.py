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
    print("received: " + msg)
    keywords = ["tuesday"]  # ["tuesday", "sighthill", "power", "league"]
    resp = MessagingResponse()
    resp_msg = resp.message()
    if all((word in msg for word in keywords)):
        resp_msg.body("in")
        return str(resp)

    print("message received but a match could not be found")  # debug on console
    resp_msg.body("could not find match")
    return str(resp)  # return xml format string, will be redirected


if __name__ == "__main__":
    app.run(host="localhost", port="5000", debug=True)
