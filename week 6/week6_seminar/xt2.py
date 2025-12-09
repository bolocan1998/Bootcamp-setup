def display_chars(file_path, num_chars):
    with open(file_path,'r') as file:
        content = file.read(num_chars)
        print(f'the first {num_chars} characters are : ')
        print(content)

def display_line(file_path):
    with open(file_path,'r') as file:
        firs_lie= file.readline()
        print("The first lie is : ")
        print(firs_lie)

def display_text(file_path):
    with open(file_path,'r') as file:
        content= file.read()
        print("The full text is : ")
        print(content)

def run():
    file_path="librari.txt"
    display_chars(file_path, num_chars=5)
    print()
    display_line(file_path)
    print()
    display_text(file_path)

if __name__ == "__main__":
    run()