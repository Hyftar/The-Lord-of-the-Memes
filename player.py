class Player(object):
    def __init__(self, player_name):
        self.name = player_name
        self.health = 100
        self.inventory = []
        self.equipment = []
        self.strength = None
        self.constitution = None
        self.defense = None
        self.dexterity = None
        self.intelligence = None
        self.charisma = None
        self.luck = None
        self.skill_points = 20

    def PrintPoints(self, initial=True, pick=False):
        if initial is True:
            print("""
Attributes to set:
Strenght: %d, Constitution: %d, Defense: %d, Dexterity: %d, Intelligence: %d,
Charisma: %d, Luck: %d.
""")
        if self.skill_points != 0 or pick is True:
            print("You have %s points to set." % (self.skill_points))

    def Pick(self):
        # Implement loop to catch error for each attribute
        self.PrintPoints()
        a = None
        b = None
        c = None
        d = None
        e = None
        f = None
        g = None
        while True:
            try:
                self.strenght = int(self.strenght)
                self.skill_points -= self.strenght
                if self.skill_points < 0:
                    self.skill_points += self.strenght
                    a = 0
                    1/a
                self.PrintPoints(pick=True)
                break
            except:
                self.strenght = input("Strenght:\n")
                if a == 0:
                    self.PrintPoints(initial=False, pick=True)
        while True:
            try:
                self.constitution = int(self.constitution)
                self.skill_points -= self.constitution
                if self.skill_points < 0:
                    self.skill_points += self.constitution
                    b = 0
                    1/b
                self.PrintPoints(pick=True)
                break
            except:
                self.constitution = input("Constitution:\n")
                if b == 0:
                    self.PrintPoints(initial=False, pick=True)
        while True:
            try:
                self.defense = int(self.defense)
                self.skill_points -= self.defense
                if self.skill_points < 0:
                    self.skill_points += self.defense
                    c = 0
                    1/c
                self.PrintPoints(pick=True)
                break
            except:
                self.defense = input("Defense:\n")
                if c == 0:
                    self.PrintPoints(initial=False, pick=True)
        while True:
            try:
                self.dexterity = int(self.dexterity)
                self.skill_points -= self.dexterity
                if self.skill_points < 0:
                    self.skill_points += self.dexterity
                    d = 0
                    1/d
                self.PrintPoints(pick=True)
                break
            except:
                self.dexterity = input("Dexterity:\n")
                if d == 0:
                    self.PrintPoints(initial=False, pick=True)
        while True:
            try:
                self.intelligence = int(self.intelligence)
                self.skill_points -= self.intelligence
                if self.skill_points < 0:
                    self.skill_points += self.intelligence
                    e = 0
                    1/e
                self.PrintPoints(pick=True)
                break
            except:
                self.intelligence = input("Intelligence:\n")
                if e == 0:
                    self.PrintPoints(initial=False, pick=True)
        while True:
            try:
                self.charisma = int(self.charisma)
                self.skill_points -= self.charisma
                if self.skill_points < 0:
                    self.skill_points += self.charisma
                    f = 0
                    1/f
                self.PrintPoints(pick=True)
                break
            except:
                self.charisma = input("Charisma:\n")
                if f == 0:
                    self.PrintPoints(initial=False, pick=True)
        while True:
            try:
                self.luck = int(self.luck)
                self.skill_points -= self.luck
                if self.skill_points < 0:
                    self.skill_points += self.luck
                    g = 0
                    1/g
                self.PrintPoints(pick=True)
                break
            except:
                self.luck = input("Luck:\n")
                if g == 0:
                    self.PrintPoints(initial=False, pick=True)
