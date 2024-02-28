import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch(username):
    FACEIT_API_KEY = os.getenv("FACEIT_API_KEY")
    url = f"https://open.faceit.com/data/v4/players?nickname={username}"
    headers = {"Authorization": f"Bearer {FACEIT_API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()

        if "message" in result:
            return None, result["message"]

        return result, None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None, None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None, None

def test_cs2_elo(username):
    result, error_message = fetch(username)

    # If the result is not None, it means the API request was successful
    if result is not None:
        # Check if the "games" key exists in the user data
        if "games" in result:
            # Check if the "cs2" key exists in the "games" data
            if "cs2" in result["games"]:
                # Check if the "faceit_elo" key exists in the "cs2" game data
                if "faceit_elo" in result["games"]["cs2"]:
                    elo = result["games"]["cs2"]["faceit_elo"]
                    return int(elo)
                else:
                    return "CS2 faceit_elo data not found."
            else:
                return "CS2 game data not found."
        else:
            return "User data not found."
    else:
        return error_message

print(test_cs2_elo("femboyrat"))