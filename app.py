
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8257965645:AAEgvQYkwTMXmhgCsMkr4P27dsspotbvUcs"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/')
def home():
    return "Bot is running fine ✅"

@app.route('/webhook', methods=["POST"])
def webhook():
    data = request.get_json()
    if data and "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        reply = f"You said: {text}"
        requests.post(TELEGRAM_URL, json={"chat_id": chat_id, "text": reply})
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
