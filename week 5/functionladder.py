def dispalay_ladder(steps):
    print("| |")
    for step in range(steps):
        print("***")
        print("| |")
def create_ladder():
    print("How many steps remain?")
    steps=int(input())
    dispalay_ladder(steps)

create_ladder()

