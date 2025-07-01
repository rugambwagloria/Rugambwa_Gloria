import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()



class YTelegramAgent:
    def __init__(self, bot_token, channel_username):
        self.bot_token = bot_token
        self.channel_username = channel_username
        self.api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

    def create_post(self, message):
        payload = {
            'chat_id': self.channel_username, 
            'text': message,
            'parse_mode': 'HTML'
        }
        response = requests.post(self.api_url, json=payload)
        return response.json()

    def automate_posts(self, messages, delay=10):
        for msg in messages:
            result = self.create_post(msg)
            print(f"Posted: {msg} | Result: {result}")
            time.sleep(delay)


if __name__ == "__main__":
    
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHANNEL_USERNAME = os.getenv("TELEGRAM_CHANNEL_USERNAME")
    agent = YTelegramAgent(TELEGRAM_BOT_TOKEN,TELEGRAM_CHANNEL_USERNAME)

    posts = [
        "Hello, this is an automated post!",
        "Stay tuned for more updates.",
        "Follow us for the latest news."
        "What would you want to see next?",
        "Engaging with our community is important!",
    ]

    agent.automate_posts(posts, delay=5)
    
    