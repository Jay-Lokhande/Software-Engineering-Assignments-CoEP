import os

# Define the directory path you want to create
directory_path = input("Enter Directory name: ")

# Check if the directory already exists
if not os.path.exists(directory_path):
    # If it doesn't exist, create it
    os.makedirs(directory_path)
    print(f"Directory '{directory_path}' created successfully.")
else:
    print(f"Directory '{directory_path}' already exists.")
