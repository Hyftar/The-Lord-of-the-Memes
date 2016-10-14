from player import Player
from strings import Str1

# Initiate Game
Str1()
player_number = None
while True:
    try:
        player_number = int(player_number)
        break
    except:
        player_number = input("How many players do you have?\n")
player = []
for _ in range(int(player_number)):
    player.append(Player(input("Player %s name:\n" % ((_+1)))))
# Pick player stats
for _ in player:
    print("Set attributes for player %s." % (_.name))
    _.Pick()
    print("Picking attribute done!")
    