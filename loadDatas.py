import requests, os
from datetime import date
from dotenv import load_dotenv
from interfaces import buildLeague, buildTeam

today = date.today()

season = today.year

load_dotenv()

league_url = f"https://api-football-v1.p.rapidapi.com/v3/standings"


headers = {
	"X-RapidAPI-Key": os.getenv("API_KEY"),
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

# Function to call the league API endpoint 
# It extracts and transforms the information to a custom interface
def loadData(league: int) -> dict:

    querystring = {"season":f"{season}","league": f"{league}"}

    response = requests.request("GET", league_url, headers=headers, params=querystring).json()

    league = response['response'][0]['league']

    stands = league['standings'][0]

    teams = []

    for team in stands:
        teams.append(buildTeam(
        name= team["team"]["name"],
        rank= team["rank"],
        points= team["points"],
        ))

    league = buildLeague(league['name'], league['season'], teams)
    return league 