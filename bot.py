import os
import json
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()

TELEGRAM_BOT_TOKEN= os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_ADMIN_CHAT_ID= json.loads(os.getenv('TELEGRAM_ADMIN_CHAT_ID'))
PANEL_URL= os.getenv('PANEL_URL')
PANEL_API_TOKEN= os.getenv('PANEL_API_TOKEN')

check_env = (TELEGRAM_BOT_TOKEN, TELEGRAM_ADMIN_CHAT_ID, PANEL_URL, PANEL_API_TOKEN)

for variable in check_env:
    if variable == "":
        raise ValueError("some of the environment variables is missed.")

bot = TeleBot(TELEGRAM_BOT_TOKEN)
admin_id = TELEGRAM_ADMIN_CHAT_ID


