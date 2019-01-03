# import random
from random import randint

player_wins = 0
computer_wins = 0

wins_needed = 3

# for count in range(3):
while player_wins < wins_needed and computer_wins < wins_needed:
    print(f"Player Score: {player_wins}")
    print(f"Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    user_choice = input("Enter your choice (R)ock, (S)cissors, (P)aper ").upper()

    if user_choice == "QUIT" or user_choice == "Q":
        break

    if user_choice == "R" or user_choice == "S" or user_choice == "P":
        computer_choice = randint(1, 3)
        if computer_choice == 1:
            # ROCK
            computer_choice = "Rock"
        elif computer_choice == 2:
            # scissors
            computer_choice = "Scissors"
        else:
            # paper
            computer_choice = "Paper"

        print(f"The computer plays: {computer_choice}")
        computer_choice = computer_choice[0]

        if user_choice == computer_choice:
            print("It's a draw")
        elif user_choice == "R" and computer_choice == "S":
            print("You win yeah!!!")
            player_wins += 1
        elif user_choice == "S" and computer_choice == "P":
            print("You win yeah!!!")
            player_wins += 1
        elif user_choice == "P" and computer_choice == "R":
            print("You win yeah!!!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

    else:
        print("You must enter in R, S, or P")

print(f"Final Scores... Player: {player_wins} Computer: {computer_wins}")

if player_wins > computer_wins:
    print("Congrats you win")
elif player_wins < computer_wins:
    print("Computer wins")
else:
    print("It's a tie")
