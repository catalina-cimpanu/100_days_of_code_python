import random
from higher_lower_data import data
import higher_lower_art as art


def higher_lower():
    print(art.logo)

    score = 0
    game_over = False

    while game_over == False:
        choice_A = random.choice(data)
        choice_B = random.choice(data)
        right_answer = ""
        if int(choice_A['follower_count']) > int(choice_B['follower_count']):
            right_answer = "A"
        else:
            right_answer = "B"

        print(f"------------- ROUND {score+1} ---------------")
        print(
            f"\nCompare A: {choice_A['name']}, a {choice_A['description']}, from {choice_A['country']}."
        )
        print(art.vs)
        print(
            f"Against B: {choice_B['name']}, a {choice_B['description']}, from {choice_B['country']}."
        )

        answer = input("\nWho has more followers? Type 'A' or 'B': ").upper()
        while answer != "A" and answer != "B":
            answer = input(
                "\nPlease give a valid answer. Who has more followers? Type 'A' or 'B': "
            ).upper()

        if answer == right_answer:
            score += 1
            print(f"\nCorrect! Your score is now {score} points.\n\n\n")
        else:
            print(f"\nWrong. Your final score is {score} points.\n")
            print("\n ---------  Game over ----------\n")
            game_over = True

    play_again = input(
        "Do you want to play again? Type 'yes' or 'no': ").lower()
    while play_again != "yes" and play_again != "no":
        play_again = input(
            "Please give a valid answer. Do you want to play again? Type 'yes' or 'no': "
        )

    if play_again == "yes":
        higher_lower()
    else:
        print("Bye bye!")


higher_lower()
