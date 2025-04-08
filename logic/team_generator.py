# logic/team_generator.py
from utils.zodiac import get_element

def generate_teams(profils):
    equipes = {}
    for p in profils:
        p["element"] = get_element(p["zodiac"])

    profils.sort(key=lambda x: x["element"])
    team_size = 2
    team_id = 0

    for i in range(0, len(profils), team_size):
        equipes[team_id] = profils[i:i+team_size]
        team_id += 1

    return equipes