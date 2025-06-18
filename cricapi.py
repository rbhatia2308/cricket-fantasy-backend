import requests

API_KEY = "your_cricapi_key_here"

def get_matches():
    url = f"https://api.cricapi.com/v1/matches?apikey={API_KEY}"
    response = requests.get(url)
    return response.json()
