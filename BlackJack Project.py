from urllib.parse import uses_relative

from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def add_to_user_cards():
    user_cards.append(cards[random.randint(0, len(cards) - 1)])

def add_to_computer_cards():
    computer_cards.append(cards[random.randint(0, len(cards) - 1)])

def total_score(card_pile):
    total = 0
    for index in range(len(card_pile)):
        total += card_pile[index]
    return total

print("Welcome to the game 'BLACK JACK' ")

choice = input("Would you like to play? ")
if choice.lower() == "y":
    not_end = True
    not_done = True
    for i in range(0, 2):
        add_to_user_cards()
        add_to_computer_cards()

    while not_end and not_done:
        print(f"Your cards: {user_cards}")
        print(f"Total score: {total_score(user_cards)}")

        print(f"Computer's first card: {computer_cards[0]}")

        more = input("Do you want more cards? ('y' or 'n')")

        computer_draw = random.randint(0,1)

        if computer_draw == 1:
            add_to_computer_cards()
            if total_score(computer_cards) > 21:
                not_end = False
                print(f"You won, Computer busted: {computer_cards} with a score: {total_score(computer_cards)}")
                print(f"Your cards: {user_cards}")
                print(f"Total score: {total_score(user_cards)}")

        if more.lower() == "y":
            add_to_user_cards()
            if total_score(user_cards) > 21:
                not_end = False
                print(f"Busted!!!: {user_cards} with a score: {total_score(user_cards)}")
                print(f"Your cards: {user_cards}")
                print(f"Computer's cards: {computer_cards}")

        elif more.lower() == "n":
            not_done = False
            if total_score(user_cards) > total_score(computer_cards):
                print(f"You won!!! SCORE: {total_score(user_cards)}")
                print(f"Computer's SCORE: {total_score(computer_cards)}")

elif choice.lower() == "n":
    exit()

