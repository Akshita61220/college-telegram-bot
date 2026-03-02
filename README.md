# College Telegram Bot

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Telegram bot that provides information about the top 5 colleges in India with images, location, and ranking. Built with Python and MongoDB.

---

## Features

- `/start` - Welcome message  
- `/topcolleges` - Shows top 5 colleges with:
  - Image
  - Description
  - Location
  - Ranking  
- Unknown commands → Friendly error message

---

## Telegram Bot Preview

**Start Command:**  

User: /start
Bot: Welcome to the College Info Bot! Use /topcolleges to see top 5 colleges.


**Top Colleges Command:**  

User: /topcolleges
Bot: Shows each college with image, description, location, ranking


**Unknown Command:**  

User: /hello
Bot: Oops! Something went wrong. Use /topcolleges or /start.


---

## Top 5 Colleges Preview

| College       | Image |
|---------------|-------|
| IIT Bombay    | ![IIT Bombay](images/IIT_Bombay.jpg) |
| IIT Delhi     | ![IIT Delhi](images/IIT_Delhi.jpg) |
| IISc Bangalore| ![IISc Bangalore](images/IISc_Bangalore.jpg) |
| BITS Pilani   | ![BITS Pilani](images/BITS_Pilani.jpg) |
| NIT Trichy    | ![NIT Trichy](images/NIT_Trichy.jpg) |

---

## Project Structure


college-telegram-bot/
│
├─ bot.py # Main bot file
├─ config.py # Local config with BOT_TOKEN & Mongo URI (not pushed)
├─ config_example.py # Example config for GitHub
├─ database.py # MongoDB connection logic
├─ logic.py # Bot logic
├─ insert_sample_data.py # Script to insert sample data in MongoDB
├─ images/ # College images
├─ venv/ # Virtual environment (ignored)
└─ README.md # This file


---

## Setup Instructions

1. **Clone the repository**  
```bash
git clone https://github.com/Akshita61220/college-telegram-bot.git
cd college-telegram-bot

Create and activate virtual environment

python3 -m venv venv
source venv/bin/activate

Install dependencies

pip install python-telegram-bot pymongo

Create your local config file

Copy config_example.py to config.py

Add your BOT_TOKEN and MongoDB URI

# config.py
BOT_TOKEN = "YOUR_REAL_BOT_TOKEN"
MONGO_URI = "YOUR_REAL_MONGO_URI"

Insert sample data (optional)

python3 insert_sample_data.py

Run the bot

python3 bot.py
Usage

Open Telegram → Search your bot → Start

Use /start or /topcolleges commands

Unknown commands will show a friendly error

Notes

Never push your real config.py to GitHub

Keep config.py local, push only config_example.py

Make sure MongoDB is running and accessible

License

MIT License


---

### ✅ **Next Step to add README to GitHub**

1. Project folder me README create karo aur paste karo content:  

```bash
touch README.md
nano README.md   # ya koi editor open karo, content paste karo

Git add & commit:

git add README.md
git commit -m "Add professional README for College Telegram Bot"
git push
