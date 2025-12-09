import csv

def read_csv(path):
    with open(path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print("headings")
        print(headings)

        print("Values:")
        for row in csv_reader:
            print(row)

def run_task_1():
    read_csv("clothing.csv")



if __name__ == "__main__":
    run_task_1()