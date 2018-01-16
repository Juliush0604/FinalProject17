import random
"""Functions"""

rooms = []

class room():

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


def room_creation():
    for amount in range(random.randint(0,6)):
        rooms.append(room())
    n = 0
    for some in rooms:
        rooms[n].treasure_chance()
        rooms[n].healing_chance()
        rooms[n].monster_chance()
        print(rooms[n].treasure)
        print(rooms[n].healing)
        print(rooms[n].monster, "\n\n")
        n = n + 1


room_creation()