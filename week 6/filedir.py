# This grabs the current directory and prints all files.
import os
def cwd():
    path = os.getcwd()
    print(f"The current directory is {path}")
    print("The following files were found: ")
    for file in os.listdir(path):
        print(file)

def run():
    print("Processing.....")
    cwd()


if __name__ == "__main__":
    run()