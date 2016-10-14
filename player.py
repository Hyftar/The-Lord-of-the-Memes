class Player(object):
    def __init__(self, player_name):
        self.name = player_name
        self.health = 100
        self.inventory = []
        self.equipment = []
        self.stats = [
                    ['strength', None],
                    ['constitution', None],
                    ['defense', None],
                    ['dexterity', None],
                    ['intelligence', None],
                    ['charisma', None],
                    ['luck', None]
                    ]
        self.skill_points = 20

    def PrintPoints(self, initial=True, pick=False):
        if initial == 0:
            print("""
Attributes to set:
Strenght, Constitution, Defense, Dexterity, Intelligence, Charisma, Luck.
""")
        if self.skill_points != 0:
            print("You have %s points to set." % (self.skill_points))

    def Pick(self):
        # Implement loop to catch error for each attribute
        self.PrintPoints()

        for k, v in self.stats:
            a = None
            while True:
                try:
                    v = int(v)
                    self.skill_points -= self.strenght
                    if self.skill_points < 0:
                        self.skill_points += self.strenght
                        a = 0
                        1/a
                    self.PrintPoints(pick=True)
                    break
                except:
                    self.strenght = int(input("%s:\n" % (k)))
                    if a == 0:
                        self.PrintPoints(pick=True)
