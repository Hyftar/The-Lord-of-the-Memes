from player import Player
from strings import Str1


Str1()
while True:
    try:
        player_number = int(player_number)
        break
    except:
        player_number = input("How many players do you have?\n")
player = []
for _ in range(int(player_number)):
    player.append(Player(input("Player %s name:\n" % ((_+1)))))
print(player)
for _ in player:
    _.Pick()
