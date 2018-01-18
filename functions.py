import random
"""Functions"""
#Creates up to 6 rooms
def room_creation():
    for amount in range(random.randint(0,6)):
        rooms.append(room())
    n = 0
    for some in rooms:
        rooms[n].treasure_chance()
        rooms[n].healing_chance()
        rooms[n].monster_chance()
        #Just to make sure room creation works
        """
        print(rooms[n].treasure)
        print(rooms[n].healing)
        print(rooms[n].monster)
        """
        n = n + 1

"""Classes"""
class Warrior():
    #Warrior Class

    inventory = {}

    def __init__(self):
        self.name = None
        self.health = 25
        self.mana = 0
        self.strength = 15
        self.vitality = 8
        self.magic = 8
        self.sense = 11
        self.dexerity = 11
        self.charisma = 12
        self.barriers = 0
        self.wealth = 0
        self.vision = 0

    def add_item(self, item):
        self.inventory.update({item: 1})

    def show_stats(self):
        print('Name:', self.name)
        print('Health:', self.health)
        print('Mana:', self.mana)
        print('Strength:', self.strength)
        print('Vitality:', self.vitality)
        print('Magic:', self.magic)
        print('Sense:', self.sense)
        print('Dexerity:', self.dexerity)
        print('Barriers:', self.charisma)
        print('Name:', self.barriers)
        print("Wealth:", self.wealth)

class room():
#Room Class
    def __init__(self):
        self.treasure = 0
        self.healing = 0
        self.monster = 0

    def treasure_chance(self):
        tchance = random.randint(0,100)
        if tchance < 40:
            self.treasure = 1
        else:
            self.treasure = 0

    def healing_chance(self):
        hchance = random.randint(0,100)
        if hchance < 10:
            self.healing = 1
        else:
            self.healing = 0

    def monster_chance(self):
        mchance = random.randint(0,100)
        if mchance < 60:
            self.monster = 1
        else:
            self.monster = 0

class Skeleton():

    def __init__(self, health, mana, strength, magic, dexerity, barriers, money, name):
        self.level = level
        self.health = health
        self.mana = mana
        self.strength = strength
        self.magic = magic
        self.dexerity = dexerity
        self.barriers = barriers
        self.money = money
        self.name = 'skeleton'

"""Lists and Dictionaries"""
#Creates temporary list of rooms
rooms = []