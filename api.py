import requests

from bot import(
    PANEL_URL,
    PANEL_API_TOKEN
)

HEADERS = {
      "Authorization": f"Bearer {PANEL_API_TOKEN}",
      "Content-Type": "application/json"
    }

def search_user(username: str):
    url = f"{PANEL_URL}/api/users/by-username/{username}"
    try:
        response =  requests.get(
        url=url,
        headers=HEADERS
    )
    except Exception as er:
        return f"An error occurred : {er}"
    
    return (
        response.status_code,
        response.json()
    )