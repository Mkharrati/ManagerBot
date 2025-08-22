import requests

from bot import(
    PANEL_URL,
    PANEL_API_TOKEN
)

# headers for request to panel
HEADERS = {
      "Authorization": f"Bearer {PANEL_API_TOKEN}",
      "Content-Type": "application/json"
    }

def search_user_by_username(username: str):
    '''search users by username. return error or a tuple : (status code, json)'''
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