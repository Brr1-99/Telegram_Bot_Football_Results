from loadDatas import loadData

leagues_id = {
    "Premier League": 39,
    "Ligue 1": 61,
    "Bundesliga": 78,
    "Serie A": 135,
    "LaLiga" : 140,

}

leagues_id = [39, 61, 78, 135, 140]

for id in leagues_id:
    data = loadData(league=id)
