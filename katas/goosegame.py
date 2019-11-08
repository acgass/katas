
class GooseGame:
    def __init__(self, players):
        self.players = players

    def addplayer(self, player):
        if self.players.__contains__(player):
            print(player + ": already existing player")
            return self.players
        if len(self.players) == 2:
            print("Already at Max number of Players")
            return self.players
        self.players.append(player)
        return self.players


# game = GooseGame([]);
# answer = input("Would you like to play a game?")
# if answer == "yes":
#     while (len(game.players) < 2):
#         player = input("Please enter a player: ")
#         game.addplayer(player)
