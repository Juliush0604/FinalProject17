from functions import Warrior
from functions import room_creation
from functions import rooms

mcharacter = Warrior()

room_creation()

while True:
    #Character Creation
    start_item = input("What would like as your starting item?\n[Health Potion] [Mana Potion] [Scanner] [Torch]\n\n")
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
        print('\nThat is not an option\n')

print("\nWelcome to the DEPTHS\n\nYou wake up in a dark room, unsure of where you are")
room_amount = len(rooms)
if room_amount == 1:
    print("There is one room in front of you")
else:
    print(f'\nThere are {room_amount} rooms in front of you\n')

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
        print(f'Room {room_num} {status}\n')
        n = n + 1

else:
    print("You cannot see beyond the darkness\n")