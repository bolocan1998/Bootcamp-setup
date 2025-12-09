def search_books(path):
    print("Searching.....", end="")
    sections = ""
    books = "Books:\n"

    with open(path, "rt") as file:
        for line in file:
            line = line.strip()
            if line.startswith("Section"):
                sections += line + "\n"
            elif line:
                books += line + "\n"
    print("Done!")
    return f"{sections}\n\n{books}"

def save(path, data):
    print("Saving.....")
    with open(path, "wt") as file:
        file.write(data)
    print("Done!")

def run_task_4():
    data = search_books("books.txt")
    save("section-books.txt", data)


if __name__ == "__main__":
    run_task_4()