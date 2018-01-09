from functions import Warrior
import random

#Asks for character class
mclass = input("What are you?\n[Warrior] [Mage] [Rogue] [Priest]\n")

if mclass.lower() == "warrior":
    mcharacter = Warrior()
else:
    None

#Asks for character name
mcharacter.name = input("What is your name?\n")

while True:
    start_item = input("What would like as your starting item? \n[Health Potion] [Mana Potion] [Scanner] [Torch]\n")
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
        print('That is not an option')
