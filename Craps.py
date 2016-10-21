import random
from random import randint

die_1 = random.randint(1,7)
die_2 = random.randint(1,7)
total_roll = (die_1 + die_2)
player_currency = "100"

start_game = input("Would you like to start the game? ")

#Come out Roll
while "y" == start_game[0].lower():
    die_1 = random.randint(1,7)
    die_2 = random.randint(1,7)
    total_roll = (die_1 + die_2)
    roll = input("Roll dice. ")
    print(total_roll)
    if total_roll == 2 or total_roll == 3 or total_roll == 12:
        print("Round Over. You crapped out! All players lost their pass line bets!")
    elif total_roll == 7 or total_roll == 11:
        print("Round Over. All pass line bets win!")
    else:
        print((total_roll), " is the point. Moving on to the point phase.")
        point = (total_roll)

#Point Phase        
        while point == (total_roll):
            die_1 = random.randint(1,7)
            die_2 = random.randint(1,7)
            total_roll = (die_1 + die_2)
            roll = input("Roll dice. ")
            print(total_roll)
            if total_roll == point:
                print("You rolled the point number! All pass line bets win!")
            elif total_roll == 7:
                print("Round over. All pass line bets lose!")
            else:
                roll_again = input("Roll again.")
                point = (total_roll)
