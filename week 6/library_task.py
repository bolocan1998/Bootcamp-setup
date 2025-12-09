

#This fuction reads chars
def display_chars(path,num):
    with open(path,'r') as file:
        text = file.read(num)
        print(text)

#This function reads 1 line
def display_line(path):
    with open(path,'r') as file:
        line=file.readline()
        print(line)
#This function reads all contents
def display_text(path):
    with open(path,'r') as file:
        text=file.read()
        print(text)

def run_task_2():
    print("Display chars:")
    display_chars("library.txt", 15)

    print("\nDisplay line:")
    display_line("library.txt")

    print("\nDisplay text:")
    display_text("library.txt")

def search(filename):
    print("Searching.....")
    with open(filename, "rt") as file:
        for line in file:
            print(f"Looked in {line.strip()}")
    print("Done")

def run_task_3():
    search("library.txt")


if __name__ == "__main__":
    run_task_3()