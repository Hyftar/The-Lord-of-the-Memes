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
        self.skill_points = 20

    def PrintPoints(self):
        print("""
Attributes to set:
Strenght, Constitution, Defense, Dexterity, Intelligence, Charisma, Luck.
""")
        if self.skill_points != 0:
            print("You have %s points to set." % (self.skill_points))

    def Pick(self):
        # Implement loop to catch error for each attribute
        while True:
            try:
                self.strenght = int(self.strenght)
                self.skill_points = self.skill_points - self.strenght
                if self.skill_points < 0:
                    self.skill_points = 0
                    a = 1/self.skill_points
                self.PrintPoints()
                break
            except:
                self.strenght = int(input("Strenght:\n"))
        while True:
            try:
                self.constitution = int(self.constitution)
                self.skill_points = self.skill_points - self.constitution
                if self.skill_points < 0:
                    self.skill_points = 0
                    a = 1/self.skill_points
                self.PrintPoints()
                break
            except:
                self.constitution = int(input("Constitution:\n"))
        while True:
            try:
                self.defense = int(self.defense)
                self.skill_points = self.skill_points - self.defense
                if self.skill_points < 0:
                    self.skill_points = 0
                    a = 1/self.skill_points
                self.PrintPoints()
                break
            except:
                self.defense = int(input("Defense:\n"))
        while True:
            try:
                self.dexterity = int(self.dexterity)
                self.skill_points = self.skill_points - self.dexterity
                if self.skill_points < 0:
                    self.skill_points = 0
                    a = 1/self.skill_points
                self.PrintPoints()
                break
            except:
                self.dexterity = int(input("Dexterity:\n"))
        while True:
            try:
                self.intelligence = int(self.intelligence)
                self.skill_points = self.skill_points - self.intelligence
                if self.skill_points < 0:
                    self.skill_points = 0
                    a = 1/self.skill_points
                self.PrintPoints()
                break
            except:
                self.intelligence = int(input("Intelligence:\n"))
        while True:
            try:
                self.charisma = int(self.charisma)
                self.skill_points = self.skill_points - self.charisma
                if self.skill_points < 0:
                    self.skill_points = 0
                    a = 1/self.skill_points
                self.PrintPoints()
                break
            except:
                self.charisma = int(input("Charisma:\n"))
        while True:
            try:
                self.luck = int(self.luck)
                self.skill_points = self.skill_points - self.luck
                if self.skill_points < 0:
                    self.skill_points = 0
                    a = 1/self.skill_points
                self.PrintPoints()
                break
            except:
                self.luck = int(input("Luck:\n"))
