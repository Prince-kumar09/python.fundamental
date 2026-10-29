class Player:
    def __init__(self,name):
        self.name=name

class Team:
    def __init__(self,player):
        self.player=player

    def show_name(self):
        print("Player name:",self.player.name)

s1=Player("Rahul")
Team1=Team(s1)
Team1.show_name()
