from art import logo
import random

print(logo)
print("Welcome to the number guessing game!!!")

choice = input("Choose a difficulty level ('easy' or 'hard'): ")

if choice.lower() == "easy":
    tries = 10
else:
    tries = 5

print("I am thinking of a number (1 - 100) ")
not_done = True
number = random.randint(0,100)
while tries > 0 and not_done == True:
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high")
        tries -=1
        print(f"You have {tries} tries left")
    elif guess < number:
        print("Too low")
        tries -=1
        print(f"You have {tries} tries left")
    else:
        print("You won!")
        not_done = False
