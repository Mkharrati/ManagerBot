from telebot.types import(
    InlineKeyboardMarkup,
    InlineKeyboardButton
)



def user_info_markup():
    update_btn = InlineKeyboardButton(
        text="🔄 update",
        callback_data="user_info_update"
    )
    markup = InlineKeyboardMarkup(row_width=2)
    markup.row(update_btn)
    return markup