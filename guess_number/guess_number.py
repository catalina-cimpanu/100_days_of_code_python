import random
import guess_art as art


def guess_number():
    print(art.logo)

    number = random.randint(1, 100)

    level = input("Please choose difficulty: type 'easy' or 'hard': ").lower()
    while level != "easy" and level != "hard":
        level = input(
            "Please choose a valid difficulty: type 'easy' or 'hard': ").lower(
            )
    if level == "easy":
        attempts = 10
    else:
        attempts = 5

    player_won = False

    while attempts > 0 and player_won == False:
        user_number = int(input("Choose a number between 1 and 100: "))
        while user_number < 1 or user_number > 100:
            user_number = int(
                input(
                    "Invalid choice. Please choose a number between 1 and 100")
            )

        if user_number == number:
            print(f"\nYou win! The number to guess was {number}.")
            player_won = True
        elif user_number > number:
            attempts -= 1
            print("Too high.")

        else:
            attempts -= 1
            print("Too low.")

    if player_won == False:
        print("Sorry, you lost. ")

    play_again = input(
        "\nDo you want to play again? Type'yes' or 'no': ").lower()
    while play_again != "yes" and play_again != "no":
        play_again = input(
            "Please give a valid answer. Do you want to play again? Type'yes' or 'no': "
        ).lower()

    if play_again == "yes":
        guess_number()
    else:
        print("Bye bye!")


guess_number()
