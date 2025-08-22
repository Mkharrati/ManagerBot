def extract_username(text: str):
    """
    extract username from user_info message text
    """
    text = text.split("\n")[0]
    text = text.split(":")[1].strip()
    return text

def bytetoGB(byte):
    '''convert byte to gigabyte'''
    return byte / 1073741824