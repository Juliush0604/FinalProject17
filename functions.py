"""Functions"""
def room_creation():
    rooms = random.randint(0,6)
    print(f"There are {rooms} rooms in front of you.")
    if mcharacter.vision == 0:
        print("You cannot see anything within the rooms")
    else:






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

"""Lists and Dictionaries"""