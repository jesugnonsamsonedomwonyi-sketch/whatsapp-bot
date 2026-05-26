from flask import Flask
import os

app = Flask(__name__)
@app.route("/webhook", methods=["GET"])
def verify():
    VERIFY_TOKEN = "mybot123"

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge

    return "Verification failed"
@app.route("/")
def home():
    return "Bot running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
