from flask import Flask, request, jsonify
from flask_cors import CORS 
import sqlite3

app = Flask(__name__)
CORS(app)  

def init_db():
    conn = sqlite3.connect('campaigns.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS campaigns
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, budget REAL, audience TEXT, summary TEXT)''')
    conn.commit()
    conn.close()

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_message = data.get('message')

    if "create campaign" in user_message.lower():
        response = "Sure! Let's create a campaign. What's the name of your campaign?"
    elif "budget" in user_message.lower():
        response = "Got it. What's your budget for this campaign?"
    elif "audience" in user_message.lower():
        response = "Who is your target audience?"
    elif "summary" in user_message.lower():
        response = "Here's a summary of your campaign."
    else:
        response = "I'm here to help you create a campaign. Let's start with the campaign name."

    return jsonify({"response": response})

@app.route('/save_campaign', methods=['POST'])
def save_campaign():
    data = request.json
    name = data.get('name')
    budget = data.get('budget')
    audience = data.get('audience')
    summary = data.get('summary')

    conn = sqlite3.connect('campaigns.db')
    c = conn.cursor()
    c.execute("INSERT INTO campaigns (name, budget, audience, summary) VALUES (?, ?, ?, ?)",
              (name, budget, audience, summary))
    conn.commit()
    conn.close()

    return jsonify({"message": "Campaign saved successfully!"})


@app.route('/get_campaigns', methods=['GET'])
def get_campaigns():
    conn = sqlite3.connect('campaigns.db')
    c = conn.cursor()
    c.execute("SELECT * FROM campaigns")
    campaigns = c.fetchall()
    conn.close()

    return jsonify({"campaigns": campaigns})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
