import os

def check_fun(path):
    if os.path.exists(path):
        print("The path exists")
        x=os.path.basename(path)
        y=os.path.dirname(path)
        print(f"Filename: {x}")
        print(f"Directory: {y}")
    else:
        print(f"The path does not exist.")
        return
    
    
x = input()
check_fun(x)
