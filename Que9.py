import os

file_path = input("Enter the file path: ")

if os.path.exists(file_path):
    with open(file_path, "a") as file:
        file.write("hello world\n")
        print(f"'hello world' appended to '{file_path}'")
else:
    with open(file_path, "w") as file:
        file.write("hello world\n")
        print(f"'hello world' written to a new file '{file_path}'")
