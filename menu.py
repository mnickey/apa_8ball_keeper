from teams import Team


def main():
    print_header()
    menu()
    menu_input()


def print_header():
    print("------------------------------")
    print("  APA 8 Ball Scoring System")


def menu():
    print("------------------------------")
    print("        Menu Options")
    print("------------------------------")
    print("Add a [T]eam")
    print("Add a [P]layer (to a team)")
    print("[R]emove a player from a team")
    print("[U]date a players skill level")
    print("Review [M]enu choices")
    print("E[X]it")


def menu_input():
    menu_choice = ''
    while menu_choice.lower() != 'x':
        menu_choice = input("Selection: ").lower()
        if menu_choice == 't':
            print("entering team addition phase")
            team_name = input("What is the team name? ")
            team_num = input("What is the team number? ")
            add_team = Team(team_num, team_name)
            print(add_team.__repr__(), "\n")
            menu()
            #TODO the objects are being created, now store them somewhere
            # instead of a break we'll call the next set of functions
        elif menu_choice == 'p':
            print("entering player addition phase")
            # instead of a break we'll call the next set of functions
        elif menu_choice == 'r':
            print("entering player removal phase")
            # instead of a break we'll call the next set of functions
        elif menu_choice == 'u':
            print("entering player skill level update phase")
            # instead of a break we'll call the next set of functions
        elif menu_choice == 'm':
            print("entering menu review phase")
            menu()
        else:
            print("No valid selection given, please try again.")
    print("Exiting...")


if __name__ == '__main__':
    main()
