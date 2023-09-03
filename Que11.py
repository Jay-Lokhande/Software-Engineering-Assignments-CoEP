import os

file_path = input("Enter the file path: ")
try:
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                print(line.strip())
    else:
        with open(file_path, "w") as file:
            file.write("hello world\njay\naman\nschool\nabcd")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

