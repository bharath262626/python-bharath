import os

folders = input("please provide list of folders names with spaces between:").split()

for folder in folders:
    folder = os.listdir(folder)
    folder = os.path.expanduser(folder)
    folder = os.path.normpath(folder)
    print(folder)
    print(folder)
    print(folder)