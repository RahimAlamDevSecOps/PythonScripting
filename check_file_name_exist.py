import os
filename = "file9"
if os.path.exists(filename):
    print(f"{filename} exists")
else:
    print(f"{filename} does not exist")
