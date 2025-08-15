from bot import (
    bot,
    admin_id
)
from messages import (
    start,
    user_info
)

@bot.message_handler(commands=["start"])
def handle_start(message):
    chat_id = message.chat.id
    if chat_id in admin_id:
        bot.send_message(chat_id, text=start())

@bot.message_handler(content_types="text")
def handle_search_user(message):
    chat_id = message.chat.id
    if chat_id in admin_id:
        message = user_info(message.text)
        bot.send_message(
            chat_id,
            text=message,
            parse_mode="HTML")

