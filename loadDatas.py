import requests, os
from datetime import date
from dotenv import load_dotenv

today = date.today()

season = today.year

load_dotenv()

league_url = f"https://api-football-v1.p.rapidapi.com/v3/standings"

headers = {
	"X-RapidAPI-Key": os.getenv("API_KEY"),
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

# Function to call the league API endpoint 
# It first extracts and transforms the information 
# Into a message response for the Telegram Bot
def loadData(league: int) -> str:
    message = ""

    querystring = {"season":f"{season}","league": f"{league}"}

    response = requests.request("GET", league_url, headers=headers, params=querystring).json()

    league_info = response['response'][0]['league']

    message += f"Standings for '{league_info['name']}' {league_info['season']}\n"

    stands = league_info['standings'][0]

    for team in stands:
        message += f"{team['rank']}. -> {team['team']['name']} : {team['points']} points\n"

    return message 