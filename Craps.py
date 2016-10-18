import random
from random import randint


player_currency = "100"

start_game = input("Would you like to start the game? ")

while "y" == start_game[0].lower():
    die_1 = random.randint(1,7)
    die_2 = random.randint(1,7)
    total_roll = (die_1 + die_2)
    roll = input("Roll dice. ")
    print(total_roll)
    if total_roll == 2 or total_roll == 3 or total_roll == 12:
        print("Round Over. You crapped out!")
    elif total_roll == 7 or total_roll == 11:
        print("Round Over.")
    else:
        print((total_roll), " is the point. Moving on to the point phase.")

