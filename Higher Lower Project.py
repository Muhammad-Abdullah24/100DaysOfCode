import random
from art import logo
from art import vs
from game_data import data

print(logo)
print("Welcome to the game 'Higher or Lower'")

score = 0
game_should_continue = True

# Randomly pick the first account to compare
account_a = random.choice(data)

while game_should_continue:
    # Move B to A and generate a new B
    account_b = account_a
    account_a = random.choice(data)

    # Ensure A and B are not the same
    while account_b == account_a:
        account_b = random.choice(data)

    name1 = account_a["name"]
    follower_count1 = account_a["follower_count"]
    description1 = account_a["description"]
    country1 = account_a["country"]

    name2 = account_b["name"]
    follower_count2 = account_b["follower_count"]
    description2 = account_b["description"]
    country2 = account_b["country"]

    print(f"\nCompare A: {name1}, a {description1}, from {country1}")
    print(vs)
    print(f"Against B: {name2}, a {description2}, from {country2}")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Determine the correct answer
    correct_answer = "A" if follower_count1 > follower_count2 else "B"

    if choice == correct_answer:
        score += 1
        print(f"✅ You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"❌ Sorry, that's wrong. Final score: {score}")


