def observed():
    observation=set()
    observation.add("car")
    observation.add("car")
    observation.add("bus")
    observation.add("bus")
    observation.add("bike")
    observation.add("train")
    return observation
def run():
    result_set=observed()
    print(result_set)
if __name__ == '__main__':
    run()