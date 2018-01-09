import random
"""Functions"""
rooms = []

class room():

    def __init__(self, name):
        self.name = 0
        self.treasure = 0
        self.healing = 0
        self.monster = 0

def room_creation():
    room_amount = random.randint(1,6)
    for name in range(room_amount):
        rooms.append(room(name))


room_creation()
print(rooms)
