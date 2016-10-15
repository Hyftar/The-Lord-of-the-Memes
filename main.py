from player import Player
from strings import StoryStrings
from eastereggs import EasterEggs


# Initiate Game
print(StoryStrings.Welcome())
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
for player in players:
    print("Set attributes for player %s." % (player.name))
    if EasterEggs.NameEggs(player):
        player.Pick()
    for stat in player.stats:
        print('%s: %i' % (stat[0].capitalize(), stat[1]))
