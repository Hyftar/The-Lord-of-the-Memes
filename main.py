from player import Player
from strings import Str1

# Initiate Game
print(Welcome())
player_number = None
while True:
    try:
        player_number = int(input("How many players do you have?\n"))
        break
    except Exception as error:
        print(error)

players = []
for i in range(int(player_number)):
    players.append(Player(input("Player %s name:\n" % ((i + 1)))))

# Pick player stats
for p in players:
    print("Set attributes for player %s." % (p))
    p.Pick()
    for stat in p.stats:
        print('%s: %i' % (stat[0], stat[1]))
