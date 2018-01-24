import sys
import random
import math


from functions import Warrior
mcharacter = Warrior()

class SkeletonWarrior():

    def __init__(self):
        self.level = level
        self.health = round((2.71828 ** (level * 0.065) * 25) * random.uniform(0.6, 0.72),0)
        self.total_health = self.health
        self.mana = 0
        self.strength = round((2.71828 ** (level * 0.07) * 5) * random.uniform(0.5, 1.6),0)
        self.magic = 0
        self.sense = round((2.71828 ** (level * 0.02) * 9) * random.uniform(0.73, 1.05),0)
        self.dexerity = round((2.71828 ** (level * 0.03) * 15.8) * random.uniform(0.87, 1.44),0)
        self.barriers = 0
        self.money = round((30 + (20 * level)) * random.uniform(0.2, 0.9), 0)
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
        self.health = self.health + (self.total_health * 0.15)

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

level = 1
monster = SkeletonWarrior()

def battle():

    global mcharacter
    global skeleton
    global level

    accuracy_constant = round(56 + (76 * (math.log(mcharacter.dexerity / monster.sense))),0)
    while True:
        while True:
            print("\nYour health:", mcharacter.health)
            print("Enemy health:", monster.health)
            current_action = input("\nWhat will you do?\n[Attack]\n\n")
            if current_action.lower() == 'attack':
                print("\nYou swung your sword at the skeleton")
                attack = random.randint(0,100)
                if attack <= accuracy_constant:
                    print("\nYour attack hit!")
                    monster.health = monster.health - monster.strength
                    break
                elif attack >= accuracy_constant:
                    print("\nYou missed!")
                    break
                else:
                    print("Something went wrong...")
                    break
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
            level = level + 1
            break
        else:
            monster.action()

battle()