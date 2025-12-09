def search(filename):
    print("Searching")
    file=open(filename,'r')
    for line in file:
        location=line.strip()
        print(f" Looked in {location}")
    file.close()
def run():
    search("librari.txt")

if __name__ == '__main__':
    run()