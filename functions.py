"""Functions"""
def show_stats():
    print('Name', mcharacter.name)

"""Classes"""
class Warrior():
    """Warrior class"""

    inventory = {}

    def __init__(self):
        self.name = None
        self.health = 25
        self.mana = 0
        self.strength = 15
        self.vitality = 0.6
        self.magic = 8
        self.sense = 11
        self.dexerity = 11
        self.charisma = 12

    def add_item(self, item):
        self.inventory.update({item: 1})

"""Lists and Dictionaries"""