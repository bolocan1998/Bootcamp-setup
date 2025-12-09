import os
def cwd():
    path=os.getcwd()
    print(f'The current working directory is {path}')
    print("The Directory contain the following lines: ")
    for file in os.listdir(path):
        print(file)

def run():
    print("processing....")
    cwd()

if __name__ == "__main__":
    run()
