import numpy


class EasterEggs():
    @staticmethod
    def NameEggs(player):
        if player.name == "God Trump Emperor":
            for stat in player.stats:
                stat[1] = 100
            print("Trump!\n" * 100)
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
        elif player.name == "Hillary Clinton" or player.name == "Richard Nixon":
            for stat in player.stats:
                stat[1] = 0
            print("It doesn't pay to be a crook!")
        elif player.name == "PC master race":
            for stat in player.stats:
                stat[1] = 10
            textlist = ["Fedora!", "420!", "Doritos!", "Mountain Dew!",
                        "Anonymous!", "git gewd", "trolololololo", "wow!",
                        "newfag!!", "consolers are plebians"]
            for text in range(20):
                n = int(numpy.random.randint(0, 10, 1))
                print(textlist[n])
        else:
            return True
        return False
