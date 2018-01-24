#Import math, random, and sys modules
import sys
import random
import math

#Bunch of imports from function.py
from functions import Warrior
from functions import room
from functions import rooms
from functions import room_creation

#Asks for character class
while True:
    mclass = input("What are you?\n[Warrior]\n\n")

    if mclass.lower() == "warrior":
        mcharacter = Warrior()
        break
    else:
        print("\nThat is not a valid option\n")

#Asks for character name
mcharacter.name = input("\nWhat is your name?\n\n")

while True:
    #Character Creation
    start_item = input("\nWhat would like as your starting item?\n[Torch]\n\n")
    #If adding more items
    """
    if start_item.lower() == 'health potion':
        mcharacter.add_item('Health Potion')
        break
    elif start_item.lower() == 'mana potion':
        mcharacter.add_item('Mana Potion')
        break
    elif start_item.lower() == 'scanner':
        mcharacter.add_item('Scanner')
        mcharacter.scan = 1
        break
    """
    #Only possible item
    if start_item.lower() == 'torch':
        mcharacter.add_item('Torch')
        mcharacter.vision = 1
        break
    #Make sure there aren't errors
    else:
        print('\nThat is not an option')

#Introduction
room_creation()
print("\nWelcome to THE DEPTHS\n\nYou wake up in a dark room, unsure of where you are")

#Function to describes rooms, not sure how to import mcharacter.vision to other file so this function is on this file
def describe_rooms():
    global mcharacter
    room_amount = len(rooms)
    if room_amount == 1:
        print("\nThere is one room in front of you")
    else:
        print(f'\nThere are {room_amount} rooms in front of you\n')

    #Describes rooms if user has torch
    if mcharacter.vision == 1:
        print("Thanks to your torch, you can see what is inside\n")
        n = 0
        for aroom in rooms:
            if rooms[n].monster == 0:
                status = 'there is nothing'
            elif rooms[n].monster == 1:
                status = 'there is a monster'
            else:
                None
            room_num = n + 1
            print(f'In room {room_num} {status}\n')
            n = n + 1
    else:
        print("You cannot see beyond the darkness\n")

#Function to describes stimulate battle, not sure how to import mcharacter from other file so it is in this one
def battle():
    """Battle stimulator"""

    global mcharacter
    global skeleton

    #Calculates accuracy of user
    accuracy_constant = round(56 + (76 * (math.log(mcharacter.dexerity / monster.sense))),0)

    while True:

        print("\nYour health:", round(mcharacter.health,2))
        print("Enemy health:", round(monster.health,2))

        while True:
            current_action = input("\nWhat will you do?\n[Attack]\n\n")
            if current_action.lower() == 'attack':
                print("\nYou swung your sword at the skeleton")
                attack = random.randint(0,100)
                if attack <= accuracy_constant:
                    print("\nYour attack hit!")
                    monster.health = monster.health - mcharacter.strength
                    break
                elif attack >= accuracy_constant:
                    print("\nYou missed!")
                    break
                else:
                    print("Something went wrong...")
            else:
                print("That is not a valid option")
        if mcharacter.health <= 0:
            print("\nYou died!!!")
            sys.exit()
        if monster.health <= 0:
            print("\nYou killed the skeleton!")
            mcharacter.health = mcharacter.health + monster.total_health
            mcharacter.strength = mcharacter.strength + (monster.strength * 0.3)
            mcharacter.sense = mcharacter.sense + (monster.sense * 0.1)
            mcharacter.dexerity = mcharacter.dexerity + (monster.dexerity * 0.3)
            break
        else:
            monster.action()

class SkeletonWarrior():
    """Skeleton Class, not sure how to edit level variable across files so it is in this one"""
    def __init__(self):
        self.level = 1
        self.health = round((2.71828 ** (self.level * 0.065) * 25) * random.uniform(0.3, 0.36),0)
        self.total_health = self.health
        self.mana = 0
        self.strength = round((2.71828 ** (self.level * 0.07) * 5) * random.uniform(0.25, 0.8),0)
        self.magic = 0
        self.sense = round((2.71828 ** (self.level * 0.02) * 9) * random.uniform(0.36, 0.50),0)
        self.dexerity = round((2.71828 ** (self.level * 0.03) * 15.8) * random.uniform(0.43, 0.77),0)
        self.barriers = 0
        self.money = round((30 + (20 * self.level)) * random.uniform(0.2, 0.9), 0)
        self.c_cooldown = 0
        self.h_cooldown = 0
        self.name = 'skeleton'

    def attack(self):

        global mcharacter

        accuracy_constant = round(56 + (76 * (math.log(monster.dexerity / mcharacter.sense))),0)

        print("\nThe skeleton warrior swung at you with its sword")
        attack = random.randint(0,100)
        if attack <= accuracy_constant:
            print("\nYou got hit!")
            mcharacter.health = mcharacter.health - monster.strength
        elif attack >= accuracy_constant:
            print("\nIt missed!")
        else:
            print("Something went wrong...")

    def heal(self):

        print("\nThe skeleton warrior covers itself in dirt and lets loose a high pitched screech. It seems to have recovered some health")
        self.health = self.health + (self.total_health * 0.4)

    def action(self):

        global mcharacter
        global h_cooldown

        if self.health <= (self.total_health * 0.5) and self.h_cooldown == 0:
            self.heal()
            self.h_cooldown = 3
        elif self.health > (self.total_health * 0.5) or self.h_cooldown > 0:
            self.attack()
        else:
            print("What is going on")

#Code if adding more stuff to rooms
"""
elif rooms[n].treasure == 1 and rooms[n].healing == 0 and rooms[n].monster == 0:
status = 'has a treasure chest'
elif rooms[n].treasure == 0 and rooms[n].healing == 1 and rooms[n].monster == 0:
status = 'has a healing spring'
elif rooms[n].treasure == 1 and rooms[n].healing == 1 and rooms[n].monster == 0:
status = 'there is a treasure chest and a healing spring'
elif rooms[n].treasure == 1 and rooms[n].healing == 0 and rooms[n].monster == 1:
status = 'there is a monster and a treasure chest'
elif rooms[n].treasure == 0 and rooms[n].healing == 1 and rooms[n].monster == 1:
status = 'there is a monster and a healing spring'
elif rooms[n].treasure == 1 and rooms[n].healing == 1 and rooms[n].monster == 1:
status = 'there is a monster, treasure chest, and a healing spring'
"""

monster = SkeletonWarrior()

while True:
    print(f"\nYou are on level {monster.level}")

    describe_rooms()

    n = 1
    rooms_to_enter = ''
    for broom in rooms:
        rooms_to_enter += f'[Room {n}] '
        n = n + 1

    current_room = room()

    while True:
        target_room = input(f"Which room would you like to enter?\n{rooms_to_enter}\n\n")

        if target_room.lower() == 'room 1':
            current_room = rooms[0]
            break
        elif target_room.lower() == 'room 2':
            current_room = rooms[1]
            break
        elif target_room.lower() == 'room 3':
            current_room = rooms[2]
            break
        elif target_room.lower() == 'room 4':
            current_room = rooms[3]
        elif target_room.lower() == 'room 5':
            current_room = rooms[4]
            break
        elif target_room.lower() == 'room 6':
            current_room = rooms[5]
            break
        else:
            print("That is not a valid option")
    if current_room.monster == 1:
        print("\nYou tentatively walk into the room. There is a monster!")
        battle()
        monster.level = monster.level + 1
        monster.health = monster.total_health + 1
    else:
        None
    if monster.level == 11:
        print("You won!")
        sys.exit()
    else:
        None