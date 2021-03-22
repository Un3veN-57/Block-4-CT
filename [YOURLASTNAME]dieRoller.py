"""
Ideas about how this could work!

-> import a random library switch between different dice
-> switch between different dice
-> Use text to ask user whatkind of dice to use
-> multiple places where random numbers  are generated
"""

import random

print("Dice Rolling Engine 1.0")
print("Hello! What kind of die do you want to roll?")
dieType = input("Type d20, d12, d8, d6, or d4:   ")
print("Thank You! Here's your roll: ")


#is a d20 is selected, pick a random number between 1 and 20
# we're using random.randint(x , y)


if dieType.lower() == "d20":
    print (random.randint(1, 20))

elif dieType.lower() == "d12":
    print(random.randint(1, 12))

elif dieType.lower() == "d8":
    print(random.randint(1, 8))

elif dieType.lower() == "d6":
    print(random.randint(1, 6))

elif dieType.lower() == "d4":
    print(random.randint(1, 4))

else:
    print("Try again with an actual die type, please!")

    
