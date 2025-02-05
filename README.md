# Chatbot Campaign Manager

This project is a **Chatbot Campaign Manager** that allows users to interact with a chatbot to create and manage campaigns. The chatbot understands user inputs, asks relevant questions, and saves campaign details to a database. The frontend displays the chat interface and a list of saved campaigns.

---

## Features
1. **Chatbot Interaction**:
   - Users can chat with the bot to create campaigns.
   - The bot asks for campaign details like name, budget, and target audience.
2. **Campaign Management**:
   - Campaigns are saved to a SQLite database.
   - Users can view a list of all saved campaigns.
3. **Simple Interface**:
   - A clean and intuitive frontend for interacting with the chatbot and viewing campaigns.

---

## Technologies Used
- **Backend**: Python, Flask, SQLite
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: Fetch API for frontend-backend communication
- **Database**: SQLite for storing campaign data

---

## Setup and Installation

### Prerequisites
1. **Python 3.x**: Install Python from [python.org](https://www.python.org/).
2. **Flask**: Install Flask using pip:
   ```bash
   pip install flask flask-cors

---

##Project Structure

chatbot-campaign-manager/
│
├── app.py                # Backend: Flask server and chatbot logic
├── index.html            # Frontend: Chat interface and campaign list
├── README.md             # Project documentation
└── campaigns.db          # SQLite database (created automatically)
