import random


def RollDice(rolls):
    for i in range(0, rolls):
        number = random.randint(1, 6)
        print(number)
        Menu()


def Menu():
    print("1. Roll a Dice")
    print("2. Roll multiple dice  ")
    print(".........")
    print("Exit program")

    choice = int(input("Enter Here: "))
    if choice == 1:
        RollDice(1)
    if choice == 2:
        rolls = int(input("How many rolls?"))
        RollDice(rolls)
    if choice == 3:
        exit()


Menu()
