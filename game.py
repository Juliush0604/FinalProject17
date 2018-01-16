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
    start_item = input("\nWhat would like as your starting item? \n[Health Potion] [Mana Potion] [Scanner] [Torch]\n\n")
    if start_item.lower() == 'health potion':
        mcharacter.add_item('Health Potion')
        break
    elif start_item.lower() == 'mana potion':
        mcharacter.add_item('Mana Potion')
        break
    elif start_item.lower() == 'scanner':
        mcharacter.add_item('Scanner')
        break
    elif start_item.lower == 'torch':
        mcharacter.add_item('Torch')
        mcharacter.vision = 1
        break
    else:
        print('\nThat is not an option')

#Introduction
room_creation()
print("\n\n\n\n\n\n\n\n\n\nWelcome to the DEPTHS\n\nYou wake up in a dark room, unsure of where you are")
room_amount = len(rooms)
if room_amount == 1:
    print("There is one room in front of you")
else:
    print(f'\nThere are {room_amount} rooms in front of you\n')