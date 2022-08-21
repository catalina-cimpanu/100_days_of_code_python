import random
# from replit import clear
import os
clear = lambda: os.system('cls')


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game_over = False

    player = random.choices(cards, k=2)
    dealer = random.choices(cards, k=2)

    while game_over == False:
        player_score = sum(player)
        dealer_score = sum(dealer)
        clear()
        print("Your cards:", player, ". Your score:", player_score)
        print("Dealer's first card:", dealer[0])

        if player_score == dealer_score == 21:
            print(
                f"Draw. Both the player and the dealer have blackjack. Your cards: {player}. Dealer's cards: {dealer}"
            )
            game_over = True
        elif player_score == 21:
            print(
                f"Blackjack! You win! Your cards: {player}. Dealer's cards: {dealer}"
            )
            game_over = True
        elif dealer_score == 21:
            print(
                f"Dealer has blackjack. You lose. Your cards: {player}. Dealer's cards: {dealer}"
            )
        else:
            if player_score > 21:
                if 11 in player:
                    print(
                        "You have an ace. Recalculating with ace as 1 instead of 11"
                    )
                    player.remove(11)
                    player.append(11)
                    player_score = sum(player)
                    print(f"Your new score is {player_score}")
                    # player_score_with_ace = player_score - 10
                    if player_score > 21:
                        print(
                            f"You lose. Your cards: {player}. Dealer's cards: {dealer}"
                        )
                        game_over = True
                    else:
                        print(f"Your new score is: {player_score}")
                else:
                    print(
                        f"You lose. Your cards: {player}. Dealer's cards: {dealer}"
                    )
                    game_over = True
            else:
                want_new_card = input(
                    "Do you want another card? Type 'yes' or 'no': ").lower()
                while want_new_card != "yes" and want_new_card != "no":
                    want_new_card = input(
                        "Please give a valid answer. Do you want another card? Type 'yes' or 'no': "
                    ).lower()
                if want_new_card == "yes":
                    new_card = random.choice(cards)
                    player.append(new_card)
                else:
                    while dealer_score < 17:
                        new_card = random.choice(cards)
                        dealer.append(new_card)
                        dealer_score = sum(dealer)
                        print("Dealer draws card. Dealer's cards: ", dealer,". Dealer's score: ", dealer_score)
                    if dealer_score > 21:
                        print(
                            f"You win! Your score is {player_score}, dealer's score is {dealer_score}. "
                        )
                        game_over = True
                    else:
                        if player_score == dealer_score:
                            print(
                                f"Draw. Your cards: {player}. Dealer's cards: {dealer}"
                            )
                        elif player_score > dealer_score:
                            print(
                                f"You win! Your score is {player_score}, dealer's score is {dealer_score}. "
                            )
                        else:
                            print(
                                f"You lose. Your score is {player_score}, dealer's score is {dealer_score}. "
                            )
                        game_over = True

    play_again = input(
        "\nDo you want to play again? Type 'yes' or 'no'.\n").lower()
    while play_again != "yes" and play_again != "no":
        play_again = input(
            "Please give a valid answer. Do you want to play again? Type 'yes' or 'no'.\n"
        ).lower()
    if play_again == "yes":
        blackjack()
    else:
        print("Bye bye then! ")


blackjack()
