import random
import math


class Character:
    def __init__(self, modifiers):
        self.modifiers = modifiers

    def rstats(self, stre, dex, con, inte, wis, cha):
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
        dx = int(input("Input your strength stat:"))
        cn = int(input("Input your strength stat:"))
        it = int(input("Input your strength stat:"))
        wi = int(input("Input your strength stat:"))
        cr = int(input("Input your strength stat:"))
        print("Calculating...")
        base_stats = [st, dx, cn, it, wi, cr]
        modifiers = Character.rstats(0, base_stats[0], base_stats[1], base_stats[2], base_stats[3], base_stats[4], base_stats[5])
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
        modifiers = Character.rstats(0, base_stats[0], base_stats[1], base_stats[2], base_stats[3], base_stats[4], base_stats[5])
        print("Rolled:", base_stats)
        print("Modifiers:", modifiers)
        answer = True
    else:
        print("Error.")

# loop while no answer is given, choose skills
answer = False
while not answer:
    print("What skills you you want to put points into?")

input()
