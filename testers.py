import random
"""Functions"""
rooms = []
possibleRooms = ['room1', 'room2', 'room3', 'room4', 'room5', 'room6']

class room():

    def __init__(self, name, treasure, healing, monster):
        self.name = name
        self.treasure = 0
        self.healing = 0
        self.monster = 0



def room_creation():
    for rooms in range(random.randint(0,6)):
        rooms


room_creation('test')
print(test)