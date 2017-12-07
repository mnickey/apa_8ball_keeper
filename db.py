import os
import json

class db:
    def json_check():
## CHECK FOR TEAMS.JSON FILE, CREATE IT IF IT DOESN'T EXIST, AND OPEN THE JSON FILE
        if os.path.exists('teams.json') == False:
            teams = open('teams.json', 'w+') as teams_json
        else:
            with open('teams.json') as teams_json:
                teams = json.load(teams_json)
## CHECK FOR PLAYERS.JSON FILE, CREATE IT IF IT DOESN'T EXIST, AND OPEN THE JSON FILE
        if os.path.exists('players.json') == False:
            players = open('players.json', 'w+') as players_json
        else:
            with open('players.json') as players_json:
                players = json.load(players_json)
## CHECK FOR SEASONS.JSON FILE, CREATE IT IF IT DOESN'T EXIST, AND OPEN THE JSON FILE
        if os.path.exists('season.json') == False:
            season = open('season.json', 'w+') as season_json
        else:
            with open('seasons.json') as season_json:
                season = json.load(season_json)
