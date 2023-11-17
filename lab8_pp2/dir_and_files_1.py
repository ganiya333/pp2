import os
def directories(path):
    ans= os.listdir(path)
    dir = [i for i in ans if os.path.isdir(os.path.join(path, i))]
    print("all directories:", dir)
def files(path):
    ans=os.listdir(path)
    files = [i for i in ans if os.path.isfile(os.path.join(path, i))]
    print("all files:", files)
def dirs_and_files(path):
    ans = os.listdir(path)
    print("all directories and files:", ans)

path=input()
directories(path)
files(path)
dirs_and_files(path)


