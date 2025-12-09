


import FUNCTIONS.test1 as Ftest1
import FUNCTIONS.test2 as Ftest2


def run():
    while True:
        print("What would you like to do?")
        response = input("Run week 1&2 [t] or quit [q]: ")

        if response == "t":
            number = int(input("Enter a number (test 1) or (test 2) - [1,2]: "))
            if number == 1:
                Ftest1.simple_message()
            elif number == 2:
                Ftest2.simple_message()
            else:
                print("Invalid input")
        elif response == "q":
            break
        else:
            print("Invalid input")


run()