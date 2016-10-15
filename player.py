class Player(object):
    def __init__(self, player_name):
        self.name = player_name
        self.health = 100
        self.inventory = []
        self.equipment = []
        self.stats = [
                    ['strength', 0],
                    ['constitution', 0],
                    ['defense', 0],
                    ['dexterity', 0],
                    ['intelligence', 0],
                    ['charisma', 0],
                    ['luck', 0]
                    ]
        self.skill_points = 20

    def PrintPoints(self, initial=True):
        if initial:
            print("""
Attributes to set:
Strenght, Constitution, Defense, Dexterity, Intelligence, Charisma, Luck.
You have %i points to assign
""" % (self.skill_points))
        else:
            print("You have %s points to assign." % (self.skill_points))

    def Pick(self):
        # Implement loop to catch error for each attribute
        self.PrintPoints()
        for i in range(len(self.stats)):
            if self.skill_points == 0:
                return
            element = self.stats[i]
            while True:
                try:
                    element[1] = int(input("%s:\n" % (element[0].capitalize())))
                    self.skill_points -= element[1]
                    if self.skill_points < 0:
                        self.skill_points += element[1]
                        raise Exception('Exceeded skill points to assign.')
                    self.PrintPoints(False)
                    break
                except Exception as error:
                    print(error)
