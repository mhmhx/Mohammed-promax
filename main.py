from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import datetime

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/')
def home():
    return send_from_directory('', 'index.html')

@app.route('/send.html')
def send_page():
    return send_from_directory('', 'send.html')

@app.route('/style.css')
def style():
    return send_from_directory('', 'style.css')

@app.route('/send-news', methods=['POST'])
def send_news():
    data = request.get_json()
    new_message = {
        'text': data['text'],
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    try:
        with open('messages.json', 'r', encoding='utf-8') as f:
            messages = json.load(f)
    except:
        messages = []

    messages.append(new_message)

    with open('messages.json', 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

    return jsonify({"message": "تم الإرسال بنجاح!"})

@app.route('/get-news')
def get_news():
    try:
        with open('messages.json', 'r', encoding='utf-8') as f:
            messages = json.load(f)
    except:
        messages = []
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)