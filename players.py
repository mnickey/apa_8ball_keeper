import json
import os

teams = {}
players = {}

class tandp:
    def add_team():
        print("Let's add a new team!")
        team_name = input("Enter the team name here: ")
        team_num = input("Enter the team number here: ")
        print("Comitting data to database... ")
        teams[team_name] = team_num
        with open('teams.json', 'a') as teams_json:
            json.dump(teams, teams_json)

    def add_player():
        print("Let's add some players!")
        player_name = input("Enter the players name: ")
        skill_level = input("Enter the players skill level: ")
        player_team = input("Enter the team number for this player: ")
        print("Commiting data to database... ")
        players[player_name] = skill_level, player_team
        with open('players.json', 'a') as players_json:
            json.dump(players, players_json)

    def remove_player():
        remove_player_name = input("Which player should be removed? ")
        if remove_player_name in players:
            del players[remove_player_name]
        else:
            print("Sorry", remove_player_name, "was not found!")

    def update_player():
        update_player_data = input("Which player should be updated? ")
        if update_player_data in players:
            del players[update_player_data]
            print("Removing players data... ")
            print("Now let's re-add that player with the correct info...")
            tandp.add_player()
        else:
            print("Sorry", update_player_data, "was not found!")
