import random

while True:
    input("Press enter to roll the dice or q to quit: ")
    roll = random.randint(1,6)
    print(f"You rolled a {roll}")

    again = input("Would you like to roll again? (y/n): ")
    if again != "y":
        print("Goodbye")
        break