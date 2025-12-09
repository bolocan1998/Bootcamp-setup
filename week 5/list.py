#Write two functions:
#i) directions(): creates a list of steps with "Move Forward", "Move Backward", "Turn Left", "Turn Right" and returns it.
#ii) run_task1(): calls directions() and prints the returned list.

def directions():
    steps = ["move forward", "move backward", "turn left", "turn right"]
    return steps

def run_task1():
    steps_list = directions()
    print(steps_list)

def movements():
    path = ["move forward", 10, "move backward", 5, "turn left", 3, "turn right", 1]
    return path

def run_task2():
    print("Moving......")

    path_list = movements()

    for i in range(0, len(path_list), 2):
        direction = path_list[i]
        steps = path_list[i+1]
        print(f"{direction} for {steps} steps!")

def menu():
    print("Select a direction:")
    directions_list=directions()
def menu_and_input():
    print("Enter a direction [0-3] only!")
    directions_list = directions()

    for index, direction in enumerate(directions_list):
        print(f"{index}. {direction}")

    choice = int(input("Enter your choice! "))
    return directions_list[choice]

def run_task4():
    route = []
    print("Working out escape route/plan....")

    for _ in range(5):
        direction = menu_and_input()
        route.append(direction)
    print(f"Escape route: {route}")


if __name__ == "__main__":
   run_task1()
   run_task2()
