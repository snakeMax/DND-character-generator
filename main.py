import random
import math


class Character:
    def __init__(self, modifiers):
        self.modifiers = modifiers

    def rstats(self, stre, dex, con, inte, wis, cha):
        if stre == 0:
            stre = math.floor((random.randint(1, 20) - 10)/2)

        if dex == 0:
            dex = math.floor((random.randint(1, 20) - 10)/2)

        if con == 0:
            con = math.floor((random.randint(1, 20) - 10)/2)

        if inte == 0:
            inte = math.floor((random.randint(1, 20) - 10)/2)

        if wis == 0:
            wis = math.floor((random.randint(1, 20) - 10)/2)

        if cha == 0:
            cha = math.floor((random.randint(1, 20) - 10)/2)
        modifiers = stre, dex, con, inte, wis, cha
        return stre, dex, con, inte, wis, cha


# print("Strength, dexterity, constitution, intelligence, wisdom, charisma =", Character.rstats(0, 0, 0, 0, 0, 0, 0))
# exit()
answer = False
while not answer:
    rll = input("Do you have your ability rolls? y/n\n")
    if rll == "y" or "Y" or "Yes" or "yes":
        st = input("Input your strength stat:")
        dx = input("Input your strength stat:")
        cn = input("Input your strength stat:")
        it = input("Input your strength stat:")
        wi = input("Input your strength stat:")
        cr = input("Input your strength stat:")
        print("Calculating...")
        answer = True
    elif rll == "n" or "N" or "No" or "no":
        print("Randomizing and Calculating...")
        answer = True
    else:
        print("Error.")

input()