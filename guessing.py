from random import randint

number_to_guess = randint(1, 10)

while True:
    try:
        user_guess = input("What is your guess from 1 to 10: ")
        user_guess = int(user_guess)

        if user_guess < number_to_guess:
            print("number is too low")
        elif user_guess > number_to_guess:
            print("number is too high")
        else:
            print("you won!!!!")
            play_again = input("Do you want to play again? (Y/N)").upper()
            if play_again == "Y" or play_again == "YES":
                number_to_guess = randint(1, 10)
                user_guess = None
            else:
                print("Thanks for playing")
                break
    except ValueError:
        print(f"Invalid value '{user_guess}', enter an integer")
