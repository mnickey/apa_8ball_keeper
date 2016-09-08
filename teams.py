class Team:
    def __init__(self, number=None, name=None):
        self.name = name
        self.number = number

    def add(self):
        team_name = input("Enter the team name: ")
        team_number = input("Enter the team number: ")
        self.name = team_name
        self.number = team_number

    def __repr__(self):
        return "The team name is {} and it's number is {}.".format(self.name, self.number)
