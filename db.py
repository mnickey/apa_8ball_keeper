import os.path
import json

class db:
    def json_check():
        if os.path.exists('teams.json') == False:
            teams = open('teams.json', 'w')
        else:
            with open('teams.json', 'r') as teams_json:
                try:
                    teams = json.load(teams_json)
                except ValueError:
                    teams = {}
        if os.path.exists('players.json') == False:
            players = open('players.json', 'w')
        else:
            with open('players.json', 'r') as players_json:
                try:
                    players = json.load(players_json)
                except ValueError:
                    players = {}
        if os.path.exists('season.json') == False:
            season = open('season.json', 'w')
        else:
            with open('season.json', 'r') as season_json:
                try:
                    season = json.load(season_json)
                except ValueError:
                    season = {}
