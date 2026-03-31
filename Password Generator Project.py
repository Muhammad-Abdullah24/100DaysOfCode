import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))

collection = []
password = ""


for i in range(0,n_letters):
    choice = random.randint(0,51)
    collection.append(letters[choice])

for i in range(0,n_numbers):
    choice = random.randint(0,len(numbers)-1)
    collection.append(numbers[choice])

for i in range(0,n_symbols):
    choice = random.randint(0,len(symbols)-1)
    collection.append(symbols[choice])

random.shuffle(collection)
for characters in collection:
    password += characters


print("Your random generated password is: " + password)