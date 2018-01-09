import random
"""Functions"""
def room_creation():
    for name in range(random.randint(0,6)):
        rooms.append(room(name))








"""Classes"""
class Warrior():
    """Warrior class"""

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

    def __init__(self):
        self.name = 0
        self.treasure = 0
        self.healing = 0
        self.monster = 0

"""Lists and Dictionaries"""
rooms = []