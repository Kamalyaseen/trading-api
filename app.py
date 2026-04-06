from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "7926070108:AAGxP748l627ZzvsmLZtCxwQX912aLFE61U"
CHAT_ID = "-1003441215877"

@app.route("/")
def home():
    return "API WORKING"

@app.route("/trade", methods=["POST"])
def trade():
    data = request.json

    msg = f"""NEW TRADE

Symbol: {data.get('symbol')}
Type: {data.get('type')}
Entry: {data.get('entry')}
SL: {data.get('sl')}
TP: {data.get('tp')}
RR: {data.get('rr')}
Session: {data.get('session')}
"""

    send_telegram(msg)
    return jsonify({"status": "ok"})

@app.route("/result", methods=["POST"])
def result():
    data = request.json

    if data.get("result") == "WIN":
        msg = f"TP HIT\n{data.get('symbol')} +{data.get('profit')}"
    else:
        msg = f"SL HIT\n{data.get('symbol')} {data.get('profit')}"

    send_telegram(msg)
    return jsonify({"status": "updated"})

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
