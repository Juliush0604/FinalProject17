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
    start_item = input("\nWhat would like as your starting item?\n[Health Potion] [Mana Potion] [Scanner] [Torch]\n\n")
    if start_item.lower() == 'health potion':
        mcharacter.add_item('Health Potion')
        break
    elif start_item.lower() == 'mana potion':
        mcharacter.add_item('Mana Potion')
        break
    elif start_item.lower() == 'scanner':
        mcharacter.add_item('Scanner')
        break
    elif start_item.lower() == 'torch':
        mcharacter.add_item('Torch')
        mcharacter.vision = 1
        break
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
        print("There is one room in front of you")
    else:
        print(f'\nThere are {room_amount} rooms in front of you\n')

    #Describes rooms if user has torch
    if mcharacter.vision == 1:
        print("Thanks to your torch, you can see what is inside\n")
        n = 0
        for aroom in rooms:
            if rooms[n].treasure == 0 and rooms[n].healing == 0 and rooms[n].monster == 0:
                status = 'there is nothing'
            if rooms[n].treasure == 1 and rooms[n].healing == 0 and rooms[n].monster == 0:
                status = 'has a treasure chest'
            elif rooms[n].treasure == 0 and rooms[n].healing == 1 and rooms[n].monster == 0:
                status = 'has a healing spring'
            elif rooms[n].treasure == 0 and rooms[n].healing == 0 and rooms[n].monster == 1:
                status = 'there is a monster'
            elif rooms[n].treasure == 1 and rooms[n].healing == 1 and rooms[n].monster == 0:
                status = 'there is a treasure chest and a healing spring'
            elif rooms[n].treasure == 1 and rooms[n].healing == 0 and rooms[n].monster == 1:
                status = 'there is a monster and a treasure chest'
            elif rooms[n].treasure == 0 and rooms[n].healing == 1 and rooms[n].monster == 1:
                status = 'there is a monster and a healing spring'
            elif rooms[n].treasure == 1 and rooms[n].healing == 1 and rooms[n].monster == 1:
                status = 'there is a monster, treasure chest, and a healing spring'
            else:
                None
            room_num = n + 1
            print(f'In room {room_num} {status}\n')
            n = n + 1
    else:
        print("You cannot see beyond the darkness\n")

describe_rooms()

n = 1
rooms_to_enter = ''
for broom in rooms:
    rooms_to_enter += f'[Room {n}] '
    n = n + 1

target_room = input(f"Which room would you like to enter?\n{rooms_to_enter}\n\n")

current_room = room()

while True:
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
    print("There is a monster!\n")