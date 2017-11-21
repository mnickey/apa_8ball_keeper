import os
import json

class db:
    def json_check():
        if os.path.exists('teams.json') == False:
            t = open('teams.json', 'w+')
        else:
            with open('teams.json') as teams_json:
                teams = json.load(teams_json)
        if os.path.exists('players.json') == False:
            p = open('players.json', 'w+')
        else:
            with open('players.json') as players_json:
                players = json.load(players_json)
        if os.path.exists('season.json') == False:
            s = open('season.json', 'w+')
