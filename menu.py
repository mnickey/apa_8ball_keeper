import json
import os.path
from db import db
from seasons import seasons
from players import tandp

def start():
    print_header()
    db.json_check()
    seasons.archive_check()
    menu()
    menu_input()


def print_header():
    print("""
    ___________________________________
                                    ___`.
   _______________________________,'   \ `.
   ______________________________/,d$$$/   `.
                ,-.     ,-.       `$$$`.     `.
   :::::======o(   )   ((2))          `.`.     `.
                `-'     `-'             `.`.     `.
                         ,-.              `.`.     `.
                        ((7))               `.`.     `.
                         `-'                  `.`.
     `Two-ball in the corner-pocket'            `.
""")
    print("--------------------------------------")
    print("__APA 8 Ball Team & Player Collector__")
    print("--------------------------------------")

def menu():
    print("------------------------------")
    print("|       Menu Options         |")
    print("------------------------------")
    print("Start a [S]eason")
    print("[A]rchive a Season")
    print("Add a [T]eam")
    print("Add a [P]layer (to a team)")
    print("[R]emove a Player (from a team)")
    print("[U]date a Player Skill Level")
    print("[S]tart a Match!")
    print("E[X]it")


def menu_input():
    menu_choice = ''
    while menu_choice.lower() != 'x':
        menu_choice = input("Selection: ").lower()
        if menu_choice == 's':
            seasons.season_start()
            menu()
        elif menu_choice == 'a':
            seasons.archive_season()
            menu()
        elif menu_choice == 't':
            tandp.add_team()
            menu()
        elif menu_choice == 'p':
            tandp.add_player()
            menu()
        elif menu_choice == 'r':
            tandp.remove_player()
            menu()
        elif menu_choice == 'u':
            tandp.update_player()
            menu()
        elif menu_choice == 's':
            print("Let's play some pool!")
        elif menu_choice == 'x':
            print("Exiting...")
            exit()
        else:
            print("No valid selection given, please try again.")

start()
