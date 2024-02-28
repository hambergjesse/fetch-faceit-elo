import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch(username):
    FACEIT_API_KEY = os.getenv("FACEIT_API_KEY")
    url = f"https://open.faceit.com/data/v4/players?nickname={username}"
    headers = {"Authorization": f"Bearer {FACEIT_API_KEY}"}

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status() 
        data = res.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

    return None 

def testFunc(username):
    result = fetch(username)
    if result:
        if "games" in result and "cs2" in result["games"]:
            elo = result["games"]["cs2"]["faceit_elo"]
            return f"Elo: {elo}"
        else:
            return "CS2 game data not found."
    else:
        return "Failed to fetch data for the user."

print(testFunc("femboyrat"))
