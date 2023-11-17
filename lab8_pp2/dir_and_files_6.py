import string
import os

def check_fun():
    for i in string.ascii_uppercase:
        file_name = f"{i}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is the content of file {file_name}")
        print(f"File {file_name} created successfully.")

check_fun()