from bot import (
    bot,
    admin_id
)
from messages import (
    start,
    user_info,
)

from utils import(
    extract_username
)

from keyboards import (
    user_info_markup
)

# handle start command
@bot.message_handler(commands=["start"])
def handle_start(message):
    chat_id = message.chat.id
    if chat_id in admin_id:
        bot.send_message(chat_id, text=start())

# handle any text for search user
@bot.message_handler(content_types="text")
def handle_search_user(message):
    chat_id = message.chat.id
    if chat_id in admin_id:
        message = user_info(message.text)
        bot.send_message(
            chat_id,
            text=message,
            parse_mode="HTML",
            reply_markup=user_info_markup()
        )

# handle callback queries
@bot.callback_query_handler()
def handle_calls(call):
    match call.data:
        case "user_info_update":
            username = extract_username(call.message.text)
            text = user_info(username)
            # if the new message has no difference from previous one, an error will occur
            try:
                bot.edit_message_text(
                text = text,
                chat_id = call.message.chat.id,
                message_id = call.message.id,
                parse_mode="HTML",
                reply_markup=user_info_markup()
                )
            except:
                bot.answer_callback_query(
                    text="The user has not changed",
                    callback_query_id=call.id)
                pass
