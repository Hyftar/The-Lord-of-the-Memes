from strings import PrintPoints


class Player(object):
    def __init__(self, player_name):
        self.name = player_name
        self.health = 100
        self.inventory = []
        self.equipment = []
        self.strength = 0
        self.constitution = 0
        self.defense = 0
        self.dexterity = 0
        self.intelligence = 0
        self.charisma = 0
        self.luck = 0

    def Pick(self):
        points = 20
        self.strenght = input("Strenght:\n")
        points = points - self.strenght
        PrintPoints(points)
        self.constitution = input("Constitution:\n")
        points = points - self.constituion
        PrintPoints(points)
        self.defense = input("Defense:\n")
        points = points - self.defense
        PrintPoints(points)
        self.dexterity = input("Dexterity:\n")
        points = points - self.dexterity
        PrintPoints(points)
        self.intelligence = input("Intelligence:\n")
        points = points - self.intelligence
        PrintPoints(points)
        self.charisma = input("Charisma:\n")
        points = points - self.charisma
        PrintPoints(points)
        self.luck = input("Luck:\n")
        points = points - self.luck
        PrintPoints(points)
