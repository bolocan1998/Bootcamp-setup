def direction():
    steps=[]
    steps.append("Move Forward")
    steps.append("Move Backward")
    steps.append("Move Left")
    steps.append("Move Right")
    return steps
def run_task():
    direction_list=direction()
    print(direction_list)

run_task()