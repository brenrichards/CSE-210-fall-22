import math
import random

play_again = "y"
points = 300

print(f"Your score is: {points} points.")

def get_inputs():
    hi_or_lo = input("Higher or Lower? [h/l]")   
    while hi_or_lo != "h" and hi_or_lo != "l":
        hi_or_lo = input("Input not recognized, enter h or l: ")
    return hi_or_lo

while play_again == "y":
    random_integer_1 = random.randint(1, 13)
    print(f"The card is {random_integer_1}")
    hi_or_lo = get_inputs()
    random_integer_2 = random.randint(1, 13)
    if hi_or_lo == "h" and random_integer_2 > random_integer_1:
        points = points + 100
        print(f"The card was higher")
    if hi_or_lo == "h" and random_integer_2 < random_integer_1: 
        points = points - 75
        print("The card was lower")
    if hi_or_lo == "l" and random_integer_2 > random_integer_1:
        points = points + 100
        print("The card was higher")
    if hi_or_lo == "l" and random_integer_2 < random_integer_1:
        points = points - 75
        print(f"The card was lower")
    play_again = input("Play again? [y/n] ")
    while play_again != "y" and play_again != "n":
        play_again = input("Enter [y/n] ")
