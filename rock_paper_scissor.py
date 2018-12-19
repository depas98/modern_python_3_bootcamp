# import random
from random import randint

user_choice = input("Enter your choice (R)ock, (S)cissors, (P)aper ").upper()

if user_choice == "R" or user_choice == "S" or user_choice == "P":
    computer_choice = randint(1,3)
    if computer_choice == 1:
         # ROCK
        computer_choice = "Rock"
    elif computer_choice == 2:
        # scissors
        computer_choice = "Scissors"
    else:
        # paper
        computer_choice = "Paper"

    print (f"The computer plays: {computer_choice}")
    computer_choice = computer_choice[0]

    if user_choice == computer_choice:
        print("It's a draw")
    elif user_choice == "R" and computer_choice == "S":
        print("You win yeah!!!")
    elif user_choice == "S" and computer_choice == "P":
        print("You win yeah!!!")
    elif user_choice == "P" and computer_choice == "R":
        print("You win yeah!!!")
    else:
        print("Computer wins!")
else:
    print("You must enter in R, S, or P")
