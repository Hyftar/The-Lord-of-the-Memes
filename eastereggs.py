class EasterEggs():
    @staticmethod
    def NameEggs(player):
        if player.name == "God Trump Emperor":
            for stat in player.stats:
                stat[1] = 100
            print("Trump!\n"*100)
        elif player.name == "Pepe the frog":
            for stat in player.stats:
                stat[1] = 1
            print("Feels bad man...")
        elif player.name == "Morgan Freeman":
            for stat in player.stats:
                stat[1] = 10E10
            print("You are god... but still black.")
        elif player.name == "Rotaru":
            for stat in player.stats:
                stat[1] = 0
            print("Learn to python, pleb.")
        else:
            return True
