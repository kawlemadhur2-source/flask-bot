
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8257965645:AAEgvQYkwTMXmhgCsMkr4P27dsspotbvUcs"
URL = f"https://api.telegram.org/bot{TOKEN}/"

@app.route('/')
def home():
    return "Bot is running fine ✅"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        send_message(chat_id, f"You said: {text}")
    return "ok"

def send_message(chat_id, text):
    url = URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
