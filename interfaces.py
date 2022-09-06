# ┌────────────────────────
# │       INTERFACES
# └────────────────────────

# Function to create a team data

def buildTeam(
    name: str,
    rank: int,
    points: int,
    ) -> dict:
    return {
        'name': name,
        'rank': rank,
        'points': points,
    }

# Function to create a league data

def buildLeague(
    name: str,
    season: int,
    teams: list[buildTeam],
    ) -> dict:
    return {
        'name': name,
        'season': season,
        'teams': teams,
    }