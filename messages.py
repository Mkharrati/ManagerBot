from api import (
    search_user_by_username
)

from utils import(
    bytetoGB
)

def start():
    '''start message text'''
    message = '''
Hi!
Welcome to ManagerBot.
Send username for receive information.
'''
    return message

def user_info(username: str):
    '''get user info from api if exist and preparation suitable message text'''
    info = search_user_by_username(username)
    match info:
        case (200, info):
            info = info['response']
            message = f'''
<b>Username : </b> {info['username']}
<b>Data Usage :</b> {bytetoGB(info['lifetimeUsedTrafficBytes'])}
<b>Expiration Date: </b> {info['expireAt']}
➖➖➖➖➖➖➖➖➖➖➖
<b>Subscription link : </b> <code>{info['subscriptionUrl']}</code>
'''
            return message
        case (404, info):
            return "User not found ❗️"
        case _:
            return str(info)

                 