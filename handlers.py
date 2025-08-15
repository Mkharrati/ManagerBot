from bot import (
    bot,
    admin_id
)
from messages import (
    start
)

@bot.message_handler(commands=["start"])
def handle_start(message):
    chat_id = message.chat.id
    if chat_id in admin_id:
        bot.send_message(chat_id, text=start())
