import os

folders = input("Enter a list of folder paths separated by spaces: ").split()

for folder in folders:
     # Convert Git Bash style `/c/...` to Windows `C:/...`
     if folder.startswith("/c/"):
          folder = folder.replace("/c/", "c:/", 1)
     folder = os.path.normpath(folder)
     try:
           files = os.listdir(folder)
           print(f"\ncontents of {folder}:")
           for f in files:
                 print(f" {f}")
     except FileNotFoundError:
        print(f"folder not found: {folder}")     
