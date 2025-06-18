import requests

API_KEY = "c6962711-0540-49d3-806d-d23a03ddae59"

def get_matches():
    url = f"https://api.cricapi.com/v1/matches?apikey={API_KEY}"
    response = requests.get(url)
    return response.json()
