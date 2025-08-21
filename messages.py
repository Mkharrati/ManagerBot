from api import (
    search_user
)

from utils import(
    BytetoGB
)

def start():
    message = '''
Hi!
Welcome to ManagerBot.
Send username for receive information.
'''
    return message

def user_info(username: str):
    info = search_user(username)
    match info:
        case (200, info):
            info = info['response']
            message = f'''
<b>Username : </b> {info['username']}
<b>Data Usage :</b> {BytetoGB(info['lifetimeUsedTrafficBytes'])}
<b>Expiration Date: </b> {info['expireAt']}
➖➖➖➖➖➖➖➖➖➖➖
<b>Subscription link : </b> <code>{info['subscriptionUrl']}</code>
'''
            return message
        case (404, info):
            return "User not found ❗️"
        case _:
            return str(info)

                 