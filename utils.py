def extract_username(text: str):
    """
    extract username from user_info message text
    """
    text = text.split("\n")[0]
    text = text.split(":")[1].strip()
    return text

def BytetoGB(Byte):
    return Byte / 1073741824