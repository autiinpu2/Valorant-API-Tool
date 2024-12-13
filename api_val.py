import requests

def get_puuid(riot_id, tagline):
    """
    Fetch the PUUID from the Riot Games API using a Riot ID and Tagline.

    Returns:
        str: The PUUID if the request is successful, or an error message if it fails.
    """
    API_KEY = "RGAPI-9e13d0a7-1dc7-4b2a-b9c9-f9057d8aff17" 
    base_url = "https://europe.api.riotgames.com"
    endpoint = "/riot/account/v1/accounts/by-riot-id/" + riot_id + "/" + tagline + "?api_key=RGAPI-9e13d0a7-1dc7-4b2a-b9c9-f9057d8aff17"
    headers = {"X-Riot-Token": API_KEY}

    try:
        response = requests.get(base_url + endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("puuid")  # Extract the 'puuid' field
    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            return {"error": "Forbidden - check API key permissions or endpoint URL"}
        return {"error": str(e)}


puuid = get_puuid("Apacoff", "9598")
