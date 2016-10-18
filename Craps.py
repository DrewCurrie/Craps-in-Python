import random
from random import randint#This code is terrible

die_1 = random.randint(1,7)
die_2 = random.randint(1,7)
black_die = die_1
white_die = die_2
total_roll = (die_1 + die_2)
player_currency = "100"

start_game = input("Would you like to start the game? ")

while start_game == "Yes" or "yes" or "Yeah" or "yeah" or "Y" or "y" or "start" or "Start":
    roll = input("Roll dice. ")
    if roll == (""):
        print(total_roll)
        if total_roll == 2 or 3 or 12:
            print("Round Over. You crapped out!")
        elif total_roll == 7 or 11:
            print("Round Over.")
        elif tota_roll == 5 or 6 or 8 or 9 or 10:
            print((total_roll), " is the point. Moving on to the point phase.")
