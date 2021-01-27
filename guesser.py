import random

print("Welcome to the guessing game! \n, your objective is to guess the number \n that the computer randomly chose!")

x = input("Are you ready for the challenge? Yes or No\n")

if x == "Yes":
    userin = int(input("Okay!, Enter a random number between 1 and 5\n "))
    compin = random.randint(1, 6)
    if userin == compin:
        print("Congratulations! You have won!")
    else:
        print(f"Oops! It was {compin} Better luck next time!")
else:
    print("Okay! Cya!")
    exit()