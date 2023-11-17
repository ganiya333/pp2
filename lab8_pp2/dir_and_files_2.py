import os
def check_fun(path):

    if os.path.exists(path):
        print("the path exists")
    else:
        print("the path does not exist")
        return
    
    if os.access(path,os.R_OK):
        print("the path is Readable")
    else:
        print("the path is not readable")


    if os.access(path,os.W_OK):
        print("the path is writable")
    else:
        print("the path is not not writable")


    if os.access(path,os.X_OK):
        print("the path is executable")
    else:
        print("the path is not not executable")

path = input()
check_fun(path)
