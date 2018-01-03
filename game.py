from functions import Warrior

#Asks for character class
mclass = input("Are you a Warrior, a Mage, or a Rogue?\n")

if mclass == "Warrior" or "warrior" or "W" or "w":
    mcharacter = Warrior()
else:
    None

#Asks for character name
mcharacter.name = input("What is your name?\n")

while True:
    start_item = input("What would like as your starting item? \n[Health Potion] [Mana Potion] [Wallet] [Torch]\n")
    if start_item == '1':
        mcharacter.add_item('Health Potion')
        break
    elif start_item == '2':
        mcharacter.add_item('Mana Potion')
        break
    elif start_item == '3':
        mcharacter.add_item('Wallet')
        break
    elif start_item == '4':
        mcharacter.add_item('Torch')
        break
    else:
        print('That is not an option')

from functions import show_stats