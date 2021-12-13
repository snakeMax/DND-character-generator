import random
import math
from typing import Match


class Character:
    def __init__(self, modifiers):
        self.modifiers = modifiers

    def rstats(self, stre, dex, con, inte, wis, cha, race):
        if race == 1:
            stre += 2
            cha += 1
        elif race == 2:
            con += 2
        elif race == 3:
            dex += 2
        elif race == 4:
            inte += 2
        elif race == 5:
            cha += 2
            print("Choose an ability score to add +1")
            plus_1 = "f"
            plus_2 = "f"
            while not plus_1 or not plus_2 in ["stre","dex","con","inte","wis","cha"]:
                plus_1 = input("Type one of stre, dex, con, inte, wis, cha: ")
                plus_2 = input("Type one of stre, dex, con, inte, wis, cha: ")
                if plus_1 == plus_2:
                    plus_1 = "f"
            if plus_1 == "stre":
                stre += 1
            elif plus_1 == "dex":
                dex += 1
            elif plus_1 == "con":
                con += 1
            elif plus_1 == "inte":
                inte += 1
            elif plus_1 == "wis":
                wis += 1
            elif plus_1 == "cha":
                cha += 1
        elif race == 6:
            dex += 2
        elif race == 7:
            stre += 2
            con += 2
        elif race == 8:
            stre += 1
            dex += 1
            con += 1
            inte += 1
            wis += 1
            cha += 1
        elif race == 9:
            cha += 2
            inte += 1

        stre = math.floor((stre - 10)/2)
        dex = math.floor((dex - 10)/2)
        con = math.floor((con - 10)/2)
        inte = math.floor((inte - 10)/2)
        wis = math.floor((wis - 10)/2)
        cha = math.floor((cha - 10)/2)

        modifiers = [stre, dex, con, inte, wis, cha]
        return modifiers
    
    def rskills(self, one, two, three, four):
        one, two, three, four


# Beginning #
answer = False
while not answer:
    print("Choose a race:")
    print("1) Dragonborn")
    print("2) Dwarf")
    print("3) Elf")
    print("4) Gnome")
    print("5) Half-elf")
    print("6) Halfling")
    print("7) Half-orc")
    print("8) Human")
    print("9) Tiefling")
    race = int(input("Enter number: "))
    if race in [1,2,3,4,5,6,7,8,9]:
        answer = True


# print("Strength, dexterity, constitution, intelligence, wisdom, charisma =", Character.rstats(0, 0, 0, 0, 0, 0, 0))

# loop while an answer is not given, initiate stats based on input
answer = False
while not answer:
    print("Do you have your ability rolls?\n")
    print("1) Yes, manually assign stats\n")
    print("2) No, randomize my stats\n")
    rll = input("What next: ")
    if rll == "1":
        st = int(input("Input your strength stat:"))
        dx = int(input("Input your dexterity stat:"))
        cn = int(input("Input your constitution stat:"))
        it = int(input("Input your inteligence stat:"))
        wi = int(input("Input your wisdom stat:"))
        cr = int(input("Input your charisma stat:"))
        print("Calculating...")
        base_stats = [st, dx, cn, it, wi, cr]
        modifiers = Character.rstats(0, base_stats[0], base_stats[1], base_stats[2], base_stats[3], base_stats[4], base_stats[5], race)
        print("Rolled:", base_stats)
        print("Modifiers:", modifiers)
        answer = True
    elif rll == "2":
        print("Randomizing and Calculating...")
        st = random.randint(1, 20)
        dx = random.randint(1, 20)
        cn = random.randint(1, 20)
        it = random.randint(1, 20)
        wi = random.randint(1, 20)
        cr = random.randint(1, 20)
        base_stats = [st, dx, cn, it, wi, cr]
        modifiers = Character.rstats(0, base_stats[0], base_stats[1], base_stats[2], base_stats[3], base_stats[4], base_stats[5], race)
        print("Rolled:", base_stats)
        print("Modifiers:", modifiers)
        answer = True
    else:
        print("Error.")

# loop while no answer is given, choose skills
answer = False
while not answer:
    input()
    print("What skills you you want to put points into?")

input()
