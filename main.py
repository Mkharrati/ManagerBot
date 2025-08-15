from bot import bot
import handlers

if __name__ in "__main__":
    try:
        bot.polling()
    except Exception as er:
        raise ValueError(f"Bot crashed : {er}")