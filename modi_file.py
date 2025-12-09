# import os
# filename = "data.txt"
# if os.path.exists(filename):
#     with open(filename, "r") as file:
#         content = file.read()
#         print(content)
# else:
#     print("File does not exist.")

import os


filename = "data.txt"


# Check if the file already exists
if os.path.exists(filename):
    confirm = input(f"The file '{filename}' already exists. Overwrite? (y/n): ")
    if confirm.lower() != "y":
        print("Operation cancelled.")
    else:
        with open(filename, "w") as file:
            file.write("New data written to the file.")
            print("File overwritten successfully.")
else:
    with open(filename, "w") as file:
        file.write("New file created.")
        print("File created successfully.")

#import csv
# with open("data.csv") as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
#    for row in csv_reader:
#        print(row[0])