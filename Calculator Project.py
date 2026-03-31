from art import logo

print(logo)
print()
not_done = True

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

n1 = float(input("Please enter number 1: "))

while not_done:

    print("""
    +
    -
    *
    /   
    """)

    operation = input("Please choose one of the following operations: ")
    n2 = float(input("Please enter number 2: "))


    result = operations[operation](n1, n2)

    print(f"{n1} {operation} {n2} = {result}")

    choice = input("Do you want to use this result or start anew?('y' for using the result and 'n' for starting anew) ")
    if choice.lower() == "y":
        n1 = result
    else:
        n1 = float(input("Please enter number 1: "))

